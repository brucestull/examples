# Django Field Choices

## Django commands and server links:
* `python .\manage.py runserver`
* http://localhost:8000/
* http://localhost:8000/admin/
* http://localhost:8000/the-app/
* http://localhost:8000/the-app/no-choices/
* http://localhost:8000/the-app/yes-choices/
* http://localhost:8000/the-app/no-choices/new/
* http://localhost:8000/the-app/yes-choices/new/


## Process:
1. Create `pipenv` virtual environment and install Django V4.0:
    * `pipenv install django==4.0`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices> pipenv install django==4.0
            Creating a virtualenv for this project...
            Pipfile: C:\Users\Bruce\Programming\examples\django\django_field_choices\Pipfile
            Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.6) to create virtualenv...
            [  ==] Creating virtual environment...created virtual environment CPython3.10.6.final.0-64 in 3090ms
            creator CPython3Windows(dest=C:\Users\Bruce\.virtualenvs\django_field_choices-3K9AxgPs, clear=False, no_vcs_ignore=False, global=False)
            seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Bruce\AppData\Local\pypa\virtualenv)
                added seed packages: pip==22.2.2, setuptools==63.2.0, wheel==0.37.1
            activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

            Successfully created virtual environment!
            Virtualenv location: C:\Users\Bruce\.virtualenvs\django_field_choices-3K9AxgPs
            Creating a Pipfile for this project...
            Installing django==4.0...
            Adding django to Pipfile's [packages]...
            Installation Succeeded
            Pipfile.lock not found, creating...
            Locking [dev-packages] dependencies...
            Locking [packages] dependencies...
            Locking...Building requirements...
            Resolving dependencies...
            Success!
            Updated Pipfile.lock (036cf0)!
            Installing dependencies from Pipfile.lock (036cf0)...
            ================================ 0/0 - 00:00:00
            To activate this project's virtualenv, run pipenv shell.
            Alternatively, run a command inside the virtualenv with pipenv run.
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices>
            ```

1. Activate `pipenv` virtual environment:
    * `pipenv shell`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices> pipenv shell
            Launching subshell in virtual environment...
            PowerShell 7.2.6
            Copyright (c) Microsoft Corporation.

            https://aka.ms/powershell
            Type 'help' to get help.

            PS C:\Users\Bruce\Programming\examples\django\django_field_choices>
            ```
    * Note from the output above:
        * `Launching subshell in virtual environment...`

1. Verify installed packages (which should include Django):
    * `pip list`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices> pip list
            Package    Version
            ---------- -------
            asgiref    3.5.2
            Django     4.0
            pip        22.2.2
            setuptools 63.2.0
            sqlparse   0.4.2
            tzdata     2022.2
            wheel      0.37.1
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices>
            ```

1. Verify the current Python interpreter:
    * `Get-Command python | fl *`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices> Get-Command python | fl *

            HelpUri            :
            FileVersionInfo    : File:
                                C:\Users\Bruce\.virtualenvs\django_field_choices-3K9AxgPs\Scripts\python.exe
                                InternalName:     Python Launcher
                                OriginalFilename: py.exe
                                FileVersion:      3.10.6
                                FileDescription:  Python
                                Product:          Python
                                ProductVersion:   3.10.6
                                Debug:            False
                                Patched:          False
                                PreRelease:       False
                                PrivateBuild:     False
                                SpecialBuild:     False
                                Language:         Language Neutral

            Path               : C:\Users\Bruce\.virtualenvs\django_field_choices-3K9AxgPs\Scripts\python.exe
            Extension          : .exe
            Definition         : C:\Users\Bruce\.virtualenvs\django_field_choices-3K9AxgPs\Scripts\python.exe
            Source             : C:\Users\Bruce\.virtualenvs\django_field_choices-3K9AxgPs\Scripts\python.exe
            Version            : 3.10.6150.1013
            Visibility         : Public
            OutputType         : {System.String}
            Name               : python.exe
            CommandType        : Application
            ModuleName         :
            Module             :
            RemotingCapability : PowerShell
            Parameters         :
            ParameterSets      :


            PS C:\Users\Bruce\Programming\examples\django\django_field_choices>
            ```
    * Note line with Python interpeter path. It's the version inside our virtual environment:
        ```
        Path : C:\Users\Bruce\.virtualenvs\django_field_choices-3K9AxgPs\Scripts\python.exe
        ```

1. Create Django project skeleton:
    * `django-admin startproject the_project .`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices> django-admin startproject the_project .
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices>
            ```

1. Verify directory structure:
    * `tree /f /a`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices> tree /f /a
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

            PS C:\Users\Bruce\Programming\examples\django\django_field_choices>
            ```

1. Test development server:
    * `python .\manage.py runserver`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices> python .\manage.py runserver
            Watching for file changes with StatReloader
            Performing system checks...

            System check identified no issues (0 silenced).

            You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
            Run 'python manage.py migrate' to apply them.
            August 25, 2022 - 07:45:49
            Django version 4.0, using settings 'the_project.settings'
            Starting development server at http://127.0.0.1:8000/
            Quit the server with CTRL-BREAK.
            ```

1. Open internet browser to development server address:
    * http://localhost:8000/

1. Verify Django Green Rocket with "The install worked successfully! Congratulations!" text.

1. Add a Django app:
    * `python .\manage.py startapp the_app`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices> python .\manage.py startapp the_app
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices>
            ```

1. Verify directory structure:
    * `tree /f /a`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices> tree /f /a
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

            PS C:\Users\Bruce\Programming\examples\django\django_field_choices>
            ```

1. Add the `TheAppConfig` from [`the_app/apps.py`](../the_app/apps.py) of our app `the_app` to `INSTALLED_APPS` in [`the_project/settings.py`](../the_project/settings.py):
    * Sample changes:
        ```
        INSTALLED_APPS = [
            ...
            'the_app.apps.TheAppConfig',
            ...
        ]
        ```

1. We're going to create a simple view to verify connection of all the things.

1. Add a `URLPattern` for our app `the_app` to [`the_project\urls.py`](../the_project/urls.py):
    * Import `include` from `django.urls`.
    * Add `path` function with following arguments to `urlpatterns`:
        * `route`: `the-app/`
        * `view`: `include('the_app.urls')`
    * Sample content:
        ```
        from django.urls import include

        urlpatterns = [
            ...
            path('the-app/', include('the_app.urls')),
            ...
        ]
        ```

1. Create a `URLconf` [`the_app/urls.py`](../the_app/urls.py) with following contents:
    ```
    from django.urls import path
    from . import views


    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ```

1. Create a function-based view `index` in [`the_app/views.py`](../the_app/views.py):
    * Add import for `render` from `django.shortcuts`.
    * Add import for `HttpResponse` from `django.http`.
    * Add view function `index`.
        ```
        from django.shortcuts import render
        from django.http import HttpResponse


        def index(request):
            return_string = "Can you see me now?"
            return HttpResponse(return_string)
        ```

1. Test app `the_app`'s url in internet browser:
    * `python .\manage.py runserver`
    * http://localhost:8000/the-app/

1. Add import for `models` from `django.db` and create models `NoChoices`and `YesChoices` to [`the_app/models.py`](../the_app/models.py)
    ```
    from django.db import models


    class NoChoices(models.Model):
        name = models.CharField(max_length=20)

        def __str__(self):
            return self.name


    class YesChoices(models.Model):
        name = models.CharField(max_length=20)

        def __str__(self):
            return self.name
    ```

1. Add `NoChoicesListView` to `YesChoicesListView` in [`the_app/view.py`](../the_app/views.py):
    ```
    class NoChoicesListView(ListView):
        model = NoChoices


    class YesChoicesListView(ListView):
        model = YesChoices
    ```





## TESTING OUT CLASS-BASED VIEWS

1. Import and add `admin.site.register` of `NoChoices` and `YesChoices` models to [`the_app/admin.py`](../the_app/admin.py):
    ```
    from django.contrib import admin

    from .models import NoChoices, YesChoices

    admin.site.register(NoChoices)
    admin.site.register(YesChoices)
    ```

1. `python .\manage.py makemigrations`
1. `python .\manage.py migrate`

1. Install [The Django admin documentation generator](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/admindocs/#module-django.contrib.admindocs)
    * `pipenv install docutils==0.19`

