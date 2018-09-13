from django.shortcuts import render
from blog.models import Announcement
import psycopg2

def index(request):
	ann = Announcement.objects.all()[::-1]
	context = {
		'ann': ann[0:5]
	}
	return render(request, 'putin/home.html', context)
