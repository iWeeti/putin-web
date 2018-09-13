from django.shortcuts import render
from blog.models import Announcement
from .models import Settings
import psycopg2

def index(request):
	ann = Announcement.objects.all()[::-1]
	settings = Settings.objects.using('bot').all()[0]
	context = {
		'ann': ann[0:5],
		'settings': settings
	}
	return render(request, 'putin/home.html', context)
