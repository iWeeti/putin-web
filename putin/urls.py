from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='putin-me'),
	path('profile/', views.profile, name='putin-profile'),
	path('guilds/', views.guilds, name='putin-guilds'),
	path('invite/', views.invite, name='putin-invite'),
]
