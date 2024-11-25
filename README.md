# LAB-ORM-SHOWROOM

![image](https://github.com/user-attachments/assets/95450e94-dfb6-429f-8889-f932a1d012be)

![image](https://github.com/user-attachments/assets/61d9caf2-d442-4495-a388-1bd225fd2bc3)

![image](https://github.com/user-attachments/assets/396ea60f-dba1-4eb5-920a-8a7ad9192e20)

![image](https://github.com/user-attachments/assets/b8ef1a39-8275-4117-bbb0-c8cf246b56b5)

![image](https://github.com/user-attachments/assets/7590ec8e-d1c2-4d85-92a6-ddc563add8b5)

![image](https://github.com/user-attachments/assets/0a7edddb-3f07-4239-992d-120eb13afe38)

![image](https://github.com/user-attachments/assets/8a41d667-2b2e-4399-9452-43a011db9f6e)

![image](https://github.com/user-attachments/assets/82dfc0f2-3136-43d9-b5b2-b7d83e39b8e3)

![image](https://github.com/user-attachments/assets/a583c3e1-886b-4551-8201-4bb715cf2690)


## Using what you learned, create a new project called `ShowRoom`
This is a website for showing brands of cars, cars and details about cars. Essentially a Show Room for cars !

### Models
#### `Brand`
- this is a model for the brands of cars. ex: Chevrolet, Toytoa, Ford, Tesla, etc.
- It should at leas have the following attributes: name, logo, about, founded_at, ..... etc. You can add more.

#### `Color`
- This is a model to represent colors of cars.
- It should at least have the following attributes: name, photo or rgb or hexadeicml color, ..... etc. You can add more.

#### `Car`
- This is a model to represent cars, ex: Camry, Caprice, Model 3, etc.
- It should at least have the following attributes: name, brand, colors,  photo, specs, model, ..... etc. You can add more.
Note: car model has a relation with `Car` model and `Color` model (use appropriate relation types for each)


### Pages
- Home page `/`: this page shows the latest cars (limit to 4 with a link to go to all cars) , lates brands.
- All Cars page `cars/all/`: this page shows all the cars (with pagination, max. 10 cars per page). It also has filters to filter by Brand and by Color, with search by name.
- Car Detail page `cars/details/<card_id>/`: this page shows details of a car : name, photo, brand, available colors, specs, etc.
- New car page: `cars/new/` : to add new car.
- update car page: `cars/update/<car_id>/`: to update a car.
- All Brands page: `brands/all/`: this page shows all the brands, with search by name. In the brand card, beside the name and logo , it should show how many cars each brand has.
- Brand details page `brands/details/<brand_id>/` : this page shows the brand details: logo, name, about, etc. And cars in this brand.
- New brand page `brands/new/`: to add new brand.
- Update brand page `brands/update/<brand_id>/`: to update a brand.
- Add new Color page `cars/colors/new/` : to add a new color.
- Update color page `cars/colors/update/<color_id>/`: to update a color.
- For each model, implement delete.
- Use Django messages to give feedback to user (in creation, update, delete)
- At least you should have 3 apps: main, cars, brands.
