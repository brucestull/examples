# Demonstrate `reverse()` Method
* Demonstrate how Django `reverse()` works.

## Resources:
* [`django.urls`](https://docs.djangoproject.com/en/4.1/ref/urlresolvers/#module-django.urls)
* [reverse()](https://docs.djangoproject.com/en/4.1/ref/urlresolvers/#reverse)

## Code Examples Repository links:
* [Code Examples Repository](../../../README.md)
* [Django Code Examples](../../README.md)

## Tag meanings for this guide:
* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.

## Process:
1. Start in the directory [`reverse`](../../reverse/) which contains the code from [Django Starter](../../django-starter/README.md):
    * **TODO:** Add [instructions](https://github.com/brucestull/examples/issues/41#issue-1368891990) to 'copy' the code for `django-starter` to this directory.
    * Sample directory location:
        * `C:\Users\Bruce\Programming\examples\django\reverse\`

1. Examine directory structure:
    * These are the directories and files created by the [Django starter](../../django-starter/README.md) in the directory [`examples/django/django-starter/`](../../django-starter/)
    * `tree /f /a`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   manage.py
            |   Pipfile
            |   Pipfile.lock
            |   README.md
            |
            +---notes
            |       commands_and_links.md
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

            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>

1. Proceed to [Create a New `pipenv` Virtual Environment for the Project](./01_create_virtual_environment.md)




