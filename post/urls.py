from django.urls import path
from .views import CreatePost, ListPost


urlpatterns = [
    path('create/', CreatePost, name='post-create'),
    path('list/', ListPost, name='post-list')
]