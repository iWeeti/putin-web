from django.shortcuts import render

posts = [
	{
		'author': 'CoreyMS',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'September 8, 2018'
	},
	{
		'author': 'Veeti',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'September 9, 2018'
	}
]


def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context=context)


def about(request):
	context = {
		'title': 'About'
	}
	return render(request, 'blog/about.html', context)
