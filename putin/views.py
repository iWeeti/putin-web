from django.shortcuts import render, redirect
from django.contrib import messages
from blog.models import Announcement
from django.contrib.auth.decorators import login_required
from .models import Settings, Profiles, Guilds
import requests
import json
from discord_bind import conf
from . import config
from .forms import SettingsForm
import discord
import time

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

@login_required
def guilds(request):
	ann = Announcement.objects.all()[::-1]
	guilds = requests.get('https://discordapp.com/api/users/@me/guilds', headers={'Authorization': f'Bearer {request.user.discorduser.access_token}'}).json()
	bot_guilds = Guilds.objects.using('bot').all()
	bot_guilds_ids = [_.id for _ in bot_guilds]
	_guilds = []
	for guild in guilds:
		guild_perms = discord.Permissions(int(guild['permissions']))
		if guild['id'] in str(bot_guilds_ids) and guild_perms.manage_guild or guild_perms.administrator or guild_perms.manage_channels:
			_guilds.append(guild)
	__guilds = []
	for index, guild in enumerate(_guilds):
		if index <= 3:
			try:
				__guilds[0]
			except IndexError:
				__guilds[0] = []
			__guilds[0].append(guild)
		if index <= 6 and index > 3:
			try:
				__guilds[1]
			except IndexError:
				__guilds[1] = []
			__guilds[1].append(guild)
		if index <= 9 and index > 6:
			try:
				__guilds[3]
			except IndexError:
				__guilds[3] = []
			__guilds[2].append(guild)
		if index <= 12 and index > 9:
			try:
				__guilds[3]
			except IndexError:
				__guilds[3] = []
			__guilds[3].append(guild)
		if index <= 15 and index > 12:
			try:
				__guilds[4]
			except IndexError:
				__guilds[4] = []
			__guilds[4].append(guild)

	context = {
		'ann': ann,
		'_guilds': _guilds
	}
	return render(request, 'putin/guilds.html', context)

@login_required
def dashboard(request):
	try:
		request.GET['id']
	except KeyError:
		return redirect('putin-guilds')
	guilds = requests.get('https://discordapp.com/api/users/@me/guilds', headers={'Authorization': f'Bearer {request.user.discorduser.access_token}'}).json()
	bot_guilds = Guilds.objects.using('bot').all()
	bot_guilds_ids = [_.id for _ in bot_guilds]
	_guilds = []
	__guilds = {}
	for guild in guilds:
		guild_perms = discord.Permissions(int(guild['permissions']))
		if guild['id'] in str(bot_guilds_ids) and guild_perms.manage_guild or guild_perms.administrator or guild_perms.manage_channels:
			_guilds.append(guild['id'])
			__guilds[guild['id']] = guild
	if not request.GET['id'] in _guilds:
		messages.warning(request, 'You do not have access to change the settings of this guild.')
		time.sleep(1)
		return redirect('putin-guilds')
	if request.method == 'POST':
		ann = Announcement.objects.all()[::-1]
		_settings = Settings.objects.using('bot').get(pk=request.GET['id'])
		form = SettingsForm(request.POST, instance=_settings)
		form.save()
		# .get(id=int(request.GET['id']))
		# form = SettingsForm(instance=_settings)
		context = {
			'ann': ann,
			'guild_id': request.GET['id'],
			'settings': form,
			'guild': __guilds[request.GET['id']]
		}
		return render(request, 'putin/dashboard.html', context)
	else:
		ann = Announcement.objects.all()[::-1]
		_settings = Settings.objects.using('bot').get(pk=request.GET['id'])
		if not _settings:
			_settings = Settings(id=request.GET['id'])
		# .get(id=int(request.GET['id']))
		form = SettingsForm(instance=_settings)
		context = {
			'ann': ann,
			'guild_id': request.GET['id'],
			'settings': form,
			'guild': __guilds[request.GET['id']]
		}
		return render(request, 'putin/dashboard.html', context)

def invite(request):
	return redirect('https://discordapp.com/api/oauth2/authorize?client_id=488929645186514954&permissions=8&redirect_uri=https%3A%2F%2Fw-bot.ml%2Fdiscord%2Fcb&scope=bot')
