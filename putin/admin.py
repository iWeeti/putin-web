from django.contrib import admin
from .models import (
	Settings,
	Profiles
	)

admin.site.register(Settings)
admin.site.register(Profiles)