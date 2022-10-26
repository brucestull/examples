# Create Simple View Function Without Using a Template

## Resources:

## Process:

1. Add import for `include` from `django.urls` and create a URL pattern for the application `the_app` to `urlpatterns` in the project URL configuration file [`the_project/urls.py`](../the_project/urls.py):
        ```
        from django.urls import include
    
        urlpatterns = [
            #...
            path('url-fragment-to-the-app/', include('the_app.urls')),
            #...
        ]
        ```

1. Create [`the_app/urls.py`](../the_app/urls.py) and add the following:
    * Import of `path` from `django.urls`.
    * Import of `views` from `.`.
    * The `path()` function, with following arguments, to a list called `urlpatterns`:
        * route: `'url-fragment-for-simple-view-function-fragment/'`
        * view: `views.simple_view_function`
            * We will create this in next step.
        * name: `'simple_view_name'`
        ```
        from django.urls import path
        
        from . import views
        
        
        app_name = 'our_app_name'
        
        urlpatterns = [
            path('url-fragment-for-simple-view-function-fragment/', views.simple_view_function, name='simple_view_name'),
        ]
        ```

1. Create Django view function `simple_view_function` in [`the_app/views.py`](../the_app/views.py):
    ```
    def simple_view_function(request):
        return HttpResponse("A hard-coded string to display on webpage!")
    ```

1. Start development server, if not already running, and test the URL pattern we specified in [`the_project/urls.py`](../the_project/urls.py) and [`the_app/urls.py`](../the_app/urls.py):
    * `python .\manage.py runserver`
    * The URL we specified:
        * URL fragment from [`the_project/urls.py`](../the_project/urls.py):
            * `'url-fragment-to-the-app/'`
        * URL fragment from [`the_app/urls.py`](../the_app/urls.py):
            * `'url-fragment-for-simple-view-function-fragment/'`
        * The actual URL we test is server root added to the two above patterns:
            * http://localhost:8000/url-fragment-to-the-app/url-fragment-for-simple-view-function
            * --OR--
            * http://localhost:8000/url-fragment-to-the-app/url-fragment-for-simple-view-function/

1. Verify text string passed into `HttpResponse` contstructor in view function `simple_view_function` is present on webpage.



