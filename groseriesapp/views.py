from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Category, Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

@login_required
def all_groseries(request):
    products = Product.objects.all()
    shopping_list =  {}
    for product in products:
        if product.category not in shopping_list:
            shopping_list[product.category] = []
        shopping_list[product.category].append(product)
    return render(request,'groseries/groserieslist.html',{'shopping_list':shopping_list,'form':ProductForm()})

@login_required
def addProduct(request):
    if request.method == 'GET':
        return render(request,'groseries/newproduct.html',{'form':ProductForm()})
    else:
        form = ProductForm(request.POST)
        newProduct = form.save(commit=False)
        newProduct.user = request.user
        newProduct.save()
        return redirect('groseriesapp:all_groseries')

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

