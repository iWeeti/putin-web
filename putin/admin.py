from django.contrib import admin
from .models import (
	Settings,
	Profiles,
	Starboard
	)

@admin.register(Profiles)
class ProfilesAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'description'
		)
	list_display_links = ('id',)