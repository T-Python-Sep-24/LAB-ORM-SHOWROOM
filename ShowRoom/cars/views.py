from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from cars.models import Car, Attachment, Color, Comment
from cars.forms import CarForm, ColorForm
from brands.models import Brand
from django.core.paginator import Paginator
from django.db.models import Count
from accounts.models import Bookmark

# Add color View
def addColorView(request:HttpRequest):
    if not (request.user.is_staff and request.user.has_perm('cars.add_color')):
        messages.warning(request, "Only editors can add colors.", "alert-warning")
        response = redirect('main:homeView')
    else:
        colorData = ColorForm()
        response = render(request, 'colors/addColor.html')
        if request.method == "POST":
            colorData = ColorForm(request.POST, request.FILES)
            if colorData.is_valid():
                colorData.save()
                messages.success(request, f"Color '{request.POST['name']}' was added successfully.", "alert-success")
            else:
                messages.error(request, f"Color '{request.POST['name']}' wasn't added.", "alert-danger")
                
            response = redirect('main:homeView')

    return response

# Update color View
def updateColorView(request:HttpRequest, clrId:int):
    
    if not (request.user.is_staff and request.user.has_perm('cars.change_color')):
        messages.warning(request, "Only editors can update colors.", "alert-warning")
        response = redirect('main:homeView')
    else:
        try:
            color = Color.objects.get(pk=clrId)
        except Exception:
            response = render(request, '404.html')
        else:
            response = render(request, 'colors/updateColor.html', context={'color': color})
            if request.method == "POST":
                colorData = ColorForm(request.POST, request.FILES, instance=color)
                if colorData.is_valid():
                    colorData.save()
                    messages.success(request, f"Color '{request.POST['name']}' was updated successfully.", "alert-success")
                else:
                    messages.error(request, f"Color '{request.POST['name']}' wasn't updated.", "alert-danger")
                    
                response = redirect('main:homeView')

    return response

# Delete color View
def deleteColorView(request: HttpRequest, clrId:int):

    if not (request.user.is_staff and request.user.has_perm('cars.delete_color')):
        messages.warning(request, "Only editors can delete colors.", "alert-warning")
        response = redirect('main:homeView')
    else:
        try:
            color = Color.objects.get(pk=clrId)
        except Exception:
            response = render(request, '404.html')
        else:
            try:
                color.delete()
            except Exception:
                messages.error(request, f"'{color.name}' wasn't deleted.", "alert-danger")
            else: 
                messages.success(request, f"'{color.name}' deleted successfully.", "alert-success")    
            
            response = redirect('main:homeView')

    return response

# Display all colors View
def allColorsView(request:HttpRequest):
    
    if not (request.user.is_staff and request.user.has_perm('cars.view_color')):
        messages.warning(request, "Only editors can view registered colors.", "alert-warning")
        response = redirect('main:homeView')
    else:
        colors = Color.objects.all()
        response = render(request, 'colors/allColors.html', {'colors': colors})
    
    return response

# Add car View
def addCarView(request: HttpRequest):

    if not (request.user.is_staff and request.user.has_perm('cars.add_car')):
        messages.warning(request, "Only editors can add cars.", "alert-warning")
        response = redirect('main:homeView')
    else:
        carData = CarForm()
        colors = Color.objects.all()
        brands = Brand.objects.all()
        response = render(request, 'cars/addCar.html', context={'brands': brands, 'colors': colors, 'gearTypes': Car.Gear.choices, 'fuelTypes': Car.Fuel.choices, 'bodyTypes': Car.BodyType.choices})
        
        if request.method == "POST":
            carData = CarForm(request.POST)
            images = request.FILES.getlist('images')
            if carData.is_valid():
                car:Car = carData.save(commit=False)
                car.save()
                car.colors.set(request.POST.getlist("colors"))
                for img in images:
                    Attachment.objects.create(car=car, image=img)
                messages.success(request, f"'{request.POST['model']}' was added successfully.", "alert-success")
            else:
                messages.error(request, f"'{request.POST['model']}' wasn't added.", "alert-danger")
                
            response = redirect('cars:displayCarsView', 'all')
    
    return response

# Update car View
def updateCarView(request: HttpRequest, carId:int):

    if not (request.user.is_staff and request.user.has_perm('cars.change_car')):
        messages.warning(request, "Only editors can update cars.", "alert-warning")
        response = redirect('main:homeView')
    else:
        try:
            car = Car.objects.get(pk=carId)
        except Exception:
            response = render(request, '404.html')
        else:
            colors = Color.objects.all()
            brands = Brand.objects.all()
            carImages = Attachment.objects.filter(car=car)
            response = render(request, 'cars/updateCar.html', context={'car': car, 'carImgs': carImages, 'brands': brands, 'colors': colors, 'gearTypes': Car.Gear.choices, 'fuelTypes': Car.Fuel.choices, 'bodyTypes': Car.BodyType.choices})
            
            if request.method == "POST":
                carData = CarForm(request.POST, instance=car)
                images = request.FILES.getlist('images')
                if carData.is_valid():
                    car:Car = carData.save(commit=False)
                    car.save()
                    car.colors.set(request.POST.getlist("colors"))
                    if images:
                        Attachment.objects.filter(car=car).delete()
                        for img in images:
                            Attachment.objects.create(car=car, image=img)
                    
                    messages.success(request, f"'{request.POST['model']}' was updated successfully.", "alert-success")
                else:
                    messages.error(request, f"'{request.POST['model']}' wasn't updated.", "alert-danger")
                    
                response = redirect('cars:carDetailsView', carId)

    return response

# Delete car View
def deleteCarView(request: HttpRequest, carId:int):

    if not (request.user.is_staff and request.user.has_perm('cars.delete_car')):
        messages.warning(request, "Only editors can delete cars.", "alert-warning")
        response = redirect('main:homeView')
    else:
        try:
            car = Car.objects.get(pk=carId)
        except Exception:
            response = render(request, '404.html')
        else:
            try:
                car.delete()
            except Exception:
                messages.error(request, f"'{car.name}' wasn't deleted.", "alert-danger")
            else: 
                messages.success(request, f"'{car.name}' deleted successfully.", "alert-success")    
            
            response = redirect('cars:displayCarsView', 'all')

    return response

# Diplay cars View
def displayCarsView(request: HttpRequest, filter: str):

    bodyTypes = Car.BodyType.choices
    colors = Color.objects.all()
    brands = Brand.objects.all()

    if filter == 'all':
        cars = Car.objects.all().order_by('-addedAt')
    else:
        cars = Car.objects.filter(bodyType__iexact=filter).order_by('-addedAt')
    
    if 'search' in request.GET and len(request.GET['search']) >= 2:
        cars = cars.filter(model__contains=request.GET['search']).order_by('-addedAt')

    if 'colors' in request.GET:
        cars = cars.filter(colors__name__in=request.GET.getlist('colors')).order_by('-addedAt')

    if 'brand' in request.GET and request.GET['brand'] != '':
        cars = cars.filter(brand__name=request.GET['brand'])

    cars = cars.annotate(Count("id"))

    paginator = Paginator(cars, 4)
    pageNumber = request.GET.get('page', 1)
    page_obj = paginator.get_page(pageNumber)

    response = render(request, 'cars/displayCars.html', context={'cars': page_obj, 'selected': filter, 'bodyTypes': bodyTypes, 'colors': colors, 'brands': brands, "filteredColors":request.GET.getlist("colors")})
    
    return response

# Car details View
def carDetailsView(request: HttpRequest, carId:int):
    try:
        car = Car.objects.get(pk=carId)
    except Exception:
        response = render(request, '404.html')
    else:

        relatedCars = Car.objects.exclude(pk=carId).filter(brand=car.brand)[0:3]
        comments = Comment.objects.filter(car=car)
        isBookmarked = Bookmark.objects.filter(car=car, user=request.user).exists() if request.user.is_authenticated else False

        response = render(request, 'cars/carDetails.html', context={'car': car, 'relatedCars': relatedCars, 'comments': comments, 'isBookmarked': isBookmarked})
    return response

# Add comment View
def addCommentView(request: HttpRequest, carId: int):

    if not request.user.is_authenticated:
        messages.error(request, "Only registered users can add comments.", "alert-danger")
        response = redirect('accounts:loginView')
    else:
        if request.method == 'POST':
            car = Car.objects.get(pk=carId)
            newComment = Comment(car=car, user=request.user , comment=request.POST['comment'])
            newComment.save()
            messages.success(request, "Your comment was added successfully.", "alert-success") 

    response = redirect('cars:carDetailsView', carId)
    return response

# Delete comment View
def deleteCommentView(request: HttpRequest, commentId:int):

    try:
        comment = Comment.objects.get(pk=commentId)
    except Exception:
        response = render(request, '404.html')
    else:
        try:
            carId = comment.car.id
            if (request.user.is_staff and request.user.has_perm('cars.delete_comment')) or comment.user == request.user:
                comment.delete()
            else:
                messages.warning(request, "You can't delete this comment.", "alert-warning")

        except Exception:
            messages.error(request, "Something went wrong. Comment wasn't deleted.", "alert-danger")
        else: 
            messages.success(request, "Comment deleted successfully.", "alert-success")    
        
        response = redirect('cars:carDetailsView', carId)

    return response

# Add bookmark View
def addBookmarkView(request:HttpRequest, carId:id):
    
    if not request.user.is_authenticated:
        messages.error(request, "Only registered users can add bookmarks.", "alert-danger")
        return redirect('cars:carDetailsView', carId)
    try:
        car = Car.objects.get(pk=carId)
        
        bookmark = Bookmark.objects.filter(user=request.user, car=car).first()
        if not bookmark:
            newBookmark = Bookmark(user=request.user, car=car)
            newBookmark.save()
            messages.success(request, "Bookmark added successfully.", "alert-success")
        else:
            bookmark.delete()
            messages.warning(request, "Bookmark removed successfully.", "alert-warning")

    except Exception as e:
        messages.error(request, "Something went wrong. Couldn't add bookmark.", "alert-danger")

    return redirect('cars:carDetailsView', carId)

