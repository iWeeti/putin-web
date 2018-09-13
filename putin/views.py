from django.shortcuts import render
from blog.models import Announcement, Feeds
import psycopg2

def index(request):
	ann = Announcement.objects.all()[::-1]
	feeds = Feeds.objects.all()
	context = {
		'ann': ann[0:5],
		'feeds': feeds
	}
	return render(request, 'putin/home.html', context)
