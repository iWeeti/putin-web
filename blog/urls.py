from django.urls import path
from .views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	CommentCreateView,
	CommentEditView,
	CommentDeleteView)
from . import views

urlpatterns = [
	path('', PostListView.as_view(), name='blog-home'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/new', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
	path('post/<int:post>/comment', CommentCreateView.as_view(), name='comment-create'),
	path('post/<int:post>/comments/<int:pk>/edit', CommentEditView.as_view(), name='comment-edit'),
	path('post/<int:post>/comments/<int:pk>/delete', CommentDeleteView.as_view(), name='comment-delete'),
	path('about/', views.about, name='blog-about'),
	path('announcements/', views.announcements, name='blog-announcements'),
	path('chat/', views.chat, name='blog-chat'),
]