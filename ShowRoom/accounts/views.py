from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect


# Create your views here.

def sign_up(request: HttpRequest):

    if request.method == "POST":
        try:
            new_user = User.objects.create_user(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                password = request.POST['password'],
                username = request.POST['username'],
            )
            new_user.save()
            messages.success(request, f'{new_user.username} Account was created Successfully', 'alert-success')
            return redirect('accounts:sign_in')
        except Exception as e:
            print(e)
            messages.error(request, 'error in creating your account ', 'alert-danger')
    return render(request, 'signup.html')


def sign_in(request: HttpRequest):

    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            messages.success(request, f'{user.username} Signed in Successfully', 'alert-success')
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, 'Username or password is wrong, please try again', 'alert-danger')
    return render(request, 'signin.html')

def log_out(request: HttpRequest):


    logout(request)
    messages.success(request, 'logged out successfully, See You later', 'alert-success')
    return redirect(request.GET.get('next', '/'))
