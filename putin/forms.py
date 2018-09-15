from django import forms
from .models import Settngs

class SettingsForm(forms.ModelForm):
	class Meta:
		model = Settings
		fields = ['kick']
