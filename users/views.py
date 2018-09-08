from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def reguster(request):
	form = UserCreationForm()
	return render(request, 'users/register.html')
