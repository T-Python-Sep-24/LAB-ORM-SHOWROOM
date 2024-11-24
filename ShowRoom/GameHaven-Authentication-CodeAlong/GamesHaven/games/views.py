from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Game, Review, Category
from .forms import GameForm
from publishers.models import Publisher

from django.db.models import Q, F, Count, Avg, Sum, Max, Min
from django.core.paginator import Paginator

from django.contrib import messages

# Create your views here.

def create_game_view(request:HttpRequest):

    if not request.user.is_staff:
        messages.success(request, "only staff can add game", "alert-warning")
        return redirect("main:home_view")

    game_form = GameForm()


    categories = Category.objects.all()
    publishers = Publisher.objects.all()

    if request.method == "POST":
        
        game_form = GameForm(request.POST, request.FILES)
        if game_form.is_valid():
            game_form.save()
            messages.success(request, "Created Game Successfuly", "alert-success")
            return redirect('main:home_view')
        else:
            print("not valid form", game_form.errors)
        #publisher = Publisher.objects.get(id=request.POST["publisher"])
        # new_game = Game(title=request.POST["title"], description=request.POST["description"], publisher=publisher, rating=request.POST["rating"], release_date=request.POST["release_date"], poster=request.FILES["poster"])
        # new_game.save()
        # new_game.categories.set(request.POST.getlist("categories"))
        # return redirect('main:home_view')
    

    return render(request, "games/create.html", {"game_form":game_form,"RatingChoices": reversed(Game.RatingChoices.choices), "categories":categories, "publishers": publishers, "esrb_ratings" : Game.ESRBRating.choices})


def game_detail_view(request:HttpRequest, game_id:int):

    game = Game.objects.get(pk=game_id)



    avg = game.review_set.all().aggregate(Avg("rating"))
    print(avg)



    return render(request, 'games/game_detail.html', {"game" : game,  "average_rating":avg["rating__avg"]})


def game_update_view(request:HttpRequest, game_id:int):

    if not request.user.is_staff:
        messages.warning(request, "only staff can add game", "alert-warning")
        return redirect("main:home_view")
    
    game = Game.objects.get(pk=game_id)
    categories = Category.objects.all()
    publishers = Publisher.objects.all()

    if request.method == "POST":
        #using GameForm for updating
        game_form = GameForm(instance=game, data=request.POST, files=request.FILES)
        if game_form.is_valid():
            game_form.save()
        else:
            print(game_form.errors)
        ##basic update
        # game.title = request.POST["title"]
        # game.description = request.POST["description"]
        # game.release_date = request.POST["release_date"]
        # game.publisher = request.POST["publisher"]
        # game.rating = request.POST["rating"]
        # if "poster" in request.FILES: game.poster = request.FILES["poster"]
        # game.save()

        return redirect("games:game_detail_view", game_id=game.id)

    return render(request, "games/game_update.html", {"game":game, "categories" : categories, "publishers": publishers, "esrb_ratings" : Game.ESRBRating.choices})


def game_delete_view(request:HttpRequest, game_id:int):

    if not request.user.is_staff:
        messages.warning(request, "only staff can add game", "alert-warning")
        return redirect("main:home_view")
    
    try:
        game = Game.objects.get(pk=game_id)
        game.delete()
        messages.success(request, "Deleted game successfully", "alert-success")
    except Exception as e:
        print(e)
        messages.error(request, "Couldn't Delete game", "alert-danger")


    return redirect("main:home_view")


def all_games_view(request:HttpRequest, category_name):
    #games = Game.objects.filter(rating__gte=3).order_by("-release_date")
    #games = Game.objects.filter(rating__gte=3).exclude(title__contains="Legends").order_by("-release_date")
    
    # if  Category.objects.filter(name=category_name).exists():
    #     games = Game.objects.filter(categories__name__in=[category_name]).order_by("-release_date")
    # elif category_name == "all":
    #     games = Game.objects.all().order_by("-release_date")
    # else:
    #     games = []


    
    if category_name == "all":
        games = Game.objects.all().order_by("-release_date")
    else:
        games = Game.objects.filter(categories__name__in=[category_name]).order_by("-release_date")



    games = games.annotate(reviews_count=Count("review"))

    if "esrb" in request.GET:
        games = games.filter(esrb=request.GET["esrb"])



    page_number = request.GET.get("page", 1)
    paginator = Paginator(games, 3)
    games_page = paginator.get_page(page_number)



    


    return render(request, "games/all_games.html", {"games":games_page, "category_name":category_name, "esrb_ratings": Game.ESRBRating.choices})


def search_games_view(request:HttpRequest):

    if "search" in request.GET and len(request.GET["search"]) >= 3:
        games = Game.objects.filter(title__contains=request.GET["search"])

        if "order_by" in request.GET and request.GET["order_by"] == "rating":
            games = games.order_by("-rating")
        elif "order_by" in request.GET and request.GET["order_by"] == "release_date":
            games = games.order_by("-release_date")
    else:
        games = []


    return render(request, "games/search_games.html", {"games" : games})


def add_review_view(request:HttpRequest, game_id):
    if not request.user.is_authenticated:
        messages.error(request, "Only registered user can add review","alert-danger")
        return redirect("accounts:sign_in")

    if request.method == "POST":
        game_object = Game.objects.get(pk=game_id)
        new_review = Review(game=game_object,user=request.user,comment=request.POST["comment"],rating=request.POST["rating"])
        new_review.save()

        messages.success(request, "Added Review Successfully", "alert-success")

    return redirect("games:game_detail_view", game_id=game_id)