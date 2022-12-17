# 04 - Use Django's `reverse` Function

* This project's directory: [`reverse/`](./../)

## Resources

* [`reverse()`](https://docs.djangoproject.com/en/4.1/ref/urlresolvers/#reverse)

## Code Examples Repository links

* [Code Examples Repository - README.md](../../../README.md)
  * [`examples/`](../../../)
* [Django Code Examples - README.md](../../README.md)
  * [`examples/django/`](../../)

## Tag meanings for this guide

* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.

## Process

1. **INFO:** Everything up until this point has been to set up a project so we can use Django's [`reverse()`](https://docs.djangoproject.com/en/4.1/ref/urlresolvers/#reverse) function.
    * To demonstrate the `reverse()` function we will first use a Python print statement inside the `index` view function to display the results of the `reverse()` function.
    * The `reverse()` function is like any other Python function. We can call it and then process the returned value (object).
    * The `reverse()` function returns a URL.

1. Add a print statement of the [`reverse()`](https://docs.djangoproject.com/en/4.1/ref/urlresolvers/#reverse) function to the `index` view function in [`the_app/views.py`](../the_app/views.py):
    * We add the following arguments to the `reverse()` function:
        * viewname: `'the_app:index'`

## Repository Links

* Back to [Create Index View](./03_create_index_view.md)
