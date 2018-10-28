from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='putin-me'),
	path('profile/<int:uid>', views.profile, name='putin-profile'),
	path('guilds/', views.guilds, name='putin-guilds'),
	path('invite/<int:guild_id>', views.invite, name='putin-invite'),
	path('dashboard/', views.dashboard, name='putin-dashboard'),
]
