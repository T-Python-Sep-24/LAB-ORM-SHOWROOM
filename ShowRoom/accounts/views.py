from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.



def sign_up(request: HttpRequest):

    if request.method == "POST":

        try:
            new_user = User.objects.create_user(username=request.POST["username"],password=request.POST["password"],email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"])
            new_user.save()
            messages.success(request, "Registered User Successfuly")
            return redirect("accounts:sign_in")
        except Exception as e:
            print(e)
    

    return render(request, "sign_up.html", {})



def sign_in(request:HttpRequest):

    if request.method == "POST":

        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        print(user)
        if user:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect(request.GET.get("next", "/"))
        else:
            messages.error(request, "Please try again. You credentials are wrong")



    return render(request, "sign_in.html")


def log_out(request: HttpRequest):

    logout(request)
    messages.success(request, "logged out successfully")

    return redirect(request.GET.get("next", "/"))