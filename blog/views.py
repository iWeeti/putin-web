from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView)
from .models import Post, Announcement, Comment


def home(request):
	context = {
		'title': 'Blog'
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
			'title':'Post',
			'posts': Post.objects.order_by('-date_posted')
		})
		return context


class PostDetailView(DetailView):
	model = Post

	def get_context_data(self, **kwargs):
		context = super(PostDetailView, self).get_context_data(**kwargs)
		post = self.get_object()
		context.update({
			'object': post,
			'title': 'Post - ' + post.title,
			'comments': Comment.objects.all().filter(parent=post)
		})

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
	model = Comment
	fields = ['message']

	def form_valid(self, form):
		form.instance.author = self.request.user
		form.instance.parent = self.request.kwargs.get('post')
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		form.instance.edited = True
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author

	def get_context_data(self, **kwargs):
		context = super(PostUpdateView, self).get_context_data(**kwargs)
		context.update({
			'comments': Comment.objects.all().filter(pk=self.request.kwargs.get('post'))
		})
		return context


class CommentEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Comment
	fields = ['message']

	def form_valid(self, form):
		form.instance.author = self.request.user
		form.instance.parent = self.request.kwargs.get('post')
		form.instance.edited = True
		return super().form_valid(form)

	def test_func(self):
		comment = self.get_object()
		return self.request.user == comment.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	fields = ['title', 'content']
	success_url = '/blog/'

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Comment
	fields = ['message']
	
	def get_success_url(self):
		return f"/blog/{self.request.kwargs.get('post')}"

	def test_func(self):
		comment = self.get_object()
		return self.request.user == comment.author


def about(request):
	context = {
		'title': 'About',
	}
	return render(request, 'blog/about.html', context)

def announcements(request):
	context = {
		'title': 'Announcements',
		'announcements': Announcement.objects.order_by('-date_posted'),
		'ann': ann[0:3]
	}
	return render(request, 'blog/announcements.html', context)

def chat(request):
	context = {
		'title': 'Chat',
	}
	return render(request, 'blog/chat.html', context)
