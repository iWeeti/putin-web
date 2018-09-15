from django import forms
from .models import Settings

class SettingsForm(forms.ModelForm):
	class Meta:
		model = Settings
		fields = ['leave', 'log_join', 'kick', 'ban']
