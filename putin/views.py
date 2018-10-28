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
	_guilds = requests.get('https://discordapp.com/api/users/@me/guilds', headers={'Authorization': f'Bearer {request.user.discorduser.access_token}'}).json()
	bot_guilds = Guilds.objects.using('bot').all()
	bot_guilds_ids = [_.id for _ in bot_guilds]
	guilds = []
	for guild in _guilds:
		guild_perms = discord.Permissions(int(guild['permissions']))
		if guild['id'] in str(bot_guilds_ids):
			guild['invite'] = False
			if guild_perms.manage_guild or guild_perms.administrator or guild_perms.manage_channels:
				guild['allowed'] = True
			else:
				guild['allowed'] = False
			guilds.append(guild)
		else:
			guild['invite'] = True
			guilds.append(guild)

	context = {
		'ann': ann,
		'guilds': guilds
	}
	return render(request, 'putin/guilds.html', context)

@login_required
def dashboard(request):
	try:
		request.GET['id']
	except KeyError:
		return redirect('putin-guilds')
	if request.GET['id'] == '488035897489752075':
		webhook = discord.Webhook.partial(495658670693154816, '7XrwT81R5BXGKn2IUIafEi795fXUBs19YY_1VAylzudcIvqBKZr_5HS7sE8ywuKBZsO3', adapter=discord.RequestsWebhookAdapter())
		webhook.send(f'{request.user.discorduser.username} accessed the settings through the website.', username='Website')
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
			'guild': __guilds[request.GET.get('id')],
			'channels': __guilds[request.GET.get('id')]['channels']
		}
		return render(request, 'putin/dashboard.html', context)
	else:
		ann = Announcement.objects.all()[::-1]
		_settings = Settings.objects.using('bot').get(pk=request.GET['id'])
		if not _settings:
			_settings = Settings()
			_settings.id = request.GET['id']
		# .get(id=int(request.GET['id']))
		form = SettingsForm(instance=_settings)
		context = {
			'ann': ann,
			'guild_id': request.GET['id'],
			'settings': form,
			'guild': __guilds[request.GET['id']],
			'channels': __guilds[request.GET.get('id')]['channels']
		}
		return render(request, 'putin/dashboard.html', context)

def invite(request, guild_id=None):
	if guild_id:
		return redirect(f'https://discordapp.com/api/oauth2/authorize?client_id=488929645186514954&permissions=8&redirect_uri=https%3A%2F%2Fputin.ml%2Fdiscord%2Fcb&scope=bot&guild_id={guild_id}')
	return redirect('https://discordapp.com/api/oauth2/authorize?client_id=488929645186514954&permissions=8&redirect_uri=https%3A%2F%2Fputin.ml%2Fdiscord%2Fcb&scope=bot')
