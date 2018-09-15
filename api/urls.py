from django.urls import path, include
from . import views
from putin_web import router

urlpatterns = [
	path('meme/', views.meme, name='meme'),
	path('rr/', views.rr, name='rr'),
	path('profile/', include(router.urls)),
]