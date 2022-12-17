# Home Page with String

## Resources

* [URL namespaces and included URLconfs](https://docs.djangoproject.com/en/4.0/topics/http/urls/#url-namespaces-and-included-urlconfs)
* [Writing views](https://docs.djangoproject.com/en/4.0/topics/http/views/#writing-views)

## Tag meanings for this guide

* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.

## Process

1. **ACTION:** Add a `urlpattern` for the app `the_app` to `urlpatterns` in [`the_project/urls.py`](../the_project/urls.py):
    <details>
    <summary>Sample <code>the_project/urls.py</code> contents:</summary>

        from django.urls import include

        urlpatterns = [
            #...
            path('the-app/', include('the_app.urls')),
            #...
        ]
    </details>

1. **ACTION:** Create a URL configuration file for the app `the_app` in directory `the_app` and named `urls.py`:
    * [`the_app/urls.py`](../the_app/urls.py)

1. **ACTION:** Add a `urlpattern` for the home page to `urlpatterns` in [`the_app\urls.py`](../the_app/urls.py):
    1. Add import for [`path`](https://docs.djangoproject.com/en/4.1/ref/urls/#path) from [`django.urls`](https://docs.djangoproject.com/en/4.1/ref/urls/)
    1. Add an `app_name` of `the_app` just above `urlpatterns`.
    1. Add the `path` function to `urlpatterns` with the following arguments:
        * route: `'home/'`
        * view: `views.home`
            * We will create this view function in the next step.
        * name: `'home'`
            <details>
            <summary>Sample <code>the_app/urls.py</code> contents:</summary>

                from django.urls import path

                from . import views

                app_name = 'the_app'
                urlpatterns = [
                    path('home/', views.home, name='home'),
                ]
            </details>

1. **ACTION:** Add a view function `home` to [`the_app/views.py`](../the_app/views.py):
    * Add import of [`HttpResponse`](https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpResponse) from `django.http`
    * Add view function `home` to [`the_app/views.py`](../the_app/views.py)
            <details>
            <summary>Sample <code>the_app/views.py</code> contents:</summary>

                from django.http import HttpResponse

                def home(request):
                    return HttpResponse("Goodbuy, World! Enjoy the sail!")
            </details>

1. **INFO:** The webpage should be ready to display since we have added the following:
    * A URL configured in [`the_app/urls.py`](../the_app/urls.py).
    * A view created in [`the_app/views.py`](../the_app/views.py).
    * A template is not required yet since we are returning an `HttpResponse` without using a template. We will add a template later.

1. **INFO:** Start development server and test web response:
    * `python .\manage.py runserver`

1. **INFO:** Open internet browser to the app `the_app`'s home page URL:
    * <http://localhost:8000/the-app/home/>

1. **INFO:** Verify text displays on home page:
    * Sample text:
        * `Goodbuy, World! Enjoy the sail!`

1. Proceed to [Add Model Functionality](./03_add_model_functionality.md)

## Navigation links

* Back to [Create Basic Django Application](./01_create_basic_django_application.md)
