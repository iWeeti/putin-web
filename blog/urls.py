from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
	path('', views.home, name='blog-home'),
	path('posts/', PostListView.as_view(), name='blog-posts'),
	path('about/', views.about, name='blog-about'),
	path('announcements/', views.announcements, name='blog-announcements'),
]