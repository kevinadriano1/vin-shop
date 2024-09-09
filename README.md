# vin-shop
## Link : http://kevin-adriano-vinshop.pbp.cs.ui.ac.id/

### 1. Create a new Django project:

Use django-admin startproject vin_shop . to create a new project. This command sets up the essential files for a Django project, including settings.py and urls.py.

### 2. Create an application named "main":

create a new application called main inside the project file project by running python manage.py startapp main
views.py, models.py, and urls.py will be added for handling the logic of the app.

### 3. Perform routing for the "main" app:

you need to open the urls.py file inside of the vin_shop project directory and add:

```
urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
]
```

### 4. Create a Product model in models.py:

Define the models in main/models.py
create class Product and add
name as Charfield with 100 character max
price as IntegerField 
description as TextField
rating as DecimalField

```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name
```
Run python manage.py makemigrations and python manage.py migrate to apply the database changes.

### 5. make the html file
create a file name templates  in your main directory and make a html file named main.html
in the main.html input this

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>main</title>
</head>
<body>
    <h1>{{ app_name }}</h1>
    <p>Name: {{ name }}</p>
    <p>npm: {{ npm }}</p>
    <p>Class: {{ class }}</p>
</body>
</html>
```

### 6. Create a function in views.py:
In views.py, add:

```
from django.shortcuts import render
# Create your views here.

def show_main(request):
    context = {
        'app_name' : 'vin-shop',
        'name': 'Kevin Adriano',
        'npm': '2306172552',
        'class': 'PBP KKI',
    }

    return render(request, "main.html", context)
```

views.py acts as the middleman between the Model and the Template. The View doesn’t directly render HTML; instead, it hands off the data and the template to Django’s template engine, which then generates the final HTML.

### 7. Create routing for the about view:

Create a urls.py file in the main directory and add:

```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

### 8. Perform deployment to PWS


1. Access the PWS page
2. Login into your account
3. Create a new project
4. Store your credentials for the project somewhere safe
5. add the PWS deployment URL to the allowed host
```

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "<Your PWS deployment URL>"]

```

Run the project command instruction that is in the PWS project page.


## 2. The Diagram

![](image/diagram.png)

urls.py: urls.py directs the incoming request to a specific function in views.py based on the URL pattern. For example, if a user visits /products/, urls.py may route this to a product_list function in views.py.
views.py: A view function may interact with the database by querying or updating data using the models defined in models.py
fter processing data, the view function passes this data to an HTML template, which renders the data into a user-friendly format.
models.py: The view interacts with models to retrieve or update data in the database. For example, a view can use a model to get a list of all products or to save a new product to the database.
HTML File (Template): The final output rendered by the view, which is sent to the client as part of the HTTP response. It displays the data in a user-friendly format.


## 3. Use of Git
1: git allows developers to keep history of changes
2: git makes collab easier by enables multiple developers to collab in different branch and merging them
3: git history can be used to recover lost data
4: git allows for a structured code review process, other member can add comment on specific lines of code
5: developers can use branches to experiment new things

## 4. Reason to use Django
Django is a high level framework that simplifies complexity, allows beginner to build fully fucntional web without having to integrate many third party libraries, has comprehensive and well-organized documentation, django has a large and active community so that new developers can easily find tutorials in social media

## 5. What is ORM?
Django allows you to define your database schema using Python classes,ORM handles the translation between the object-oriented data model used in your application and the relational data model used in the database, When you create an instance of a model and save it, the ORM translates this operation into SQL commands that interact with the database, you can interact with the database using Python code rather than writing raw SQL queries