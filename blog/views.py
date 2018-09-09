from django.shortcuts import render
from .models import Post


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context=context)


def about(request):
	context = {
		'title': 'About'
	}
	return render(request, 'blog/about.html', context)

def announcements(request):
	return render(request, 'blog/announcements.html')
