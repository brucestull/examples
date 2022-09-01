# Create Django Project with List View First
* The intent is to show that it can be useful for create the Django List View first so user can see the models presented on the page and then add links to the other pages, templates, and views.
    1. Might expand this later to use `if request.method==POST` and `if request.method==GET` somewhere.
    1. For now, create a simple template with a list as a `home` or `list` page.

## Project Links and Commands:
* [Issue Link #20](https://github.com/brucestull/examples/issues/20)

* Commands:
    * `pipenv install django==4.0`
    * `pipenv shell`
    * `pip list`
    * `django-admin startproject the_project .`
    * `tree /f /a`
    * `python .\manage.py runserver`
    * `python .\manage.py startapp the_app`
    * `python .\manage.py createsuperuser`

* Development server web links:
    * http://localhost:8000/
    * http://localhost:8000/admin/

## Resources:
* **TODO**: LINK_TO_PIPENV_EXAMPLE_DOCUMENTATION

## Tag meanings for this guide:
* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info and not necessarily functional or code changes.

## Process:

### Create Django skeleton:

1. Start in the directory which will contain our Django project:
    * Sample directory location:
        * `C:\Users\Bruce\Programming\examples\django\list_first`
1. **ACTION:** Create `pipenv` virtual environment:
    * `pipenv install django==4.0`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_first> pipenv install django==4.0
            Creating a virtualenv for this project...
            Pipfile: C:\Users\Bruce\Programming\examples\django\list_first\Pipfile
            Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.6) to create virtualenv...
            [   =] Creating virtual environment...created virtual environment CPython3.10.6.final.0-64 in 429ms
            creator CPython3Windows(dest=C:\Users\Bruce\.virtualenvs\list_first-KAifsCX6, clear=False, no_vcs_ignore=False, global=False)
            seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Bruce\AppData\Local\pypa\virtualenv)
                added seed packages: pip==22.2.2, setuptools==63.4.3, wheel==0.37.1
            activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

            Successfully created virtual environment!
            Virtualenv location: C:\Users\Bruce\.virtualenvs\list_first-KAifsCX6
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
            PS C:\Users\Bruce\Programming\examples\django\list_first>
        </details>

1. **ACTION:** Activate `pipenv` virtual environment:
    * `pipenv shell`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_first> pipenv shell
            Launching subshell in virtual environment...
            PowerShell 7.2.6
            Copyright (c) Microsoft Corporation.

            https://aka.ms/powershell
            Type 'help' to get help.

            PS C:\Users\Bruce\Programming\examples\django\list_first>
        </details>

1. **INFO:** Verify we have Django installed:
    * `pip list`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_first> pip list
            Package    Version
            ---------- -------
            asgiref    3.5.2
            Django     4.0
            pip        22.2.2
            setuptools 63.4.3
            sqlparse   0.4.2
            tzdata     2022.2
            wheel      0.37.1
            PS C:\Users\Bruce\Programming\examples\django\list_first>
        </details>

1. **ACTION:** Create Django project:
    * `django-admin startproject the_project .`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_first> django-admin startproject the_project .
            PS C:\Users\Bruce\Programming\examples\django\list_first>
        </details>

1. **INFO:** Examine directory structure:
    * `tree /f /a`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_first> tree /f /a
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

            PS C:\Users\Bruce\Programming\examples\django\list_first>
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

            PS C:\Users\Bruce\Programming\examples\django\list_first> python .\manage.py startapp the_app
            PS C:\Users\Bruce\Programming\examples\django\list_first>
        </details>

1. **INFO:** Examine directory structure:
    * `tree /f /a`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_first> tree /f /a
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

            PS C:\Users\Bruce\Programming\examples\django\list_first>
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


### Create `index` page:

1. Create [the_app/urls.py](../the_app/urls.py) and add URL route for the `index_view` view to it:
    * Import `path` from `django.urls`.
    * Add our `app_name`, `the_app`.
    * Add `path()` to `urlpatterns`.

1. Add view function `index_view` to [`the_app/views.py`](../the_app/views.py):
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

1. Test development server to ensure our view function is working:
    * Server address:
        * http://localhost:8000/
    * route:
        * `the-app/index/`
    * View function:
        * `index`
