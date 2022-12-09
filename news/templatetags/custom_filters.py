from django import template

register = template.Library()

censor_words = [
    "редиска",
    "ретька",
    "flask",
    "тесто"
]


@register.filter()
def censor(value):
    returned = value

    for i in censor_words:
        splited = returned.split(i[1::])
        stars = "*" * len(i[1::])
        returned = stars.join(splited)

    return returned


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()
