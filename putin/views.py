from django.shortcuts import render
from blog.models import Announcement
from django.contrib.auth.decorators import login_required
from .models import Settings, Profiles
import requests
import json

def index(request):
	ann = Announcement.objects.all()[::-1]
	context = {
		'ann': ann,
	}
	return render(request, 'putin/home.html', context)

# @login_required
def profile(request):
	ann = Announcement.objects.all()[::-1]
	try:
		uid = request.GET['uid']
	except:
		uid = None
	if not uid is None:
		try:
			profile = Profiles.objects.using('bot').get(id=uid)
		except:
			if request.user.is_authenticated:
				try:
					profile = Profiles.objects.using('bot').get(id=request.user.discorduser.uid)
				except:
					profile = None
				else:
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

def guilds(request):
	guilds = requests.get('https://discordapp.com/api/users/@me/guilds').json()
	context = {
		'guilds': guilds
	}
	return render(request, 'putin/guilds.html', context)
