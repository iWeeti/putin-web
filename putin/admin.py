from django.contrib import admin
from .models import (
	Settings,
	Profiles,
	Starboard
	)

admin.site.register(Settings)
admin.site.register(Profiles)
admin.site.register(Starboard)