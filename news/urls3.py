from django.urls import path
from .views import CatSubscribe


urlpatterns = [
   path('subscribe', CatSubscribe.as_view(), name='news_list'),
]
