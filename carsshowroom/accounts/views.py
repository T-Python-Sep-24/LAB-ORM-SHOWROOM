from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
# Create your views here.


def signup_view(request:HttpRequest):
    if request.method == 'POST':
        try:
            new_user=User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'],first_name=request.POST['first_name'],last_name=request.POST['first_name'])
            new_user.save()
            messages.success(request,"Account has been added successfully ","alert-success")
            return redirect ('accounts:signin_view')
        except Exception as e:
            messages.error(request,"field to add Account","alert-danger")
            print(e)
            
    return render(request,"accounts/signup.html")


def signin_view(request:HttpRequest):

    if request.method=="POST":
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user:
            login(request,user)
            messages.success(request,f"welcome {user.first_name}","alert-success")
            return redirect('main:home_view')
        else:
            messages.error(request,"field to login to your account","alert-danger")
    return render(request,"accounts/signin.html")

def log_out(request:HttpRequest):
    username=request.user.username
    logout(request)
    messages.success(request,f'See you soon {username}',"alert-dark")
    return redirect('main:home_view')
    


