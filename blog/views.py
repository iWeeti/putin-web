from django.shortcuts import render
from .models import Post, Announcement


def home(request):
	posts = Post.objects.all()[::-1]
	ann = Announcement.objects.all()[:3:-1]
	context = {
		'posts': posts,
		'ann': ann
	}
	return render(request, 'blog/home.html', context)


def about(request):
	ann = Announcement.objects.all()[:3:-1]
	context = {
		'title': 'About',
		'ann': ann
	}
	return render(request, 'blog/about.html', context)

def announcements(request):
	ann = Announcement.objects.all()[:3:-1]
	context = {
		'announcements': Announcement.objects.all()[::-1],
		'ann': ann
	}
	return render(request, 'blog/announcements.html', context)
