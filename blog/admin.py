from django.contrib import admin
from .models import Post, Announcement, Comment

admin.site.register(Post)
admin.site.register(Announcement)
admin.site.register(Comment)
