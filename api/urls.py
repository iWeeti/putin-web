from django.urls import path
from . import views

urlpatterns = [
	path('meme/', views.meme, name='meme'),
	path('rr/', views.rr, name='rr'),
]