from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Category


def all_groseries(request):
    categories = Category.objects.all()
    return render(request,'groseries/groserieslist.html',{'categories':categories})

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'groseries/signupuser.html',{'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('groseriesapp:all_groseries')
            except IntegrityError:
                return render(request, 'groseries/signupuser.html',{'form': UserCreationForm(), 'error':'Ya existe un usuario con este nombre.'})
        else:
            return render(request, 'groseries/signupuser.html',{'form': UserCreationForm(), 'error':'Las contraseñas no coinciden'})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('groseriesapp:all_groseries')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'groseries/loginuser.html',{'form': AuthenticationForm()})
    else:
        user = authenticate(request,username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'groseries/loginuser.html',{'form': AuthenticationForm(),'error':'Nombre de usuario o contraseña incorrectos'})
        else:
            login(request, user)
            return redirect('groseriesapp:all_groseries')
