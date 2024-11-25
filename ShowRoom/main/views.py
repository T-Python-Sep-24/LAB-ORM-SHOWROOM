from cars.models import Car
from brands.models import Brand
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import logout
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('main:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'main/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})
def logout_user(request):
    logout(request)
    return redirect('main:home')
def home(request):
    latest_cars = Car.objects.all().order_by('-id')[:4]
    latest_brands = Brand.objects.all().order_by('-id')[:4]
    return render(request, 'main/home.html', {'latest_cars': latest_cars, 'latest_brands': latest_brands})
