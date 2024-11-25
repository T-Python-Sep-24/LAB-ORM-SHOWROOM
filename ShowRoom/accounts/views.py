from django.shortcuts import render,redirect

from django.http import HttpRequest , HttpResponse

from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout

from django.contrib import messages 
def sign_up_view(request : HttpRequest):
    if request.method == "POST": 
        new_user = User.objects.create_user(email=request.POST["email"],username=request.POST["username"],first_name=request.POST["first_name"], last_name=request.POST["last_name"],password=request.POST["password"])
        new_user.save()               
        messages.success(request, "Your account has been created successfully! Please log in.")
        return redirect("accounts:sign_in_view")
        
    return render(request , "accounts/sign_up.html")

def sign_in_view(request : HttpRequest):    
    if request.method == "POST": 
        user = authenticate (request,username= request.POST["username"],password= request.POST["password"])
        if user:
            login(request,user) 
            messages.success(request, f"Welcome back, {user.first_name}!")
            return redirect(request.GET.get("next","/"))
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    return render (request , "accounts/sign_in.html")

def logout_view(request : HttpRequest):
    logout(request)
    return redirect(request.GET.get("next","/"))