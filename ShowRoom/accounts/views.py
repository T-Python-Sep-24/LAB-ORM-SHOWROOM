from django.shortcuts import render , redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate , login
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def register(request: HttpRequest):

    if request.method == "POST":

        try:
            new_user = User.objects.create_user(username=request.POST["username"],password=request.POST["password"],email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"])
            new_user.save()
            messages.success(request, "Registered User Successfuly")
            return redirect("/")
        except Exception as e:
            print(e)
            return render(request, "accounts/register.html")

         
class LogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have successfully logged out.")
        return super().dispatch(request, *args, **kwargs)