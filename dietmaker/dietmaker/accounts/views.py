from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from dietmaker.accounts.models import *

def getuserid(request):
	user = request.user
	print(user)
	return user

def dashboard(request):
	template_name = 'accounts/dashboard.html'
	return render(request, template_name)

def register(request):
	template_name = 'accounts/signup.html'
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(settings.LOGIN_URL)
	else:
		form = UserCreationForm()
	context = {
		'form': form
	}
	return render(request, template_name, context)

def create_diet(request):
	if request.method == "POST":
		name    = request.POST['dietname']
		user_id = request.POST['user_id']

		Diets.objects.create(
			name = name,
			user = user_id
			)
		return redirect("/")
	else:
		return redirect("/")

def create_food(request):
	if request.method == "POST":
		name  = request.POST['name']
		carbo = request.POST['carbo']
		prot  = request.POST['prot']
		fat   = request.POST['fat']
		
		Foods.objects.create(
			name  = name,
	    	carbo = carbo,
	    	prot  = prot,
	    	fat   = fat
	    	)
		return redirect("/")
	else:
		return redirect("/")

def rel(request):
	if request.method == "POST":
		food_id = request.POST['food_id']
		diet_id = request.POST['diet_id']

		Diet_foods.objects.create(
			food = food_id,
			diet = diet_id
			)
		return redirect("/")
	else:
		return redirect("/")

