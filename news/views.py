from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Post, Category, User
from .forms import PostForm, CatSubForm
from .filters import PostFilter


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.filter(type='N').order_by('creation_date').reverse()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news_one.html'
    context_object_name = 'news_one'


class NewsCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'news.add_post'
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'N'
        post.save()
        for i in form.cleaned_data['fptc']:
            cat = Category.objects.get(id=i)
            for j in cat.subscribers.all():
                data = {'user_name': j.username, 'href': 'http://'+self.request.get_host()+"/news/"+str(post.id),
                        'cat_name': cat.name, 'desc': post.preview()}
                html_content = render_to_string('notification_email.html', {'data': data})

                msg = EmailMultiAlternatives(
                    subject="Новые посты в категории "+cat.name,
                    body=cat.name,
                    from_email='NewsPortalPRJ@yandex.ru',
                    to=[j.email],
                )
                msg.attach_alternative(html_content, "text/html")

                msg.send()
        return redirect('/news')


class NewsUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'news.change_post'
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = 'news.delete_post'
    raise_exception = True
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news_list')


class ArtList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.filter(type='P').order_by('creation_date').reverse()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArtCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'news.add_post'
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class ArtUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'news.change_post'
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class CatSubscribe(LoginRequiredMixin, FormView):
    form_class = CatSubForm
    template_name = 'cat_subscribe.html'

    def form_valid(self, form):
        cat = form.cleaned_data
        print(cat)
        for i in cat['id']:
            c = Category.objects.get(id=int(i))
            c.subscribers.add(User.objects.get(id=self.request.user.id))
        return redirect('/news')
