from django.shortcuts import render
from blog.models import Announcement
from .models import Settings, Profiles
import psycopg2

def index(request):
	ann = Announcement.objects.all()[::-1]
	if request.user.is_authenticated:
		profile = Profiles.objects.using('bot').get(pk=request.user.discorduser.id)
		test = request.user.discorduser.id
	else:
		profile = None
	context = {
		'ann': '1',
		'profile': profile,
		'test': test
	}
	return render(request, 'putin/home.html', context)
