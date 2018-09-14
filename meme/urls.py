from django.urls import path
from . import views

urlpatterns = [
	path('', views.meme, 'meme', name='meme-return')
]