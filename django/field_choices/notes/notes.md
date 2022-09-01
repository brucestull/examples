# Django Fields Choices

## Links:
* Repository [`README.md`](../../../README.md)

## Meaning of tags on steps:
* **ACTION: **  - A step that is performing some functional task.
* **INFO: **    - A step that is providing information.

## Commands we will use:

## Process:

1. Start in directory which is the root of the Django project.

1. Create `pipenv` virtual environment and install Django V4.0:
    * Here is a list of a few `pipenv` commands:
        * Create `pipenv` virtual environment and add Django 4.0.
            * `pipenv install django==4.0`
        * Create `pipenv` virtual environment without adding any additional packages right now.
            * `pipenv install`
    * `pipenv install django==4.0`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices> pipenv install django==4.0
            Creating a virtualenv for this project...
            Pipfile: C:\Users\Bruce\Programming\examples\django\django_field_choices\Pipfile
            Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.6) to create virtualenv...
            [    ] Creating virtual environment...created virtual environment CPython3.10.6.final.0-64 in 467ms
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
            Locking...
            Resolving dependencies...
            Success!
            Updated Pipfile.lock (036cf0)!
            Installing dependencies from Pipfile.lock (036cf0)...
            ================================ 0/0 - 00:00:00
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices>
            ```

1. Activate virtual environment:
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

1. Examine installed packages:
    * Note presence of `Django`.
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

1. Create Django project:
    * `django-admin startproject the_project .`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices> django-admin startproject the_project .
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices>
            ```

1. Examine directory structure:
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

1. Start development server:
    * `python .\manage.py runserver`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices> python .\manage.py runserver
            Watching for file changes with StatReloader
            Performing system checks...

            System check identified no issues (0 silenced).

            You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
            Run 'python manage.py migrate' to apply them.
            August 25, 2022 - 20:50:57
            Django version 4.0, using settings 'the_project.settings'
            Starting development server at http://127.0.0.1:8000/
            Quit the server with CTRL-BREAK.
            ```

1. Open internet browser to the Django application page:
    * http://localhost:8000/

1. Verify Django Green Rocket and following text and lots of other stuff:
    * `The install worked successfully! Congratulations!`

1. Create Django app:
    * `python .\manage.py startapp the_app`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices> python .\manage.py startapp the_app
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices>
            ```

1. Examine directory structure:
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

1. Create `NameWithChoices` model in [`the_app/models.py`](../the_app/models.py):
