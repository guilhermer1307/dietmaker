from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
	return render(request, 'main.html')

def alunos(request):
	return render(request, 'main.html')

def professor(request):
	return render(request, 'main.html')

def alimentos(request):
	return render(request, 'main.html')

