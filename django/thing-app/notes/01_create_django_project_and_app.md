# Create Django Project and Application

## Resources:

## Process:

1. Current directory contents. We already have a `notes` directory for notes and `Pipfile` and `Pipfile.lock` files for our virtual environment:
    * `tree /f /a`:
        ```
        PS C:\Users\Bruce\Programming\examples\django\thing-app> tree /f /a
        Folder PATH listing for volume OS
        Volume serial number is CC00-DD12
        C:.
        |   Pipfile
        |   Pipfile.lock
        |   
        \---notes
                00_commands_and_links.md
                01_create_django_project_and_app.md
                
        PS C:\Users\Bruce\Programming\examples\django\thing-app>
        ```

1. Create a Django project:
    * `django-admin startproject the_project .`

1. Create a Django application:
    * `python .\manage.py startapp the_app`

1. Current directory structure:
    * `tree /f /a`:
        ```
        PS C:\Users\Bruce\Programming\examples\django\thing-app> tree /f /a
        Folder PATH listing for volume OS
        Volume serial number is CC00-DD12
        C:.
        |   manage.py
        |   Pipfile
        |   Pipfile.lock
        |
        +---notes
        |       00_commands_and_links.md
        |       01_create_django_project_and_app.md
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
        
        PS C:\Users\Bruce\Programming\examples\django\thing-app>
        ```