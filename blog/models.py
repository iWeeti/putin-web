from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	edited = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	@property
	def long(self):
		return len(self.content) > 300

	@property
	def shortcontent(self):
		return self.content[0:300]

	def db_for_write(self, model, **hints):
		return 'default'

	def db_for_read(self, model, **hints):
		return 'default'

class Comment(models.Model):
	message = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	parent = models.ForeignKey(Post, on_delete=models.CASCADE)
	edited = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.parent.title}: {self.message}"

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.parent.pk})
	

class Announcement(models.Model):
	announcement = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.announcement

	def db_for_write(self, model, **hints):
		return 'default'

	def db_for_read(self, model, **hints):
		return 'default'
