# 03 - Create Index View
* This project's directory: [`reverse/`](./../)

## Resources:
* [django.urls](https://docs.djangoproject.com/en/4.1/ref/urlresolvers/#module-django.urls)
    * [`path()`](https://docs.djangoproject.com/en/4.1/ref/urls/#path)
    * [`include()`](https://docs.djangoproject.com/en/4.1/ref/urls/#include)
* [`django.shortcuts`](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/#module-django.shortcuts)
    * [`render()`](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/#render)
* [`django.http`](https://docs.djangoproject.com/en/4.1/ref/request-response/#module-django.http)
    * [`HttpResponse`](https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpResponse)


## Code Examples Repository links:
* [Code Examples Repository - README.md](../../../README.md)
    * [`examples/`](../../../)
* [Django Code Examples - README.md](../../README.md)
    * [`examples/django/`](../../)


## Tag meanings for this guide:
* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.


## Process:

### Add Application Route to Project URL Configuration File:
1. **ACTION:** Add a route for the application `the_app` to the Django Project `the_project`:
    * Add a [`path()`](https://docs.djangoproject.com/en/4.1/ref/urls/#path) to the `urlpatterns` attribute of project URL configuration file [`the_project/urls.py`](../the_project/urls.py):
        * We will import [`include`](https://docs.djangoproject.com/en/4.1/ref/urls/#include) from `django.urls`.
        * This `path()` function will have the following arguments:
            * route: `''`
            * view: `include('the_app.urls')`
                * The `include()` function will have the following argument:
                    * module: `'the_app.urls'`
                        * We will create the module `the_app.urls` in the next section.
    <details>
    <summary>Sample <code>the_project/urls.py</code> addition:</summary>

        #...
        from django.urls import include
        #...

        urlpatterns = [
            #...
            path('', include('the_app.urls')),
            #...
        ]
    </details>


### Add URL Mapping:
1. **ACTION:** Create a application URL configuration file [`the_app/urls.py`](../the_app/urls.py):
    1. Import [`path`](https://docs.djangoproject.com/en/4.1/ref/urls/#path) from `django.urls`.
    1. Import [`views`](../the_app/views.py) from `.`.
    1. Add an attribute `app_name`:
        * `app_name = 'the_app'`
    1. Add an attribute `urlpatterns`, which is a list of `urlpattern`s.
    1. Add a `path()` to the `urlpatterns` attribute:
        * This `path()` function will have the following arguments:
            * route: `''`
            * view: `views.index`
                * We will create the `index` view function in the [`views.py`](../the_app/views.py) module in the next section.
                * This `views.index` argument is the thing which will call the `index` view function in [`views.py`](../the_app/views.py). When a user sends a request to the route `''`, the `index` view function will be called (will run the view function).
            * name: `name='index'`

    <details>
    <summary>Sample <code>the_app/urls.py</code> contents:</summary>

        from django.urls import path
        from . import views

        app_name = 'the_app'
        urlpatterns = [
            path('', views.index, name='index'),
        ]
    </details>

1. **INFO:** When the user sends an HTTP request to the server root, the `urlpattern` we created above will call a view function `index` in the [`views.py`](../the_app/views.py) module, which will render the [`the_app/templates/index.html`](../the_app/templates/index.html) template.
    * We will create the view function in the next section.
    * **TODO:** Add explanation for how the HTTP request to the server root is handled.


### Add View Function:
1. Add a view function `index` to [`the_app/views.py`](../the_app/views.py):
    1. Verify import of [`render`](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/#render) from [`django.shortcuts`](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/#module-django.shortcuts).
    1. Add `index` view function:
        * We will call the view function `index`.
        * We will return whatever object is returned from the `render()` function.
            * This returned object will be an [`HttpResponse`](https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpResponse) object.
        * We will add the following arguments to the `render()` function call:
            * request: `request`
            * template_name: `'index.html'`
                * We will create the [`index.html`](../the_app/templates/index.html) template in the next section.
    <details>
    <summary>Sample <code>views.py</code> contents:</summary>

        from django.shortcuts import render
        
        def index(request):
            return render(request, 'index.html')
    </details> 


### Add Application Template:
1. **ACTION:** Create a [`templates`](../the_app/templates/) directory in [`the_app/`](../the_app/) directory.
1. **ACTION:** Add a template [`index.html`](../the_app/templates/index.html) to the [`templates`](../the_app/templates/) directory:
    <details>
    <summary>Sample <code>index.html</code> contents:</summary>

        <h1>Goodbuy, World! Enjoy the Sale!</h1>
    </details>

### Test the Application's `index` View:
1. Start the development server:
    * `python .\manage.py runserver`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> python .\manage.py runserver
            Watching for file changes with StatReloader
            Performing system checks...

            System check identified no issues (0 silenced).

            You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
            Run 'python manage.py migrate' to apply them.
            September 16, 2022 - 08:10:01
            Django version 4.0, using settings 'the_project.settings'
            Starting development server at http://127.0.0.1:8000/
            Quit the server with CTRL-BREAK.
        </details>

1. Open internet browser to application URL (the server root URL):
    * http://localhost:8000/

1. Verify webpage displays the string we included in [`index.html`](../the_app/templates/index.html):
    * Sample webpage display contents:
        * `Goodbuy, World! Enjoy the Sale!`

1. **INFO:** Proceed to [Use Django's `reverse` Function](./04_use_djangos_reverse_function.md)

## Repository Links:
* Back to [Create Django Application](./02_create_django_application.md)