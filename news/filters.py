from django_filters import FilterSet, DateTimeFilter, ChoiceFilter
from django.forms import DateTimeInput
from .models import Post, PostCategory


class PostFilter(FilterSet):
    creation_date = DateTimeFilter(
        field_name='creation_date',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%d',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            #'postcategory': ['exact', 'contains'],
        }


