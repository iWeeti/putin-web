from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Announcement


def home(request):
	ann = Announcement.objects.all()[:3:-1]
	context = {
		'posts': Post.objects.all()[::-1],
		'ann': ann
	}
	return render(request, 'blog/home.html', context)


class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		context.update({
			'posts': Post.objects.order_by('-date_posted'),
			'ann': Announcement.objects.all()[:-2:-1],
		})
		return context


class PostDetailView(DetailView):
	model = Post

	def get_context_data(self, **kwargs):
		context = super(PostDetailView, self).get_context_data(**kwargs)
		context.update({
			'ann': Announcement.objects.all()[:3:-1],
		})
		return context


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
