from django.shortcuts import render , redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def register(request: HttpRequest):
    if request.method == "POST":
        try:
          
            new_user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password"],
                email=request.POST["email"],
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"]
            )
            new_user.save() 
            
            messages.success(request, "Registered User Successfully")
            return redirect("accounts/login.html")  
        except Exception as e:
          
            print(e)
            messages.error(request, "An error occurred during registration. Please try again.") 
            return render(request, "accounts/register.html")  

   
    return render(request, "accounts/register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("/")  
        else:
            messages.error(request, "Invalid username or password.")  
        
    return render(request, "accounts/login.html")



'''class LogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have successfully logged out.")
        return redirect("/") '''

def log_out(request: HttpRequest):

    logout(request)
    messages.success(request, "You have successfully logged out.")

    return redirect(request.GET.get("next", "/"))        