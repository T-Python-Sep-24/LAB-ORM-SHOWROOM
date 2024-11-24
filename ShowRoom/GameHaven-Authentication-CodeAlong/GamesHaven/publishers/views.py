from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from games.models import Game

from .models import Publisher
from .forms import PublisherForm


# Create your views here.
def add_publisher(request:HttpRequest):

    if request.method == "POST":
        #addin a new game in database
        publisher_form = PublisherForm(request.POST, request.FILES)
        if publisher_form.is_valid():
            publisher_form.save()
        else:
            print(publisher_form.errors)

        return redirect("publishers:publishers_page")

    return render(request, "publishers/add_publisher.html")


def publishers_page(request:HttpRequest):

    publishers = Publisher.objects.all()[:8]

    return render(request, "publishers/publishers.html", {"publishers" : publishers})


def publisher_page(request:HttpRequest, publisher_id):

    publisher = Publisher.objects.get(id=publisher_id)
    #games_by_publisher = Game.objects.filter(publisher=publisher)

    #games = publisher.game_set.all()
    #print(games_by_publisher)
    #print(games)



    return render(request, "publishers/publisher_page.html", {"publisher" : publisher})
