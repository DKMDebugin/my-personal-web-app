# blog urls module
from django.urls import path

from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='PostListView'),
    path('<slug>', PostDetailView.as_view(), name='PostDetailView'),
]
