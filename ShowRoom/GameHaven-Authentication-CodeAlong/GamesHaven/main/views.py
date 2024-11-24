from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from games.models import Game
from django.db.models import Count
from .models import Contact
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages

# Create your views here.

def home_view(request:HttpRequest):

    if request.user.is_authenticated:
        print(request.user.email)
    else:
        print("User is not logged in")

    #get all games
    games = Game.objects.all().order_by("-release_date").annotate(reviews_count=Count("review"))[0:3]

    return render(request, 'main/index.html', {"games" : games} )


def contact_view(request:HttpRequest):
    
    if request.method == "POST":
        contact = Contact(name=request.POST["name"], email=request.POST["email"], message=request.POST["message"])
        contact.save()

        #send confirmation email
        content_html = render_to_string("main/mail/confirmation.html")
        send_to = contact.email
        email_message = EmailMessage("confiramation", content_html, settings.EMAIL_HOST_USER, [send_to])
        email_message.content_subtype = "html"
        #email_message.connection = email_message.get_connection(True)
        email_message.send()

        messages.success(request, "Your message is received. Thank You.", "alert-success")

    return render(request, 'main/contact.html' )


def contact_messages_view(request:HttpRequest):
    
    contact_messages = Contact.objects.all().order_by("-created_at")

    return render(request, 'main/contact_messages.html', {"contact_messages" : contact_messages} )



def mode_view(request:HttpRequest, mode):

    response = redirect(request.GET.get("next", "/"))

    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")


    return response



def test_params_view(request:HttpRequest, param1, param2):

    print(param1, param2)

    if "query_param1" in request.GET:
        query_param1 = request.GET["query_param1"]
        print("Query Parameter 1", query_param1)

    return render(request, "main/test_params.html", {"param1" : param1})