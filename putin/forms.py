from django import forms
from .models import Settings

class SettingsForm(forms.ModelForm):
	class Meta:
		model = Settings
		fields = ['leave', 'kick', 'ban', 'unban', 'welcome_enabled', 'advert', 'message_delete', 'message_edit', 'buy_roles', 'log_commands', 'logging_channel']
