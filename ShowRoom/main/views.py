from django.shortcuts import render , redirect
from cars.models import Car
from brands.models import Brand
from django.contrib.auth import login, authenticate , logout
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.

def home(request):
    latest_cars = Car.objects.all().order_by('-created_at')[:4]
    latest_brands = Brand.objects.all().order_by('-id')[:4]

    return render(request, 'main/home.html', {
        'latest_cars': latest_cars,
        'latest_brands': latest_brands
    })

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('main:login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have logged in successfully!")
                return redirect('main:home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('main:home')