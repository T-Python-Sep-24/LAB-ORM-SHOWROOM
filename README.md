# LAB-ORM-SHOWROOM

## Using what you learned, create a new project called `ShowRoom`
This is a website for showing brands of cars, cars and details about cars. Essentially a Show Room for cars !

### Required models
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
