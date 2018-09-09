from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView)
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
		ann = Announcement.objects.all()[::-1]
		context.update({
			'posts': Post.objects.order_by('-date_posted'),
			'ann': ann[0:3],
		})
		return context


class PostDetailView(DetailView):
	model = Post

	def get_context_data(self, **kwargs):
		context = super(PostDetailView, self).get_context_data(**kwargs)
		ann = Announcement.objects.all()[::-1]
		context.update({
			'ann': ann[0:3],
		})
		return context


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(PostCreateView, self).get_context_data(**kwargs)
		ann = Announcement.objects.all()[::-1]
		context.update({
			'ann': ann[0:3],
		})
		return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author

	def get_context_data(self, **kwargs):
		context = super(PostUpdateView, self).get_context_data(**kwargs)
		ann = Announcement.objects.all()[::-1]
		context.update({
			'ann': ann[0:3],
		})
		return context


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	fields = ['title', 'content']
	success_url = 'blog/'

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author

	def get_context_data(self, **kwargs):
		context = super(PostDeleteView, self).get_context_data(**kwargs)
		ann = Announcement.objects.all()[::-1]
		context.update({
			'ann': ann[0:3],
		})
		return context


def about(request):
	ann = Announcement.objects.all()[::-1]
	context = {
		'title': 'About',
		'ann': ann[0:3],
	}
	return render(request, 'blog/about.html', context)

def announcements(request):
	ann = Announcement.objects.all()[::-1]
	context = {
		'title': 'Announcements',
		'announcements': Announcement.objects.all()[::-1],
		'ann': ann[0:3]
	}
	return render(request, 'blog/announcements.html', context)
