from django.shortcuts import render, redirect
from blog.models import Announcement
from django.contrib.auth.decorators import login_required
from .models import Settings, Profiles, Guilds
import requests
import json
from discord_bind import conf
from . import config

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
	guild_ids = [_['id'] for _ in guilds]
	bot_guilds = Guilds.objects.using('bot').all()
	_guilds = []
	
	print(bot_guilds)
	context = {
		'ann': ann,
		'guilds': _guilds
	}
	return render(request, 'putin/guilds.html', context)

def invite(request):
	return redirect('https://discordapp.com/api/oauth2/authorize?client_id=488929645186514954&permissions=8&redirect_uri=https%3A%2F%2Fw-bot.ml%2Fdiscord%2Fcb&scope=bot')
