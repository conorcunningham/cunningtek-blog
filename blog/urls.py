from . views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views
from django.urls import path

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about', views.about, name='blog-about')
]
