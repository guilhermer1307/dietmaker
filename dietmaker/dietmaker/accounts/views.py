from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from dietmaker.accounts.forms import SignUpForm


def dashboard(request):
	template_name = 'accounts/dashboard.html'
	return render(request, template_name)

def register(request):
	template_name = 'accounts/signup.html'
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(settings.LOGIN_URL)
	else:
		form = SignUpForm()
	context = {
		'form': form
	}
	return render(request, template_name, context)
