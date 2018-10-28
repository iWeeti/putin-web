from django import forms
from .models import Settings

class SettingsForm(forms.ModelForm):
	class Meta:
		model = Settings
		fields = [
			'leave',
			'kick',
			'ban',
			'unban',
			'message_delete',
			'message_edit',
			'log_commands',
			'advert',
			'buy_roles',
			'logging_channel',
			]
		labels = {
			'leave': 'Leave Logging',
			'kick': 'Kick Logging',
			'ban': 'Ban Logging',
			'unban': 'UnBan Logging',
			'message_delete': 'Message Delete Logging',
			'message_edit': 'Messsage Edit Logging',
			'buy_roles': 'Buyable roles from shop.',
			'log_commands': 'Log Command Uses',
			'logging_channel': 'Logging Channel',
			'advert': 'Anti Advertising'
		}
