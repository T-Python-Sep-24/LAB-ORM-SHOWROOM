from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create new account View
def registerView(request:HttpRequest):

    response = render(request, 'accounts/register.html')
    if request.method == "POST":
        try:
            newUser = User.objects.create_user(first_name=request.POST['fname'], last_name=request.POST['lname'], username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
            newUser.save()
            messages.success(request, "Register successfull.", "alert-success")   
            response = redirect('accounts:loginView') 
        except Exception as e:
            messages.error(request, f"Register failed. {e}", "alert-danger")    

    return response

# Login to existing account View
def loginView(request:HttpRequest):
    response = render(request, 'accounts/login.html')
    if request.method == 'POST':
        # Check user credentials
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user:
            login(request, user)
            messages.success(request, f"Welcome back {user.name}, your login was successfull.", "alert-success")
            response = redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, f"Login failed. Your credentials are incorrect.", "alert-danger")   
    
    return response

# Logout View
def logoutView(request:HttpRequest):
    
    logout(request)
    messages.success(request, "Logged out successfully.", "alert-success")
    response = redirect(request.GET.get('next', '/'))
    
    return response
