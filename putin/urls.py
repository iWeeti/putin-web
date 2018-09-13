from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='putin-me'),
	path('profile/', views.profile, name='putin-profile'),
]