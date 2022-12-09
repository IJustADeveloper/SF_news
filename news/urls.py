from django.urls import path
from .views import NewsList, PostDetail, NewsCreate, NewsUpdate, PostDelete, ArtCreate, ArtList, ArtUpdate


urlpatterns = [
   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>', PostDetail.as_view(), name='news_detail'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
]