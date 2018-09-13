from django.shortcuts import render
from blog.models import Announcement
from .models import Profiles
import psycopg2

def index(request):
	ann = Announcement.objects.all()[::-1]
	feeds = Profiles.objects.all()[0]
	context = {
		'ann': ann[0:5],
		'feeds': feeds.description
	}
	return render(request, 'putin/home.html', context)
