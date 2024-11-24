from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def signup_view(request:HttpRequest):
    
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("accesses:signup_view")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use!")
            return redirect("accesses:signup_view")

        user = User.objects.create_user(username=username, email=email, password=password)

        user.save()

        messages.success(request, "Account created successfully! Please login.")

        return redirect("accesses:login_view")

    return render(request, 'accesses/signup.html')





def login_view(request:HttpRequest):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:

            login(request, user)

            messages.success(request, f"Welcome, {user.username}!")

            return redirect(request.GET.get("next", "/"))  
        
        else:

            messages.error(request, "Invalid username or password!")

            return redirect("accesses:login_view")

    return render(request, 'accesses/login.html')




def logout_view(request:HttpRequest):

    logout(request)

    messages.success(request, "You loggedout successfully!")

    return redirect(request.GET.get("next", "/"))

