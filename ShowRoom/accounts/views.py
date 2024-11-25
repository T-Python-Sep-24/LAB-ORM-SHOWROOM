from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile

# Create new account View
def registerView(request:HttpRequest):
 
    if request.method == "POST":
        try:
            newUser = User.objects.create_user(first_name=request.POST['fname'], last_name=request.POST['lname'], username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
            newUser.save()

            # Create profile
            profile = Profile(user=newUser, about=request.POST['about'], avatar=request.FILES.get('avatar', Profile.avatar.field.get_default()))
            profile.save()

            messages.success(request, "Register successfull.", "alert-success")   
            return redirect('accounts:loginView') 
        
        except Exception:
            messages.error(request, f"Register failed. Try again", "alert-danger")    

    return render(request, 'accounts/register.html')

# Login to existing account View
def loginView(request:HttpRequest):

    if request.method == 'POST':
        # Check user credentials
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user:
            login(request, user)
            messages.success(request, f"Welcome back {user.first_name}, your login was successfull.", "alert-success")
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, f"Login failed. Your credentials are incorrect.", "alert-danger")   
    
    return render(request, 'accounts/login.html')

# Logout View
def logoutView(request:HttpRequest):
    
    logout(request)
    messages.success(request, "Logged out successfully.", "alert-success")
    return redirect(request.GET.get('next', '/'))
    

def profileView(request: HttpRequest, username: str):
    try:
        user = User.objects.get(username=username)
        if Profile.objects.filter(user=user).first():
            profile: Profile = user.profile
        else:
            profile = Profile(user=user)
    except Exception:
        return render(request, '404.html')
    
    return render(request, 'accounts/profile.html', {'profile': profile})
