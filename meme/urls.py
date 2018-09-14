from django.urls import path

urlpatterns = [
	path('', views.meme, 'meme')
]