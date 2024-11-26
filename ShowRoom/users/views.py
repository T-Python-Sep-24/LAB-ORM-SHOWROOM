from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from users.models import Profile
# Create your views here.


def sign_up(request:HttpRequest):
   
    if request.method == "POST":
        try:
            new_user = User.objects.create_user(username=request.POST["username"],password=request.POST["password"],first_name=request.POST["first_name"],email=request.POST["email"])
            new_user.save()
            profile = Profile(user=new_user,about=request.POST["about"])
            profile.save()            
            messages.success(request,"Registered User Successfully","alert-success")
            return redirect("users:sign_in")
        except Exception as e:
            print(e)
    
    return render(request,"users/signup.html")


def sign_in(request:HttpRequest):

    if request.method == "POST":
        user = authenticate(request,username=request.POST["username"],password=request.POST["password"],)
        if user:
            login(request,user)
            messages.success(request,"logged in successfully","alert-success")
            return redirect("main:home_view")
        else:
            messages.error(request,"please try again","alert-danger")
    return render (request,"users/signin.html")

def log_out(request:HttpRequest):
    logout(request)
    return redirect("main:home_view")



def user_profile_view(request:HttpRequest,user_name):
    user = User.objects.get(username=user_name)
    profile:Profile = user.profile
   # profile = Profile.objects.get(user=user)
    return render(request,'users/profile.html',{"user":user})

