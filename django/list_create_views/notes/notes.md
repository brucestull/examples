# Create Django Project with List View First
* The intent is to show that it can be useful to create the Django List View first so user can see the models presented on the page and then add links to the other pages, templates, and views.
    1. Might expand this later to use `if request.method==POST` and `if request.method==GET` somewhere.
    1. For now, create a simple template with a list as a `home` or `list` page.

## Resources:
* **TODO**: LINK_TO_PIPENV_EXAMPLE_DOCUMENTATION

## Repository Links:
* [Examples Repository](../../../README.md)
* [Create Django Project with List View First - `README.me`](../README.md)

## Tag meanings for this guide:
* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.

## Process:

### Create Django skeleton:

1. **ACTION:** Start in the directory which will contain our Django project:
    * Sample directory location:
        * `C:\Users\Bruce\Programming\examples\django\list_create_views`
1. **ACTION:** Create `pipenv` virtual environment:
    * `pipenv install django==4.0`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_create_views> pipenv install django==4.0
            Creating a virtualenv for this project...
            Pipfile: C:\Users\Bruce\Programming\examples\django\list_create_views\Pipfile
            Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.6) to create virtualenv...
            [   =] Creating virtual environment...created virtual environment CPython3.10.6.final.0-64 in 429ms
            creator CPython3Windows(dest=C:\Users\Bruce\.virtualenvs\list_create_views-KAifsCX6, clear=False, no_vcs_ignore=False, global=False)
            seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Bruce\AppData\Local\pypa\virtualenv)
                added seed packages: pip==22.2.2, setuptools==63.4.3, wheel==0.37.1
            activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

            Successfully created virtual environment!
            Virtualenv location: C:\Users\Bruce\.virtualenvs\list_create_views-KAifsCX6
            Creating a Pipfile for this project...
            Installing django==4.0...
            Adding django to Pipfile's [packages]...
            Installation Succeeded
            Pipfile.lock not found, creating...
            Locking [dev-packages] dependencies...
            Locking [packages] dependencies...
            Locking...
            Resolving dependencies...
            Success!
            Updated Pipfile.lock (036cf0)!
            Installing dependencies from Pipfile.lock (036cf0)...
            ================================ 0/0 - 00:00:00
            To activate this project's virtualenv, run pipenv shell.
            Alternatively, run a command inside the virtualenv with pipenv run.
            PS C:\Users\Bruce\Programming\examples\django\list_create_views>
        </details>

1. **ACTION:** Activate `pipenv` virtual environment:
    * `pipenv shell`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_create_views> pipenv shell
            Launching subshell in virtual environment...
            PowerShell 7.2.6
            Copyright (c) Microsoft Corporation.

            https://aka.ms/powershell
            Type 'help' to get help.

            PS C:\Users\Bruce\Programming\examples\django\list_create_views>
        </details>

1. **INFO:** Verify we have Django installed:
    * `pip list`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_create_views> pip list
            Package    Version
            ---------- -------
            asgiref    3.5.2
            Django     4.0
            pip        22.2.2
            setuptools 63.4.3
            sqlparse   0.4.2
            tzdata     2022.2
            wheel      0.37.1
            PS C:\Users\Bruce\Programming\examples\django\list_create_views>
        </details>

1. **ACTION:** Create Django project:
    * `django-admin startproject the_project .`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_create_views> django-admin startproject the_project .
            PS C:\Users\Bruce\Programming\examples\django\list_create_views>
        </details>

1. **INFO:** Examine directory structure:
    * `tree /f /a`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_create_views> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   manage.py
            |   Pipfile
            |   Pipfile.lock
            |   README.md
            |
            +---notes
            |       notes.md
            |
            \---the_project
                    asgi.py
                    settings.py
                    urls.py
                    wsgi.py
                    __init__.py

            PS C:\Users\Bruce\Programming\examples\django\list_create_views>
        </details>

1. **INFO:** Note new directory [`the_project`](../the_project/)

1. **INFO:** Test development server:
    * `python .\manage.py runserver`
    * Development server can be stopped by using Ctrl+C in terminal.

1. **INFO:** Open internet browser to development server address:
    * http://localhost:8000/

1. **INFO:** Verify the Django Green Rocket is visible and the following text shows:
    * `The install worked successfully! Congratulations!`

1. **ACTION:** Create Django application:
    * `python .\manage.py startapp the_app`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_create_views> python .\manage.py startapp the_app
            PS C:\Users\Bruce\Programming\examples\django\list_create_views>
        </details>

1. **INFO:** Examine directory structure:
    * `tree /f /a`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_create_views> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   db.sqlite3
            |   manage.py
            |   Pipfile
            |   Pipfile.lock
            |   README.md
            |
            +---notes
            |       notes.md
            |
            +---the_app
            |   |   admin.py
            |   |   apps.py
            |   |   models.py
            |   |   tests.py
            |   |   views.py
            |   |   __init__.py
            |   |
            |   \---migrations
            |           __init__.py
            |
            \---the_project
                    asgi.py
                    settings.py
                    urls.py
                    wsgi.py
                    __init__.py

            PS C:\Users\Bruce\Programming\examples\django\list_create_views>
        </details>

1. **ACTION:** Edit [`settings.py`](../the_project/settings.py):
    * Add the [`AppConfig`](https://docs.djangoproject.com/en/4.0/ref/applications/#django.apps.AppConfig) for `the_app` to `INSTALLED_APPS`:
    * `AppConfig` for `the_app` is found in [`the_app/apps.py`](../the_app/apps.py)
        <details>
        <summary>Sample edit</summary>

            INSTALLED_APPS = [
                ...
                'the_app.apps.TheAppConfig',
                ...
            ]
        </details>

### Add URL route for the app:
1. **ACTION:** Add entry to `urlpatterns` list in [`the_project/urls.py`](../the_project/urls.py) for `the_app`:
    * Import `include` from [`django.urls`](https://docs.djangoproject.com/en/4.0/ref/urls/).
    * Confirm we have import `path` from [`django.urls`](https://docs.djangoproject.com/en/4.0/ref/urls/).
    * Add `path()` with following arguments:
        * route:
            * `the-app`
        * view:
            * `include('the_app.urls')`

        <details>
        <summary>Sample edit</summary>

            ...
            from django.urls import path, include
            ...

            ...
            urlpatterns = [
                ...
                path('the-app/', include('the_app.urls')),
                ...
            ]
            ...
        </details>


### Return an `HttpResponse` from request to `the-app/index-url/`:

1. **ACTION:** Create [`the_app/urls.py`](../the_app/urls.py) and add URL route for the `index_view` view to it:
    * Import `path` from `django.urls`.
    * Import `views` from `.`.
    * Add our `app_name`, `the_app`.
    * Add `path()` to `urlpatterns` with following arguments:
        * route:
            * `'index-url/'`
        * view:
            * `views.index_view`
        * name:
            * `name='index_url_name'`

        <details>
        <summary>Sample edit</summary>

            from django.urls import path
            from . import views

            app_name = 'the_app'
            urlpatterns = [
                path('index-url/', views.index_view, name='index_url_name')
            ]
        </details>

1. **ACTION:** Create view function `index_view` in [`the_app/views.py`](../the_app/views.py):
    * Import `HttpResponse` from `django.http`.
    * Add function-based view `index_view`.
        <details>
        <summary>Sample edit</summary>

            ...
            from django.http import HttpResponse
            ...

            ...
            def index_view(request):
                the_return_string = 'Goodbuy, World! Enjoy the sail!'
                return HttpResponse(the_return_string)
            ...
        </details>

1. **INFO:** Test development server to ensure our view function is working:
    * `python .\manage.py runserver`

1. **INFO:** Open internet browser to application URL:
    * Server address:
        * http://localhost:8000/
    * URL route to index view:
        * `the-app/index-url/`
    * So the browser URL we use is:
        * http://localhost:8000/the-app/index-url/

1. **INFO:** Verify internet browser displays `the_return_string` in [`the_app/views.py`](../the_app/views.py):
    * `Goodbuy, World! Enjoy the sail!`

1. **INFO:** Our app URL route `the-app/index-url/` now calls the view function `index_view` which returns an `HttpResponse`. We can proceed to build our model and modify view function to return data from the database rather than returning a `HttpResponse` which contains a hard-coded string.

### Display database contents on an `index` page:

1. **INFO:** We will use the same URL path `the-app/index-url/` which calls the function-based view function `index_view`. But, first, we need to create a model and database to provide information to display on the index page.

1. **ACTION:** Create model `AwesomeCat` in [`the_app/models.py`](../the_app/models.py):
    * Current model will only have one attribute.
    * Import [`models`](https://docs.djangoproject.com/en/4.0/topics/db/models/) from `django.db`.
    * Create Python `class` `AwesomeCat`.
    * Add `name` attribute to `AwesomeCat`.
    * The `name` attribute is a [`models.CharField`](https://docs.djangoproject.com/en/4.0/ref/models/fields/#charfield) object.

        <details>
        <summary>Sample edit</summary>

            from django.db import models

            class AwesomeCat(models.Model):
                name = models.CharField(max_length=50)

                def __str__(thine_fuzzy_self):
                    return f"{thine_fuzzy_self.id} : {thine_fuzzy_self.name}"
        </details>

1. **ACTION:** Make migrations for our models:
    * `python .\manage.py makemigrations`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_create_views> python .\manage.py makemigrations
            Migrations for 'the_app':
              the_app\migrations\0001_initial.py
                - Create model AwesomeCat
            PS C:\Users\Bruce\Programming\examples\django\list_create_views>
        </details>

1. **ACTION:** Perform `migrate`:
    * `python .\manage.py migrate`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_create_views> python .\manage.py migrate
            Operations to perform:
              Apply all migrations: admin, auth, contenttypes, sessions, the_app
            Running migrations:
              Applying contenttypes.0001_initial... OK
              Applying auth.0001_initial... OK
              Applying admin.0001_initial... OK
              Applying admin.0002_logentry_remove_auto_add... OK
              Applying admin.0003_logentry_add_action_flag_choices... OK
              Applying contenttypes.0002_remove_content_type_name... OK
              Applying auth.0002_alter_permission_name_max_length... OK
              Applying auth.0003_alter_user_email_max_length... OK
              Applying auth.0004_alter_user_username_opts... OK
              Applying auth.0005_alter_user_last_login_null... OK
              Applying auth.0006_require_contenttypes_0002... OK
              Applying auth.0007_alter_validators_add_error_messages... OK
              Applying auth.0008_alter_user_username_max_length... OK
              Applying auth.0009_alter_user_last_name_max_length... OK
              Applying auth.0010_alter_group_name_max_length... OK
              Applying auth.0011_update_proxy_permissions... OK
              Applying auth.0012_alter_user_first_name_max_length... OK
              Applying sessions.0001_initial... OK
              Applying the_app.0001_initial... OK
            PS C:\Users\Bruce\Programming\examples\django\list_create_views>
        </details>

1. **ACTION:** Create a superuser:
    * `python .\manage.py createsuperuser`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_create_views> python .\manage.py createsuperuser
            Username (leave blank to use 'bruce'): admin
            Email address: admin@email.app
            Password:
            Password (again):
            This password is too common.
            Bypass password validation and create user anyway? [y/N]: y
            Superuser created successfully.
            PS C:\Users\Bruce\Programming\examples\django\list_create_views>
        </details>

1. **INFO:** Start development server to test django admin integration:
    * `python .\manage.py runserver`

1. **INFO:** Open internet browser to Django admin interface:
    * http://localhost:8000/admin

1. **INFO:** Django admin interface functions but we forgot to add the model to [`the_app/admin.py`](../the_app/admin.py).

1. **ACTION:** Add model `AwesomeCat` as argument to `admin.site.register()` in [`the_app/admin.py`](../the_app/admin.py):
    * Import `admin` from `django.db`.
    * Import `AwesomeCat` from `.models`.
    * Add `admin.site.register(AwesomeCat)`
    <details>
    <summary>Sample edit</summary>

        from django.contrib import admin
        from .models import AwesomeCat


        admin.site.register(AwesomeCat)
    </details>

1. **INFO:** Open internet browser to Django admin interface:
    * http://localhost:8000/admin

1. **ACTION:** Add a couple `AwesomeCat`s to the database.
    * The only attribute in the database is the `name` of the model `AwesomeCat`.

1. **INFO:** We now have a couple items in the database so we can create a Django view function that will display the model values from the database.

1. **ACTION:** Add a line to the `index_view` function in [`the_app/views.py`](../the_app/views.py) that gets the `AwesomeCat` model values from the database and prints them to console:
    <details>
    <summary>Sample edit</summary>

        from .models import AwesomeCat

        def index_view(request):

            awesome_cat_objects = AwesomeCat.objects.all()
            print(awesome_cat_objects)
            
            the_return_string = 'Goodbuy, World! Enjoy the sail!'
            return HttpResponse(the_return_string)
    </details>

1. **ACTION:** Open internet browser to our app URL and check the output of the view function in console:
    * http://localhost:8000/the-app/index-url/
        <details>
        <summary>Sample console output</summary>

            <QuerySet [<AwesomeCat: 1 : Dezzi>, <AwesomeCat: 2 : Bunbun>]>
        </details>

1. **INFO:** Notes about the above output:
    * We have a `QuerySet` object that is a list-like object, and that `QuerySet` contains all the `AwesomeCat` objects.

1. **INFO:** We now have a `QuerySet` object that contains all the `AwesomeCat` objects. We can now pass this `QuerySet` object as part of a context object dictionary to the `render` function.

1. **ACTION:** Edit the `index_view` function in [`the-app/views.py`](../the_app/views.py) to pass the `QuerySet` object to the `render` function:
    * Import `render` from `django.shortcuts`.
    * Import `reverse` from `django.urls`.
    * Edit `index_view`.

        <details>
        <summary>Sample current `the-app/views.py` contents</summary>

            from django.shortcuts import render

            from .models import AwesomeCat

            def index_view(request):
                """
                Simple `index_view` method that renders the `AwesomeCat` list template.
                """
                awesome_cat_objects = AwesomeCat.objects.all()
                print(awesome_cat_objects)
                context = {
                    'view_to_template_objects': awesome_cat_objects
                }
                return render(request, 'the_app/index_template.html', context)
        </details>

1. **INFO:** Start development server:
    * `python .\manage.py runserver`

1. **INFO:** Open internet browser to application URL:
    * http://localhost:8000/the-app/index-url/

1. **INFO:** Sample webpage content:
    * `<QuerySet [<AwesomeCat: 1 : Dezzi>, <AwesomeCat: 2 : Bunbun>]>`

1. **INFO:** We now have the `QuerySet` object which contains the `AwesomeCat` objects displayed in the web page.

1. **INFO:** Let's see if we can get the `AwesomeCat` objects from the `QuerySet` object.

1. **ACTION:** Edit the Django template [`the_app/index_template.html`](../the_app/templates/the_app/index_template.html) to use a Django template engine for loop to iterate over the list of `AwesomeCat` objects (`view_to_template_objects`). We will display the `name` attribute and the `id` attribute of each `AwesomeCat` object (`cat_object`):

    <details>
    <summary>Sample edit</summary>

        {% for cat_object in view_to_template_objects %}
        {{ cat_object.name }} : {{ cat_object.id}}
        {% endfor %}
    </details>

1. **INFO:** Start development server and test webpage:
    1. `python .\manage.py runserver`
    1. http://localhost:8000/the-app/index-url/
        <details>
        <summary>Sample webpage contents</summary>

            Dezzi : 1 Bunbun : 2
        </details>

1. **INFO:** Notes about the above output:
    * After the edits we made to [`the_app/index_template.html`](../the_app/templates/the_app/index_template.html) we now see a couple things:
        * We no longer see `QuerySet` object and the `AwesomeCat` object displayed as objects.
        * We see the actual `id` and `name` attributes of the `AwesomeCat` objects.
        * The attributes of both `AwesomeCat` objects show on the same line since we aren't using any HTML elements to cause a line break between the first and last `AwesomeCat` object.

1. **INFO:** We now have a Django list view displaying on a webpage. Let's start to build out a create view so the end user can add `AwesomeCat` objects using the application GUI we create rather than the Django Admin Interface.

### **NOTE**: The list view is completed.
* The user can add their own functionality to the list view or continue the guide below to add a create view.

### Build out a create view for our application
* **INFO:** For this exercise we will add the `form` which is used for user input to our current `the-app/index_template.html` template. There are other solutions to this but we will leave those to other guides.
* In the below steps we will do the following:
    1. Add a `form` element to the template.
        1. Add a `action` attribute to the `form` element tag.
            1. This `action` attribute will use a [{% url 'app:url_name' %}](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#url) Django template tag.
        1. Add a `method` attribute to the `form` element tag.
        1. Add a [`{% csrf_token %}`](https://docs.djangoproject.com/en/4.1/howto/csrf/#how-to-use-django-s-csrf-protection) template tag to the `form` element.
        1. Add an HTML `input` element (for user text input) to the `form` element.
            1. Add a `type` attribute to the user text `input` element tag.
            1. Add a `name` attribute to the user text `input` element tag.
        1. Add an HTML `input` element (for the submit button) to the `form` element.
            1. Add a `type` attribute to the submit button `input` element tag.
            1. Add a `value` attribute to the submit button `input` element tag.

1. **ACTION:** Add `form` element to `the_app/index_template.html`:
    * Sample current implementation:
        ```
            <form></form>
        ```

1. **ACTION:** Add an `action` attribute to the `form` element tag:
    * This attribute will use a Django url template tag to generate the URL for us so we don't have to hard-code the URL.
        * `the_app` is our app name specified by `app_name = 'the_app'` in the urls configuration [`the_app/urls.py`](../the_app/urls.py)
        * `create` is the url name we will specify by `name='create'` in the `path` list item in the `urlpatterns` variable located in [`the_app\urls.py`](../the_app/urls.py)
    * Sample current implementation:
        ```
            <form action="{% url 'the_app:create_url_name"></form>
        ```

1. **ACTION:** Add a `method` attribute to the `form` element tag:
    * We will use a `post` method since it had the many features needed when writing to a database or creating new entries.
    * Reference:
        * [HTML \<form\> method Attribute - w3schools.com](https://www.w3schools.com/tags/att_form_method.asp)
    * Sample current implementation:
        ```
            <form action="{% url 'the_app:create' %}" method="post">
        ```

1. **ACTION:** Add a [`{% csrf_token %}`](https://docs.djangoproject.com/en/4.1/howto/csrf/#how-to-use-django-s-csrf-protection) template tag to the `form` element:
    * Sample current implementation:
        ```
            <form action="{% url 'the_app:create' %}" method="post">
                {% csrf_token %}
            </form>
        ```

1. **ACTION:** Add an HTML `input` element (for user text input) to the `form` element:
    * Sample current implementation:
        ```
            <form action="{% url 'the_app:create' %}" method="post">
                {% csrf_token %}
                <input/>
            </form>
        ```

1. **ACTION:** Add a `type` attribute `text` to the user text `input` element tag:
    * Sample current implementation:
        ```
            <form action="{% url 'the_app:create' %}" method="post">
                {% csrf_token %}
                <input type="text"/>
            </form>
        ```

1. **ACTION:** Add a `name` attribute `text_the_user_provided` to the user text `input` element tag:
    * Sample current implementation:
        ```
            <form action="{% url 'the_app:create' %}" method="post">
                {% csrf_token %}
                <input type="text" name="text_the_user_provided"/>
            </form>
        ```

1. **ACTION:** Add an HTML `input` element (for the submit button) to the `form` element:
    * Sample current implementation:
        ```
            <form action="{% url 'the_app:create' %}" method="post">
                {% csrf_token %}
                <input type="text" name="text_the_user_provided"/>
                <input/>
            </form>
        ```

1. **ACTION:** Add a `type` attribute `submit` to the submit button `input` element tag:
    * Sample current implementation:
        ```
            <form action="{% url 'the_app:create' %}" method="post">
                {% csrf_token %}
                <input type="text" name="text_the_user_provided"/>
                <input type="submit"/>
            </form>
        ```

1. **ACTION:** Add a `value` attribute `Send input box text to view function?` to the submit button `input` element tag:
    * Sample current implementation:
        ```
            <form action="{% url 'the_app:create' %}" method="post">
                {% csrf_token %}
                <input type="text" name="text_the_user_provided"/>
                <input type="submit" value="Send input box text to view function?"/>
            </form>
        ```

1. **INFO:** We have the `form` set up in the `the_app/index_template.html` template. We can now set up a url path in [`the_app/urls.py`](../the_app/urls.py) which will be used by the `form`'s `action` attribute.

1. **ACTION:** Add a `path`, which will return a `URLPattern` for the create view, to `urlpatterns` in [`the_app/urls.py`](../the_app/urls.py):
    * We will use the following concepts:
        * Use Django [`path`](https://docs.djangoproject.com/en/4.0/ref/urls/#path) function to add a `URLPattern` to the `urlpatterns` variable in [`the_app/urls.py`](../the_app/urls.py)
            * Ensure we still have the import of `views` from `.`.
            * Django [`path`](https://docs.djangoproject.com/en/4.0/ref/urls/#path) arguments we will use:
                * route:
                    * `'create/'`
                * view:
                    * `views.create`
                * name:
                    * `name='create'`
    * The `path` function we are going to add, with arguments:
        * `path('create/', views.create, name='create')`
    * Sample current [`the_app/urls.py`](../the_app/urls.py) implementation:
        ```
            from django.urls import path

            from . import views


            app_name = 'the_app'
            urlpatterns = [
                path('index-url/', views.index_view, name='index_url_name'),
                path('create/', views.create, name='create'),
            ]
        ```

1. **INFO:** We now have the `URLPattern` set up. We can now add the view function `create` to [`the_app/views.py`](../the_app/views.py)

1. **INFO:** Since we are using only one template, we need to design the `create` view function so that it renders the [`the_app/index_template.html`](../the_app/templates/the_app/index_template.html) template.

1. **ACTION:** Add a `create` view function to [`the_app/views.py`](../the_app/views.py):
    * We will initially just render a string on the webpage to ensure our view function is getting called by the `URLPattern` we created for the `create` view in the `urlpatterns` of [`the_app\urls.py`](../the_app/urls.py)
    * Concepts used here:
        * Import of [`HTTPResponse`](https://docs.djangoproject.com/en/4.0/ref/request-response/#httpresponse-objects) from `django.http`.
    * Sample current implementation:
        ```
            from django.http import HttpResponse

            def create(request):
                console_string = "Create view, ACTIVATED! ...CONSOLE!"
                print(console_string)
                web_response_string = "Create view, ACTIVATED! ...BROWSER!"
                return HttpResponse(web_response_string)
        ```

1. **INFO:** Our `create` view is now functioning with hard-coded values. We will now figure out how to get the information from the `request` object.
    * I think the `request` object we usually get passed into our view functions, in Django development server, is a `WSGIRequest` which is a type of [`HTTPRequest`](https://docs.djangoproject.com/en/4.0/ref/request-response/#django.http.HttpRequest).
    * The `request` object will contain values passed from the `form` element in [`the_app/index_template.html`](../the_app/templates/the_app/index_template.html)
        * These values will be passed through the request object with the keys specified by `name` attribute in the `form` element tag.

1. **ACTION:** But, first, we will check the dunder string and the `type` of the `request` object.
    * Add two print statements to the `create` view function.
        * Sample current implementation:
            ```
                def create(request):
                    ...
                    print('request: ', request)
                    print('type(request): ', type(request))
                    ...
                    return HttpResponse(web_response_string)
            ```

1. **INFO:** Start the development server and go to the URL which will take us to THE_PLACE_WE_GO.
    1. `python .\manage.py runserver`
    1. http://localhost:8000/the-app/index-url/

1. **INFO:** Click the `Send input box text to view function?` button without anything provided in the text box.
    * Relavent sample console output:
        ```
            request: <WSGIRequest: POST '/the-app/create/'>
            type(request): <class 'django.core.handlers.wsgi.WSGIRequest'>
        ```

1. **ACTION:** There is a specific part of the `request` object which we are interested in. That part is the `request.POST`.
    * Change the two print statements we created above to print `request.POST` instead of `request`.
        * Sample current implementation:
            ```
                def create(request):
                    ...
                    print('request.POST: ', request.POST)
                    print('type(request.POST): ', type(request.POST))
                    ...
                    return HttpResponse(web_response_string)
            ```

1. **INFO:** Start the development server and go to the URL which will take us to THE_PLACE_WE_GO.
    1. `python .\manage.py runserver`
    1. http://localhost:8000/the-app/index-url/

1. **INFO:** Click the `Send input box text to view function?` button without anything provided in the text box.
    * Relavent sample console output:
        ```
            request.POST:  <QueryDict: {
                'csrfmiddlewaretoken': ['kndozbWMqCwp4f6DWMwz7t91yKCLf1Smy2Bf1UaEFZ8cxowrDJiNQMvEFMGn9kuW'],
                'text_the_user_provided': ['']
            }>
            type(request.POST):  <class 'django.http.request.QueryDict'>
        ```

1. Comment out print statements except the following. It is the one we are going to focus on:
    * `print('request.POST: ', request.POST)`

1. **INFO:** Start the development server and go to the URL which will take us to THE_PLACE_WE_GO.
    1. `python .\manage.py runserver`
    1. http://localhost:8000/the-app/index-url/

1. **INFO:** Let's now add some text to the text box and click the `Send input box text to view function?` button.

1. Enter some text into the text box and click the `Send input box text to view function?` button:
    * Sample text: `Butter the cat`

1. Sample console output:
    ```
        request.POST:  <QueryDict: {
            'csrfmiddlewaretoken': ['tGop19JieHBTYPaVHLrl3npn9OCC2t7lHlMgtSXat4dGrYAJoIdzMGL0gQGeWMJV'],
            'text_the_user_provided': ['Butter the cat']
        }>
    ```

1. Let's look again at [`the_app/index_template.html`](../the_app/templates/the_app/index_template.html) and note some things:
    * 