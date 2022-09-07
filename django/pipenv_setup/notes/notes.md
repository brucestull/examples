# Create `pipenv` Virtual Environment for a Django Project

## Resources:
* [Pipenv: Python Development Workflow for Humans - pypi.org](https://pypi.org/project/pipenv/)
* [Installing Pipenv - python-guide.org](https://docs.python-guide.org/dev/virtualenvs/#installing-pipenv)
* [Pipenv: A Guide to the New Python Packaging Tool - realpython.com](https://realpython.com/pipenv-guide/)
* [Pipenv: Python Dev Workflow for Humans - pipenv.pypa.io](https://pipenv.pypa.io/en/latest/)
* [Why use `pipenv`?](https://pipenv.pypa.io/en/latest/#pipenv-features)

## Repository Links:
* [Examples Repository](../../../README.md)
* [Create `pipenv` virtual environment for a Django project - `README.me`](../README.md)

## Things user should know how to do before doing this activity:
* **TODO:** 

## Things user will learn from this activity:
* **TODO:** Need to describe what a `pipenv` virtual environment is. May actually just add a link to some great description when I find it.

## Things user will do during this activity:
1. Create `pipenv` virtual environment for their Django project.
1. Install `django` package in the virtual environment.
1. Activate the `pipenv` virtual environment so their Django app uses the appropriate Django version.
1. Create basic Django skeleton.
1. Test out development server.

## Assumptions and Requirements:
* User has functioning `pipenv` install.
* User has functioning `python` install.
* These commands should work for most terminal environments. The author is using PowerShell.

## Tag meanings for this guide:
* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info and not necessarily functional or code changes.

## Process:

1. **ACTION:** Open terminal in the parent directory which will contain the directory for our Django app:
    * Sample location:
        * `C:\Users\Bruce\Programming\examples\django`

1. **ACTION:** Create directory for our Django app:
    * Sample directory:
        * `C:\Users\Bruce\Programming\examples\django\django_pipenv_setup`

1. **ACTION:** Change directory into our Django app's directory:
    * `cd .\django_pipenv_setup\`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django> cd .\django_pipenv_setup\                         
            PS C:\Users\Bruce\Programming\examples\django\django_pipenv_setup>
        </details>

1. **ACTION:** Create `pipenv` virtual environment for our Django app:
    * NOTES:
        * Command to create `pipenv` without installing any packages:
            * `pipenv install`
        * Command to create `pipenv` and install latest Django version:
            * `pipenv install django`
        * Command to create `pipenv` and install our preferred Django version:
            * `pipenv install django==<OUR_FAVORITE_VERSION>`
        * This guide is choosing Django version 4.0 as our `<OUR_FAVORITE_VERSION>`.
    * `pipenv install django==4.0`

        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\django_pipenv_setup> pipenv install django==4.0
            Creating a virtualenv for this project...
            Pipfile: C:\Users\Bruce\Programming\examples\django\django_pipenv_setup\Pipfile
            Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.6) to create virtualenv...
            [  ==] Creating virtual environment...created virtual environment CPython3.10.6.final.0-64 in 376ms
            creator CPython3Windows(dest=C:\Users\Bruce\.virtualenvs\django_pipenv_setup-KgMRvH_5, clear=False, no_vcs_ignore=False, global=False)
            seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Bruce\AppData\Local\pypa\virtualenv)
                added seed packages: pip==22.2.2, setuptools==63.2.0, wheel==0.37.1
            activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

            Successfully created virtual environment!
            Virtualenv location: C:\Users\Bruce\.virtualenvs\django_pipenv_setup-KgMRvH_5
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
            PS C:\Users\Bruce\Programming\examples\django\django_pipenv_setup>
        </details>

1. **ACTION:** Activate the `pipenv` virtual environment:
    * NOTE: If terminal session already has virtual environment active, the console output will provide that info:
    * `pipenv shell`

        <details>
        <summary>Sample output when a new `subshell` is launched:</summary>

            PS C:\Users\Bruce\Programming\examples\django\django_pipenv_setup> pipenv shell
            Launching subshell in virtual environment...
            PowerShell 7.2.6
            Copyright (c) Microsoft Corporation.

            https://aka.ms/powershell
            Type 'help' to get help.

            PS C:\Users\Bruce\Programming\examples\django\django_pipenv_setup>
        </details>

        <details>
        <summary>Sample output when virtual environment is `already activated`:</summary>

            PS C:\Users\Bruce\Programming\examples\django\django_pipenv_setup> pipenv shell
            Shell for C:\Users\Bruce\.virtualenvs\django_pipenv_setup-KgMRvH_5 already activated.
            No action taken to avoid nested environments.
            PS C:\Users\Bruce\Programming\examples\django\django_pipenv_setup>
        </details>        

1. **INFO:** List installed packages of the virtual environment:
    * `pip list`

        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\django_pipenv_setup> pip list
            Package    Version
            ---------- -------
            asgiref    3.5.2
            Django     4.0
            pip        22.2.2
            setuptools 63.2.0
            sqlparse   0.4.2
            tzdata     2022.2
            wheel      0.37.1
            PS C:\Users\Bruce\Programming\examples\django\django_pipenv_setup>
        </details>

1. **INFO:** Inspect directory structure:
    * `tree /a /f`

        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\django_pipenv_setup> tree /a /f
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   Pipfile
            |   Pipfile.lock
            |
            \---notes
                    notes.md

            PS C:\Users\Bruce\Programming\examples\django\django_pipenv_setup>
        </details>

1. **ACTION:** Create Django project skeleton:
    * `django-admin startproject the_project .`

        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\django_pipenv_setup> django-admin startproject the_project .
            PS C:\Users\Bruce\Programming\examples\django\django_pipenv_setup>
        </details>

1. **INFO:** Inspect directory structure. We now have the Django-produced skeleton code for our project:
    * `tree /a /f`

        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\django_pipenv_setup> tree /a /f
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   manage.py
            |   Pipfile
            |   Pipfile.lock
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

            PS C:\Users\Bruce\Programming\examples\django\django_pipenv_setup>
        </details>

1. **INFO:** Test development server:
    1. `python .\manage.py runserver`

        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\django\django_pipenv_setup> python .\manage.py runserver
            Watching for file changes with StatReloader
            Performing system checks...

            System check identified no issues (0 silenced).

            You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
            Run 'python manage.py migrate' to apply them.
            August 24, 2022 - 10:23:18
            Django version 4.0, using settings 'the_project.settings'
            Starting development server at http://127.0.0.1:8000/
            Quit the server with CTRL-BREAK.
        </details>
    1. Open web browser:
        * http://localhost:8000/
    1. Verify the Django Green Rocket is visible and following text shows:
        * `The install worked successfully! Congratulations!`

1. **ACTION:** Proceed to adding code functionality for your Django application.
