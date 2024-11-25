from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError, transaction
from .models import Profile

def sign_up(request: HttpRequest):

    if request.method == "POST":

        try:
            with transaction.atomic():
                new_user = User.objects.create_user(username=request.POST["username"],password=request.POST["password"],email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"])
                new_user.save()
                #create profile for user
                profile = Profile(user=new_user, about=request.POST["about"], twitch_link=request.POST["twitch_link"], avatar=request.FILES.get("avatar", Profile.avatar.field.get_default()))
                profile.save()

            messages.success(request, "Registered User Successfuly", "alert-success")
            return redirect("Users:sign_in")
        
        except IntegrityError as e:
            messages.error(request, "Please choose another username", "alert-danger")
        except Exception as e:
            messages.error(request, "Couldn't register user. Try again", "alert-danger")
            print(e)
    return render(request, "users/signup.html", {})



def sign_in(request:HttpRequest):

    if request.method == "POST":

        #checking user credentials
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        print(user)
        if user:
            #login the user
            login(request, user)
            messages.success(request, "Logged in successfully", "alert-success")
            return redirect(request.GET.get("main:index_view", "/"))
        else:
            messages.error(request, "Please try again. You credentials are wrong", "alert-danger")

    return render(request, "users/signin.html")


def log_out(request: HttpRequest):

    logout(request)
    messages.success(request, "logged out successfully", "alert-warning")
    return redirect(request.GET.get("next", "/"))


def user_profile_view(request:HttpRequest, user_name):

    try:
        user = User.objects.get(username=user_name)
        if not Profile.objects.filter(user=user).first():
            new_profile = Profile(user=user)
            new_profile.save()
        #profile:Profile = user.profile  
        #profile = Profile.objects.get(user=user)
    except Exception as e:
        print(e)
        return render(request,'main/404.html')
    

    return render(request, 'users/profile.html', {"user" : user})


def update_user_profile(request:HttpRequest):
    if not request.user.is_authenticated:
        messages.warning(request, "Only registered users can update their profile", "alert-warning")
        return redirect("Users:sign_in")
    if request.method == "POST":

        try:
            with transaction.atomic():
                user:User = request.user

                user.first_name = request.POST["first_name"]
                user.last_name = request.POST["last_name"]
                user.email = request.POST["email"]
                user.save()

                profile:Profile = user.profile
                profile.about = request.POST["about"]
                profile.twitch_link = request.POST["twitch_link"]
                if "avatar" in request.FILES: profile.avatar = request.FILES["avatar"]
                profile.save()

            messages.success(request, "updated profile successfuly", "alert-success")
        except Exception as e:
            messages.error(request, "Couldn't update profile", "alert-danger")
            print(e)

    return render(request, "users/update_profile.html")