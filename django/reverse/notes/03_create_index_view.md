# 03 - Create Index View
* This project's directory: [`reverse/`](./../)

## Resources:
* [`path()`](https://docs.djangoproject.com/en/4.1/ref/urls/#path)
* [`include()`](https://docs.djangoproject.com/en/4.1/ref/urls/#include)


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


### Add Application URL Configuration File:
1. **ACTION:** Create a application URL configuration file [`the_app/urls.py`](../the_app/urls.py):
    1. Import [`path`](https://docs.djangoproject.com/en/4.1/ref/urls/#path) from `django.urls`.
    1. Import [`TemplateView`](https://docs.djangoproject.com/en/4.1/ref/class-based-views/base/#django.views.generic.base.TemplateView) from `django.views.generic.base`.
    1. Add an attribute `app_name`:
        * `app_name = 'the_app'`
    1. Add an attribute `urlpatterns`, which is a list of `urlpattern`s.
    1. Add a `path()` to the `urlpatterns` attribute:
        * This `path()` function will have the following arguments:
            * route: `''`
            * view: `TemplateView.as_view(template_name='index.html')`
            * name: `name='index'`

    <details>
    <summary>Sample <code>the_app/urls.py</code> contents:</summary>

        from django.urls import path
        from django.views.generic.base import TemplateView

        app_name = 'the_app'
        urlpatterns = [
            path('', TemplateView.as_view(template_name='index.html'), name='index'),
        ]
    </details>

1. **INFO:** When the user sends an HTTP request to the server root, the `urlpattern` we created above will call a view function, via the `TemplateView` class' function [`as_view()`](https://docs.djangoproject.com/en/4.1/ref/class-based-views/base/#django.views.generic.base.View.as_view), and render the [`the_app/templates/index.html`](../the_app/templates/index.html) template.


### Django will Provide the Application View Function:
1. **INFO:** The Django class [`TemplateView`](https://docs.djangoproject.com/en/4.1/ref/class-based-views/base/#django.views.generic.base.TemplateView) and it's function [`as_view()`](https://docs.djangoproject.com/en/4.1/ref/class-based-views/base/#django.views.generic.base.View.as_view) will handle the view function for us. We don't need to create our own view function:


### Add Application Template:
1. **ACTION:** Create a [`templates`](../the_app/templates/) directory.
1. **ACTION:** Add a template [`index.html`](../the_app/templates/index.html) to the [`templates`](../the_app/templates/) directory:
    <details>
    <summary>Sample <code>index.html</code> contents:</summary>

        <h1>Goodbuy, World! Enjoy the Sale!</h1>
    </details>

1. **INFO:** Proceed to [Use Django's `reverse` Function](./04_use_djangos_reverse_function.md)

## Repository Links:
* Back to [Create Django Application](./02_create_django_application.md)