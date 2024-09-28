# vin-shop
## Link : http://kevin-adriano-vinshop.pbp.cs.ui.ac.id/login/?next=/

## assignment 2

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

![](image/diagram.jpg)

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

## assignment 3

### 1. why we need data delivery in implementing a platform
Data delivery plays a vital role in platform implementation by facilitating smooth communication between system components and users. It powers essential functions such as real-time interactions, data processing, and user engagement. Effective data delivery improves user experience, maintains data integrity and security, enables scalability, and ensures compliance with industry regulations.

### 2. which is better, XML or JSON? Why is JSON more popular than XML?
JSON because it is simpler, more lightweight, and easier to work with, it is more popular because JSON (JavaScript Object Notation) has a straightforward structure that's easy to read and write, using key-value pairs and arrays, JSON has less syntactical overhead than XML, JSON is native to JavaScript, JSON is more human-readable and easier to understand

### 3. functional usage of is_valid() method in Django forms. Also explain why we need the method in forms.
The is_valid() method in Django forms is used to validate form data and check whether the form's input conforms to the specified rules.
It centralizes the validation logic within the form, enabling Django to automatically verify that the data adheres to the criteria specified for each field. This prevents the processing of invalid or malicious data, ensuring that only clean, valid information is saved to the database or utilized in operations. Using is_valid() simplifies the workflow by checking for validity, processing valid data, or displaying errors if the data is invalid.

### 4.Why do we need csrf_token when creating a form in Django? What could happen if we did not use csrf_token on a Django form? How could this be leveraged by an attacker?
The csrf_token is a unique, secret token included in forms that are submitted to a Django view. It serves as a security mechanism to ensure that the form submission is coming from the legitimate user and not from an unauthorized third party. If the csrf_token is not included in a form, Django's CSRF protection won't be active, leaving the application vulnerable to CSRF attacks. An attacker could craft a malicious form on another website that submits a request to the Django application (e.g., transferring funds, changing account details) using the victim’s browser session.

### 5. Create a form input to add a model object
you need create forms.py in the main directiory add the following code:
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "rating"]
```

update views.py

```
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```

create create_product_entry.html

```
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```

### 6. Add 4 views to view the added objects in XML, JSON, XML by ID, and JSON by ID formats.

add the following code in views.py 

XML
```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

JSON
```
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

XML by id
```
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

JSON by id
```
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

### 7. Create URL routing for each of the views added in point 2
import and add the url path in the urls.py in the main directory

```
from django.urls import path
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```

### 8. screenshots
XML and XML by id
![](image/localhost_xml.png)
![](image/localhost_xml_id.png)

JSON and JSON by id
![](image/localhost_json.png)
![](image/localhost_json_id.png)

## assignment 4

### difference between HttpResponseRedirect() and redirect()
HttpResponseRedirect requires a direct URL as an argument and manually sets the redirect location in the HTTP response. It's straightforward but less versatile. redirect() is a shortcut that offers more flexibility. It can accept a URL, view name, or model instance, automatically resolving to the appropriate redirect destination. Additionally, redirect() allows you to perform permanent redirects by setting a parameter, making it more convenient for various scenarios.

### how the MoodEntry model is linked with User
add this in your models.py
```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
The line user = models.ForeignKey(User, on_delete=models.CASCADE) in Django creates a foreign key relationship between the model and the User model, ensuring that when a user is deleted, all related records in the model are also deleted.

add this in your create_product_entry:
```
mood_entry = form.save(commit=False)
mood_entry.user = request.user
mood_entry.save()
return redirect('main:show_main')
```

### difference between authentication and authorization, and what happens when a user logs in? Explain how Django implements these two concepts.
Authentication: This is the process of verifying a user's identity, typically by checking credentials like a username and password.
Authorization: This process occurs after authentication and determines what actions or resources the authenticated user is allowed to access.
When a user provides their credentials (e.g., username and password), Django checks them against its database of registered users to verify the user's identity. If the credentials are correct, Django creates a session, which is stored on the server-side and identified by a session ID cookie on the user's browser. Once logged in, Django checks the user's permissions to determine what views, actions, or resources they are authorized to access, based on their role or group in the system. Django implements authentication using the auth framework and handles authorization through permissions and groups tied to users or models.

### How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use.
Django tracks logged-in users using sessions and cookies. When a user logs in, Django creates a session on the server and sends a session ID cookie to the user's browser, which is sent back with each request to keep the user logged in.
Cookies can also store things like user preferences or security tokens, but they aren't always safe. They can be vulnerable to attacks like session hijacking or cross-site scripting (XSS). To protect cookies, developers can use Secure, HttpOnly, and SameSite settings to make them safer.

### Implement the register, login, and logout functions so that the user can access the application freely.

add this in view.py
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response

    else:
        form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

make register.html:
```
{% extends 'base.html' %} {% block meta %}
<title>Register</title>
{% endblock meta %} {% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Register" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```
make login.html
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```

add the URL path to urlpatterns
```
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
```

### make two user accounts with three dummy data each, using the model made in the application beforehand so that each data can be accessed by each account locally.

![](image/firstacc.png)
![](image/secacc.png)

### Connect the models Product and User.
import this in models.py
```
from django.contrib.auth.models import User
```
and also add this:
```
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

views.py:
```
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        mood_entry = form.save(commit=False)
        mood_entry.user = request.user
        mood_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```
The code establishes a relationship between the Product model and Django's User model. By adding user = models.ForeignKey(User, on_delete=models.CASCADE), each mood entry is linked to a specific user. This ensures that every Product instance is associated with a user, meaning multiple mood entries can belong to one user. The on_delete=models.CASCADE option ensures that if a user is deleted, all their associated mood entries are deleted as well, maintaining database integrity. This setup is common when creating user-specific content in Django applications.

### Display logged in user details such as username and apply cookies like last login to the application's main page.

add this in show_main function 
```
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)

    context = {
        'myname': request.user.username,
        'class': 'PBP KKI',
        'product_entries': product_entries,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
```
This view function retrieves user-specific product entries from the database, collects data into a context dictionary (including the user's last login time from a cookie), and passes it to the main.html template for rendering.

and also add this in main.html to show logout button and last login
```
<a href="{% url 'main:create_product_entry' %}">
  <button>Add New Product Entry</button>
</a>
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
<h5>Last login session: {{ last_login }}</h5>
{% endblock content %}
```

## assignment 5

### If there are multiple CSS selectors for an HTML element, explain the priority order of these CSS selectors
1. Inline Styles (highest priority) applied directly to elements using the style attribute.
2. IDs (#) have a higher specificity than class, attribute, and element selectors.
3. Classes, attributes, and pseudo-classes (., [attribute], :hover, etc.) share the next level of specificity.
4. Element selectors (e.g., div, p) and pseudo-elements (e.g., ::before, ::after) have the lowest specificity.
5. The universal selector (*) applies to all elements but carries the least weight.

### Why does responsive design become an important concept in web application development? Give examples of applications that have and have not implemented responsive design!
Responsive design is essential in web application development for several key reasons. It ensures optimal viewing across various devices, enhancing usability and accessibility for users. A well-implemented responsive design improves navigation and interaction, leading to higher engagement and retention rates. Additionally, mobile-friendly designs are prioritized by search engines like Google, which boosts discoverability. Furthermore, by maintaining a single codebase for all devices, responsive design reduces development and maintenance costs, making it a cost-effective solution for developers. example with responsive design: instagram, without responsive design: Old Government Websites

### Explain the differences between margin, border, and padding, and how to implement these three things!
Margin is the outermost space that creates a gap between an element and its surrounding elements, effectively pushing other elements away. It is used to create space outside an element, such as separating a button from a nearby paragraph, and can be set using the margin property. Border, on the other hand, is a line that surrounds an element, located between the margin and padding areas. Borders can be styled with different colors, widths, and styles (solid, dashed, etc.) and are typically used to visually separate elements or enhance the appearance of items like buttons and cards. They can be set using the border property , with options to specify individual sides using border-top, border-right, border-bottom, and border-left. Lastly, padding refers to the space between the content of an element and its border, creating space within the element and pushing the content away from the edges. Padding improves the visual appeal and readability of content and can be set using the padding property . Together, these properties help create well-structured and visually appealing web layouts.
example:

```
.box {
    margin: 20px;            /* Creates space outside the box */
    border: 2px solid blue;  /* Adds a blue border around the box */
    padding: 15px;           /* Creates space inside the box between the content and the border */
}

```

### Explain the concepts of flex box and grid layout along with their uses!
Flexbox, short for "Flexible Box Layout," is a one-dimensional layout model that allows for the arrangement of items along a single axis (either horizontally or vertically). It enables elements to expand, shrink, and distribute space dynamically, making it ideal for laying out components within a container. uses: Creating navigation bars, Aligning elements in a card layout, Distributing space in a gallery of images, Centering items both horizontally and vertically.
Grid Layout is a two-dimensional layout model that allows for the creation of complex layouts by defining rows and columns in a grid format. It gives designers precise control over the placement and sizing of elements within a container, making it suitable for more intricate designs. uses: Designing complex webpage layouts with multiple sections . Creating responsive layouts that adjust seamlessly to various screen sizes, Aligning content in a structured manner, such as photo galleries or product listings.

### Implement functions to delete and edit products.
Open views.py in the main subdirectory, and create a new function named edit_product and delete_product that takes request and id parameters as follows.
```
def edit_product(request, id):
    # Get mood entry based on id
    product = Product.objects.get(pk = id)

    # Set mood entry as an instance of the form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Save form and return to home page
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get product based on id
    product = Product.objects.get(pk = id)
    # Delete mood
    product.delete()
    # Return to home page
    return HttpResponseRedirect(reverse('main:show_main'))
```
create edit_product.html in main/templates and add:
```
{% extends 'base.html' %}
{% load static %}
{% block meta %}
<title>Edit Product</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}
<div class="flex flex-col min-h-screen bg-gray-100">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-black">Edit Product Entry</h1>
  
    <div class="bg-white rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6">
          {% csrf_token %}
          {% for field in form %}
              <div class="flex flex-col">
                  <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                      {{ field.label }}
                  </label>
                  <div class="w-full">
                      {{ field }}
                  </div>
                  {% if field.help_text %}
                      <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                  {% endif %}
                  {% for error in field.errors %}
                      <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                  {% endfor %}
              </div>
          {% endfor %}
          <div class="flex justify-center mt-6">
              <button type="submit" class="bg-indigo-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 transition duration-300 ease-in-out w-full">
                  Edit Product Entry
              </button>
          </div>
      </form>
  </div>
  </div>
</div>
{% endblock %}
```

add url to urls.py:
```
path('edit-product/<uuid:id>', edit_product, name='edit_product'),
path('delete/<uuid:id>', delete_product, name='delete_product'),
```

edit main.html:
```
<div class="flex justify-end mb-6">
        <a href="{% url 'main:create_product_entry' %}" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
            Add New Product Entry
        </a>
    </div>
```

add in card_product.html:
```
<a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
        </svg>
      </a>
```

### Customize the login, register, and add product pages to be as attractive as possible.
modify your login.html:
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center w-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8">
    <div>
      <h2 class="mt-6 text-center text-black text-3xl font-extrabold text-gray-900">
        Login to your account
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST" action="">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        <div>
          <label for="username" class="sr-only">Username</label>
          <input id="username" name="username" type="text" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Username">
        </div>
        <div>
          <label for="password" class="sr-only">Password</label>
          <input id="password" name="password" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Password">
        </div>
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Sign in
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      {% if message.tags == "success" %}
            <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% elif message.tags == "error" %}
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% else %}
            <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% endif %}
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-black">
        Don't have an account yet?
        <a href="{% url 'main:register' %}" class="font-medium text-indigo-200 hover:text-indigo-300">
          Register Now
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```
This Django template extends a base HTML layout and provides a login form for users. It features a centered design with input fields for username and password, a submit button, and support for CSRF protection. The template displays success or error messages based on the login attempt and includes a link for users to register if they do not have an account

modify your register.html:
```
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8 form-style">
    <div>
      <h2 class="mt-6 text-center text-3xl font-extrabold text-black">
        Create your account
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        {% for field in form %}
          <div class="{% if not forloop.first %}mt-4{% endif %}">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
              {{ field.label }}
            </label>
            <div class="relative">
              {{ field }}
              <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                {% if field.errors %}
                  <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                  </svg>
                {% endif %}
              </div>
            </div>
            {% if field.errors %}
              {% for error in field.errors %}
                <p class="mt-1 text-sm text-red-600">{{ error }}</p>
              {% endfor %}
            {% endif %}
          </div>
        {% endfor %}
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Register
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        <span class="block sm:inline">{{ message }}</span>
      </div>
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-black">
        Already have an account?
        <a href="{% url 'main:login' %}" class="font-medium text-indigo-200 hover:text-indigo-300">
          Login here
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```
modify create_product.html:
```
{% extends 'base.html' %}
{% load static %}
{% block meta %}
<title>Create Product</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}

<div class="flex flex-col min-h-screen bg-gray-100">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-black">Create Product Entry</h1>
  
    <div class="bg-white shadow-md rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div class="flex flex-col">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
              {{ field.label }}
            </label>
            <div class="w-full">
              {{ field }}
            </div>
            {% if field.help_text %}
              <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        <div class="flex justify-center mt-6">
          <button type="submit" class="bg-indigo-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 transition duration-300 ease-in-out w-full">
            Create Product Entry
          </button>
        </div>
      </form>
    </div>
  </div>
</div>

{% endblock %}
```

### If there are no products saved in the application, the product list page will display an image and a message that no products are registered.

add the following code in main.html:
```
{% if not product_entries %}
    <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
        <img src="{% static 'image/very-sad.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
        <p class="text-center text-gray-600 mt-4">There is no product data in vin-shop.</p>
```

### If there are products saved, the product list page will display details of each product using cards 
make card_product.html in main/templates and fill with the following code:
```
<div class="relative break-inside-avoid">
    <div class="absolute top-2 z-10 left-1/2 -translate-x-1/2 flex items-center -space-x-2">
      <div class="w-[3rem] h-8 bg-gray-200 rounded-md opacity-80 -rotate-90"></div>
      <div class="w-[3rem] h-8 bg-gray-200 rounded-md opacity-80 -rotate-90"></div>
    </div>
    <div class="relative top-5 bg-indigo-100 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-indigo-300 transform rotate-1 hover:rotate-0 transition-transform duration-300">
      <div class="bg-indigo-200 text-gray-800 p-4 rounded-t-lg border-b-2 border-indigo-300">
        <h3 class="font-bold text-xl mb-2">{{product_entry.name}}</h3>
      </div>
      <div class="p-4">
        <p class="font-semibold text-lg mb-2">Product</p> 
        <p class="text-gray-700 mb-2">
          <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">{{mood_entry.feelings}}</span>
        </p>
        <div class="mt-4">
          <p class="text-gray-700 font-semibold mb-2">Rating</p>
          <div class="relative pt-1">
            <div class="flex mb-2 items-center justify-between">
              <div>
                <span class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-indigo-600 bg-indigo-200">
                  {% if product_entry.rating > 10 %}10+{% else %}{{product_entry.rating}}{% endif %}
                </span>
              </div>
            </div>
            <div class="overflow-hidden h-2 mb-4 text-xs flex rounded bg-indigo-200">
              <div style="width:{% if product_entry.rating > 10 %}100%{% else %}{{ product_entry.rating }}0%{% endif %}" class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-indigo-500"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="absolute top-0 -right-4 flex space-x-1">
      <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
          <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
        </svg>
      </a>
      <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
        </svg>
      </a>
    </div>
  </div>
```

### For each product card, create two buttons to edit and delete the product on that card
make sure to implement this code in card_product.html:
```
<div class="absolute top-0 -right-4 flex space-x-1">
      <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
          <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
        </svg>
      </a>
      <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
        </svg>
      </a>
    </div>
```
This code snippet creates a set of action buttons for editing and deleting a product entry within a web application. The buttons are styled using Tailwind CSS, featuring a yellow edit button and a red delete button, both with hover effects and rounded shapes. The edit button links to the product edit page using Django's URL template tag, while the delete button links to the product deletion endpoint. 

### Create a navigation bar (navbar) for the features in the application that is responsive to different device sizes, especially mobile and desktop.

make navbar.html in templates located in root directory and add the following code:
```
<nav class="bg-indigo-600 shadow-lg fixed top-0 left-0 z-40 w-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <h1 class="text-2xl font-bold text-center text-white">vin-shop</h1>
        </div>
        <div class="hidden md:flex items-center space-x-4">
            {% if user.is_authenticated %}
                <a href="#" class="text-white text-lg hover:text-gray-300 block">Home</a>
                <a href="#" class="text-white text-lg hover:text-gray-300 block">Products</a>
                <a href="#" class="text-white text-lg hover:text-gray-300 block">Categories</a>
                <a href="#" class="text-white text-lg hover:text-gray-300 block">Cart</a>
                <span class="text-gray-300">Welcome, {{ user.username }}</span>
                <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                    Logout
                </a>
            {% else %}
                <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
                    Login
                </a>
                <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                    Register
                </a>
            {% endif %}
        </div>
        <div class="md:hidden flex items-center">
          <button class="mobile-menu-button">
            <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile menu -->
    
    <div class="mobile-menu hidden md:hidden  px-4 w-full md:max-w-full">
        <div class="pt-2 pb-3 space-y-1 mx-auto">
            {% if user.is_authenticated %}
                <a href="#" class="text-white text-lg hover:text-gray-300 block">Home</a>
                <a href="#" class="text-white text-lg hover:text-gray-300 block">Products</a>
                <a href="#" class="text-white text-lg hover:text-gray-300 block">Categories</a>
                <a href="#" class="text-white text-lg hover:text-gray-300 block">Cart</a>
                <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
                <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                    Logout
                </a>
            {% else %}
                <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
                    Login
                </a>
                <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                    Register
                </a>
            {% endif %}
        </div>
    </div>
    <script>
        const btn = document.querySelector("button.mobile-menu-button");
        const menu = document.querySelector(".mobile-menu");
    
        btn.addEventListener("click", () => {
        menu.classList.toggle("hidden");
        });
    </script>
</nav>
```
This code snippet creates a responsive navigation bar for a web application using Tailwind CSS. It features a title ("vin-shop") and links to Home, Products, Categories, and Cart, depending on user authentication. Authenticated users see a welcome message and a logout button, while non-authenticated users see login and registration buttons. A hamburger menu icon appears on mobile devices, toggling the mobile menu's visibility when clicked. This design ensures a user-friendly experience across different screen sizes.