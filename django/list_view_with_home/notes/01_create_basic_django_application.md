# Create Basic Django Application

## Assumptions:
* User has functional `python` installation.
* User has functional `pip` installation.
* User has functional `pipenv` installation.
* User is familiar with terminal and shell commands.

## Resources:
* [Django Quick Start Guide (PDXCG Style)](https://github.com/PdxCodeGuild/class_otter/blob/main/3%20Django/docs/Django%20Project%20Setup.md)

## Repository Links:
* [Examples Repository](../../../README.md)
* [List View with Home - `README.me`](../README.md)

## Tag meanings for this guide:
* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.

## Process:
1. **ACTION:** Start in the project root directory:
    * Sample root directory:
        * `C:\Users\Bruce\Programming\examples\django\list_view_with_home`

1. **ACTION:** Create a `pipenv` virtual environment for the application and install Django 4.0:
    * `pipenv install django==4.0`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_view_with_home> pipenv install django==4.0
            Creating a virtualenv for this project...
            Pipfile: C:\Users\Bruce\Programming\examples\django\list_view_with_home\Pipfile
            Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.6) to create virtualenv...
            [==  ] Creating virtual environment...created virtual environment CPython3.10.6.final.0-64 in 2410ms
            creator CPython3Windows(dest=C:\Users\Bruce\.virtualenvs\list_view_with_home-OkoCrdxY, clear=False, no_vcs_ignore=False, global=False)
            seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Bruce\AppData\Local\pypa\virtualenv)
                added seed packages: pip==22.2.2, setuptools==63.4.3, wheel==0.37.1
            activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

            Successfully created virtual environment!
            Virtualenv location: C:\Users\Bruce\.virtualenvs\list_view_with_home-OkoCrdxY
            Creating a Pipfile for this project...
            Installing django==4.0...
            Adding django to Pipfile's [packages]...
            Installation Succeeded
            Pipfile.lock not found, creating...
            Locking [dev-packages] dependencies...
            Locking [packages] dependencies...
                    Building requirements...
            Resolving dependencies...
            Success!
            Updated Pipfile.lock (036cf0)!
            Installing dependencies from Pipfile.lock (036cf0)...
            ================================ 0/0 - 00:00:00
            To activate this project's virtualenv, run pipenv shell.
            Alternatively, run a command inside the virtualenv with pipenv run.
            PS C:\Users\Bruce\Programming\examples\django\list_view_with_home>
        </details>

1. **ACTION:** Activate this project's virtual environment:
    * `pipenv shell`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_view_with_home> pipenv shell
            Launching subshell in virtual environment...
            PowerShell 7.2.6
            Copyright (c) Microsoft Corporation.

            https://aka.ms/powershell
            Type 'help' to get help.

            PS C:\Users\Bruce\Programming\examples\django\list_view_with_home>
        </details>

1. **ACTION:** Create a new Django project (site root):
    * `django-admin startproject the_project .`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_view_with_home> django-admin startproject the_project .
            PS C:\Users\Bruce\Programming\examples\django\list_view_with_home>
        </details>

1. **INFO:** Examine directory structure:
    * `tree /f /a`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_view_with_home> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   manage.py
            |   Pipfile
            |   Pipfile.lock
            |   README.md
            |
            +---notes
            |       create_basic_django_application.md
            |
            \---the_project
                    asgi.py
                    settings.py
                    urls.py
                    wsgi.py
                    __init__.py

            PS C:\Users\Bruce\Programming\examples\django\list_view_with_home>
        </details>

1. **ACTION:** Start the development server:
    * `python .\manage.py runserver`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_view_with_home> python .\manage.py runserver
            Watching for file changes with StatReloader
            Performing system checks...

            System check identified no issues (0 silenced).

            You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
            Run 'python manage.py migrate' to apply them.
            September 03, 2022 - 08:46:04
            Django version 4.0, using settings 'the_project.settings'
            Starting development server at http://127.0.0.1:8000/
            Quit the server with CTRL-BREAK.
        </details>

1. **ACTION:** Open internet browser to local server root:
    * http://localhost:8000/

1. **ACTION:** Verify page load:
    * Note the Django Green Rocket image and accompanying text.

1. **ACTION:** Stop server by using \<Ctrl+C\>.

1. **ACTION:** Add a Django application to the project:
    * `python .\manage.py startapp the_app`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_view_with_home> python .\manage.py startapp the_app
            PS C:\Users\Bruce\Programming\examples\django\list_view_with_home>
        </details>

1. **INFO:** Examine directory structure:
    * `tree /f /a`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\list_view_with_home> tree /f /a
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
            |       create_basic_django_application.md
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

            PS C:\Users\Bruce\Programming\examples\django\list_view_with_home>
        </details>

1. **ACTION:** Add the new application's configuration `TheAppConfig` in [`the_app/apps.py`](../the_app/apps.py) to `INSTALLED_APPS` in [`the_project/settings.py`](../the_project/settings.py)
    <details>
    <summary>Sample <code>the_project/settings.py</code> contents:</summary>

        INSTALLED_APPS = [
            ...
            'the_app.apps.TheAppConfig',
            ...
        ]
    </details>

1. **INFO:** Test development server one more time:
    * `python .\manage.py runserver`
    * http://localhost:8000/

1. Proceed to [Add Home Page with String](./02_home_page_with_string.md) to continue building the application.