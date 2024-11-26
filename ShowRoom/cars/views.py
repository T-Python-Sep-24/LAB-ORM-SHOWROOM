from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Car,Color,Photo,Review
from brands.models import Brand
from .forms import ColorForm,CarForm
from django.contrib import messages
from django.core.paginator import Paginator
from accounts.models import Bookmark
# Create your views here.


def all_cars_view(request:HttpRequest):
    cars=Car.objects.all()
    brands=Brand.objects.all()
    colors=Color.objects.all()
    if "search" in request.GET and len(request.GET["search"]) >= 1:
        cars = cars.filter(name__icontains=request.GET["search"])

    if "filter_by_brand" in request.GET and request.GET["filter_by_brand"]:
        cars = cars.filter(brand__id=request.GET["filter_by_brand"])

    if "filter_by_color" in request.GET and request.GET["filter_by_color"]:
        cars = cars.filter(colors__id=request.GET["filter_by_color"]) 
    
    p=Paginator(cars,4)
    page=request.GET.get('page',1)
    cars_list=p.get_page(page)
    return render(request,'cars/all_cars.html',{"cars":cars_list,"colors":colors,"brands":brands})


def detail_car_view(request:HttpRequest,car_id):
    try: 

        car =Car.objects.get(pk=car_id)
        car_colors=car.colors.all()
        car_photos=car.photos.all()[1:] 
        reviews=Review.objects.filter(car=car)  
        is_bookmarked=  Bookmark.objects.filter(car=car, user=request.user).exists() if request.user.is_authenticated else False
        return render(request,'cars/detail_car.html',{"reviews":reviews,"car":car,"car_colors":car_colors,"car_photos":car_photos,"is_bookmarked":is_bookmarked})
    except Car.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found",'alert-danger')
        return redirect('main:home_view')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}",'alert-danger')
        return redirect('main:home_view')


def new_car_view(request:HttpRequest):
    if not request.user.is_superuser and not request.user.has_perm("cars.add_car"):
        messages.warning(request,"You don't have permission to add car","alert-warning")
        return redirect("main:home_view")
    brands=Brand.objects.all()
    colors=Color.objects.all()
    if request.method=="POST":
        car_form=CarForm(request.POST,request.FILES)
        if car_form.is_valid():
              car=car_form.save()
              if request.FILES.getlist('photos'):
                    photos = request.FILES.getlist('photos')
                    for photo in photos:
                        Photo.objects.create(car=car, image=photo) 
              messages.success(request, 'The car has been added successfully!','alert-success')
              return redirect("cars:new_car_view")
        else:
            print("form is not valid")
            print(car_form.errors)
    return render(request,'cars/new_car.html',{"brands":brands,"colors":colors,"FuelChoices":Car.FuelChoices.choices})

def update_car_view(request:HttpRequest,car_id):
    try:   
        if not request.user.is_superuser:
            messages.warning(request,"only staff can update car","alert-warning")
            return redirect("main:home_view")
 
        car =Car.objects.get(pk=car_id)
        brands=Brand.objects.all()
        colors=Color.objects.all()
        car_colors=car.colors.all()
        car_photos=car.photos.all()
        if request.method=="POST":
            print(request.POST.getlist('colors')) 
            car_form=CarForm(request.POST,request.FILES,instance=car)
            if request.POST.getlist('colors'): 
                    selected_colors = request.POST.getlist('colors') 
                    car.colors.set(selected_colors)


            if car_form.is_valid():
                car_form.save()
                if request.FILES.getlist('photos'):
                    car.photos.all().delete()#clear previose images
                    photos = request.FILES.getlist('photos')
                    for photo in photos:
                        Photo.objects.create(car=car, image=photo)  
                car.save()         
                messages.success(request, 'The car has been updated successfully!','alert-success')
                return redirect("cars:update_car_view",car_id=car.id)
            else:
                print("form is not valid")
                print(car_form.errors)
        else:   
            car_form = CarForm(instance=car)        
        return render(request,'cars/update_car.html',{"car":car,"car_colors":car_colors,"brands":brands,"colors":colors,"FuelChoices":Car.FuelChoices.choices,"car_photos":car_photos})
    except Car.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found",'alert-danger')
        return redirect('main:home_view')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('main:home_view')




def new_color_view(request:HttpRequest):
    if not request.user.is_superuser and not request.user.has_perm("cars.add_color"):
            messages.warning(request,"only staff can add color","alert-warning")
            return redirect("main:home_view")
 

    if request.method=="POST":
        color_form=ColorForm(request.POST,request.FILES)
        if color_form.is_valid():
              color_form.save()
              messages.success(request, 'The color has been added successfully!','alert-success')
              return redirect("cars:new_color_view")
        else:
            print("form is not valid")
            print(color_form.errors)
    return render(request,'cars/new_color.html')


def update_color_view(request:HttpRequest,color_id):
    try:
        if not request.user.is_superuser and not request.user.has_perm("cars.change_color"):
            messages.warning(request,"only staff can update color","alert-warning")
            return redirect("main:home_view")
 

        color=Color.objects.get(pk=color_id)
        if request.method=="POST":
            color_form=ColorForm(request.POST,request.FILES,instance=color)
            if color_form.is_valid():
                color_form.save()
                messages.success(request, 'The color has been updated successfully!','alert-success')
                return redirect('cars:update_color_view',color_id=color.id)
            else:
                print("form is not valid")
                print(color_form.errors)
                return redirect('main:home_view') 
        else:   
            color_form = ColorForm(instance=color)
        return render(request,'cars/update_color.html',{"color":color})                

    except Color.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found",'alert-danger')
        return redirect('main:home_view')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('main:home_view')



def search_color(request):
    if not request.user.is_superuser and not request.user.has_perm("cars.view_color"):
            messages.warning(request,"only staff can search color","alert-warning")
            return redirect("main:home_view")
 

    color_name = request.GET.get('color_name', '') 

    if color_name:
        try:
            color = Color.objects.get(name__iexact=color_name) 
            return redirect('cars:update_color_view', color_id=color.id) 
        except Color.DoesNotExist:
            messages.error(request, 'Color not found.','alert-danger')
            return redirect('main:home_view') 
    else:
        messages.error(request, 'Please enter a color name to search.','alert-danger')
        return redirect('main:home_view') 

def delete_car_view(request,car_id):
    try:
        if not request.user.is_superuser:
            messages.warning(request,"only staff can delete car","alert-warning")
            return redirect("main:home_view")

        car=Car.objects.get(pk=car_id)
        car.delete()
        messages.success(request, 'The car has been deleted successfully!','alert-success')
        return redirect("main:home_view")
    except Brand.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found",'alert-danger')
        return redirect('main:home_view')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}",'alert-danger')
        return redirect('main:home_view')

def delete_color_view(request,color_id):
    try:
        if not request.user.is_superuser:
            messages.warning(request,"only staff can delete color","alert-warning")
            return redirect("main:home_view")
 

        color=Color.objects.get(pk=color_id)
        color.delete()
        messages.success(request, 'The color has been deleted successfully!','alert-success')
        return redirect("main:home_view")
    except Brand.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found",'alert-danger')
        return redirect('main:home_view')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}",'alert-danger')
        return redirect('main:home_view')
    


def add_review_view(request:HttpRequest,car_id):
    if not request.user.is_authenticated:
        messages.error(request,"only registed user can add review",'alert-danger')
        return redirect("accounts:sign_in")
    if request.method=="POST":
        car_obj = Car.objects.get(pk=car_id)
        review=Review(user=request.user,comment=request.POST['comment'],rating=request.POST['rating'],car=car_obj)
        review.save()
        messages.success(request, "thank you for your review",'alert-success')
    return redirect("cars:detail_car_view",car_id=car_id)    




def delete_review_view(request:HttpRequest,review_id):
  
    try:
            review = Review.objects.get(pk=review_id)
            car_id=review.car.id
            if request.user != review.user and not (request.user.is_superuser and request.user.has_perm("cars.delete_review")):
                messages.error(request,"you don't have permisstion to delete a review",'alert-danger')
                return redirect("cars:detail_car_view",car_id=car_id)  
            else:    
                review.delete()
                messages.success(request, "review deleted successfully",'alert-success')
                return redirect("cars:detail_car_view",car_id=car_id)  
    except Exception as e:
        print(e)
        messages.error(request,"you don't have permisstion to delete a review",'alert-danger')


def add_bookmark_view(request,car_id):
    if not request.user.is_authenticated:
            messages.warning(request,"only rigisted user can add bookmarks","alert-warning")
            return redirect("accounts:sign_in")

    try:
       car=Car.objects.get(pk=car_id)
       bookmark =Bookmark.objects.filter(user=request.user,car=car).first()
       if not bookmark:
            new_bookmark= Bookmark(user=request.user,car=car)
            new_bookmark.save()
            messages.success(request, "added to bookmarks",'alert-success')
       else:
           bookmark.delete()
           messages.warning(request, "removed bookmark",'alert-warning')
     
    except Exception as e:
        print(e)


    return redirect("cars:detail_car_view",car_id=car_id)    