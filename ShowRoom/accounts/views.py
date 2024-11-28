from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def sign_up(request: HttpRequest):

    return render(request, "accounts/signup.html")



def sign_in(request: HttpRequest):

    return render(request, "accounts/signin.html")



def log_out(request: HttpRequest):

    return redirect("main:home_view")