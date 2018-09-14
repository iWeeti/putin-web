from django.shortcuts import render
from blog.models import Announcement
from django.contrib.auth.decorators import login_required
from .models import Settings, Profiles
import requests
import json
from discord_bind import conf
import config

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
		'ann': ann[0:3],
		'profile': profile,
	}
	return render(request, 'putin/profile.html', context)

def guilds(request):
	ann = Announcement.objects.all()[::-1]
	guilds = requests.get('https://discordapp.com/api/users/@me/guilds', headers={'Authorization': f'Bearer {request.user.discorduser.access_token}'}).json()
	_guilds = []
	bot_guilds = requests.get('https://discordapp.com/api/guilds/', headers={'Authorization': f'Bot {config.token}'})
	context = {
		'ann': ann,
		'guilds': _guilds
	}
	return render(request, 'putin/guilds.html', context)
