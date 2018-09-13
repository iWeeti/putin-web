from django.shortcuts import render
from blog.models import Announcement
from django.contrib.auth.decorators import login_required
from .models import Settings, Profiles
import psycopg2

def index(request):
	ann = Announcement.objects.all()[::-1]
	context = {
		'ann': ann,
	}
	return render(request, 'putin/home.html', context)

@login_required
def profile(request):
	ann = Announcement.objects.all()[::-1]
	if not request.GET is None:
		try:
			profile = Profiles.objects.using('bot').get(id=request.GET['uid'])
		except:
			profile = None
	else:
		if request.user.is_authenticated:
			try:
				profile = Profiles.objects.using('bot').get(id=request.user.discorduser.uid)
			except:
				profile = None
		else:
			profile = None
	context = {
		'ann': ann,
		'profile': profile,
	}
	return render(request, 'putin/profile.html', context)