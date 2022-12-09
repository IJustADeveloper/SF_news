from django.urls import path
from .views import NewsList, PostDetail, NewsCreate, NewsUpdate, PostDelete, ArtCreate, ArtList, ArtUpdate


urlpatterns = [
   path('', ArtList.as_view(), name='art_list'),
   path('<int:pk>', PostDetail.as_view(), name='art_detail'),
   path('create/', ArtCreate.as_view(), name='art_create'),
   path('<int:pk>/update/', ArtUpdate.as_view(), name='art_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='art_delete'),
]