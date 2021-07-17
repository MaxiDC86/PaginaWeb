from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm


from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm


def home(request):

    return render(request,"PaginaWebApp/home.html" )

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('Home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'La cuenta fue creada para ' + user)

				return redirect('Login')
			

		context = {'form':form}
		return render(request, 'PaginaWebApp/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('Home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('Home')
			else:
				messages.info(request, 'El usuario o contraseña es incorrecta ')

		context = {}
		return render(request, 'PaginaWebApp/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('Home')

