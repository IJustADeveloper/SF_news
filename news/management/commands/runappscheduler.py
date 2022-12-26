import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from datetime import datetime, timedelta
from django.core.mail import EmailMultiAlternatives
from news.models import Category, Post
from django.template.loader import render_to_string
from django.conf import settings

logger = logging.getLogger(__name__)


def my_job():
    today = datetime.today()
    for i in Category.objects.all():
        cat = i
        for j in cat.subscribers.all():
            posts = Post.objects.filter(fptc__in=[cat], creation_date__range=[today + timedelta(days=-7), today])
            data = {'user_name': j.username, 'href': 'http://' + settings.SITE_URL + "/news/",
                    'cat_name': cat.name, 'posts': posts}
            html_content = render_to_string('multiple_notif_email.html', {'data': data})

            msg = EmailMultiAlternatives(
                subject="Новые посты в категории " + cat.name,
                body=cat.name,
                from_email='NewsPortalPRJ@yandex.ru',
                to=[j.email],
            )
            msg.attach_alternative(html_content, "text/html")

            msg.send()


def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(
                day_of_week="sun", hour="00", minute="00"
            ),
            id="my_job",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
