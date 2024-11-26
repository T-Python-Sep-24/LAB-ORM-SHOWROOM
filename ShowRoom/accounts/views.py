from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError, transaction


from .models import Profile

# Create your views here.


def sign_up(request: HttpRequest):

    if request.method == "POST":

        try:
            with transaction.atomic():
                new_user = User.objects.create_user(username=request.POST["username"],password=request.POST["password"],email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"])
                new_user.save()

                profile=Profile(user=new_user,about=request.POST["about"],avatar=request.FILES.get("avatar",Profile.avatar.field.get_default()))
                profile.save()
                messages.success(request, "Registered User Successfuly", "alert-success")
                return redirect("accounts:sign_in")
        except Exception as e:
            messages.error(request, "Couldn't register user. Try again", "alert-danger")
            print(e)
    

    return render(request, "accounts/signup.html")



def sign_in(request:HttpRequest):

    if request.method == "POST":

        #checking user credentials
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        print(user)
        if user:
            #login the user
            login(request, user)
            messages.success(request, "Logged in successfully", "alert-success")
            return redirect(request.GET.get("next", "/"))
        else:
            messages.error(request, "Please try again. You credentials are wrong", "alert-danger")


    #
    return render(request, "accounts/signin.html")


def log_out(request: HttpRequest):

    logout(request)
    messages.success(request, "logged out successfully", "alert-warning")

    return redirect(request.GET.get("next", "/"))



def user_profile_view(request,user_name):
    try:
        user=User.objects.get(username=user_name)
        if not Profile.objects.filter(user=user).first():
            new_profile = Profile(user=user)
            new_profile.save()
        #profile=user.profile
       

    except:
        return render(request,"404.html")
    

    return render(request,"accounts/profile.html",{"user":user})


def update_profile_view(request):
        if not request.user.is_authenticated:
            messages.warning(request,"only rigisted user can update thier profile","alert-warning")
            return redirect("accounts:sign_in")
        if request.method =="POST":

                try:
                    with transaction.atomic():
                        user:User = request.user

                        user.first_name = request.POST["first_name"]
                        user.last_name = request.POST["last_name"]
                        user.email = request.POST["email"]
                        user.save()

                        profile:Profile = user.profile
                        profile.about = request.POST["about"]
                        if "avatar" in request.FILES: profile.avatar = request.FILES["avatar"]
                        profile.save()

                    messages.success(request, "updated profile successfuly", "alert-success")
                except Exception as e:
                    messages.error(request, "Couldn't update profile", "alert-danger")
                    print(e)

        return render(request,"accounts/update_profile.html")




