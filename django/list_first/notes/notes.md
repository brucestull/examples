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
    * `python .\manage.py createsuperuser`

## Resources:
* **TODO**: LINK_TO_PIPENV_DOCUMENTATION

## Tag meanings for this guide:
* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info and not necessarily functional or code changes.

## Process:
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