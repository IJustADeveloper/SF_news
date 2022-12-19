from django_filters import FilterSet, DateTimeFilter,CharFilter, MultipleChoiceFilter
from django.forms import DateTimeInput
from .models import Category


class PostFilter(FilterSet):
    creation_date = DateTimeFilter(
        label='Дата создания',
        field_name='creation_date',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%d',
            attrs={'type': 'datetime-local'},
        ),
    )
    title = CharFilter(label='Заголовок', lookup_expr='icontains')
    fptc = MultipleChoiceFilter(label='Категория', choices=Category.get_choices())



