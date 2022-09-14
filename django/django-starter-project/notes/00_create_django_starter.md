# Create this Django Starter Project

## Resources:

## Code Examples Repository links:
* [Code Examples Repository - `README.md`](../../../README.md)
    * [`examples\`](../../../)
* [Django Code Examples - `README.md`](../../README.md)
    * [`examples\django\`](../../)

## Tag meanings for this guide:
* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.

## Process:
1. **INFO:** Examine current directory structure:
    * `tree /f /a`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\django-starter> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   README.md
            |
            \---notes
                    00_create_django_starter.md
                    00_useful_commands_and_links.md

            PS C:\Users\Bruce\Programming\examples\django\django-starter>
        </details>

1. **INFO:** Directory currently contains `notes` files and a `README.md` file.

1. **ACTION:** Create a `pipenv` virtual environment for the project:
    * We will use a command which will create the virtual environment and also add `django` package to the virtual environment.
    * `pipenv install django==4.0`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\django-starter> pipenv install django==4.0
            Creating a virtualenv for this project...
            Pipfile: C:\Users\Bruce\Programming\examples\django\django-starter\Pipfile
            Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.6) to create virtualenv...
            [====] Creating virtual environment...created virtual environment CPython3.10.6.final.0-64 in 2319ms
              creator CPython3Windows(dest=C:\Users\Bruce\.virtualenvs\django-starter-DkNTxm58, clear=False, no_vcs_ignore=False, global=False)
              seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Bruce\AppData\Local\pypa\virtualenv)
                added seed packages: pip==22.2.2, setuptools==65.0.2, wheel==0.37.1
              activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

            Successfully created virtual environment!
            Virtualenv location: C:\Users\Bruce\.virtualenvs\django-starter-DkNTxm58
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
            PS C:\Users\Bruce\Programming\examples\django\django-starter>
        </details>
    * Note the line with `Virtualenv location`:
        * Sample location:
            * `C:\Users\Bruce\.virtualenvs\django-starter-DkNTxm58`
        * This is the location of the actual virtual environment files:
            * The Python interpreter.
                * TODO: Add path here.
            * The Django package.
                * TODO: Add path here.

1. **INFO:** Examine current directory structure:
    * `tree /f /a`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\django-starter> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   Pipfile
            |   Pipfile.lock
            |   README.md
            |
            \---notes
                    00_create_django_starter.md
                    00_useful_commands_and_links.md

            PS C:\Users\Bruce\Programming\examples\django\django-starter>
        </details>

1. **INFO:** Note addition of `Pipfile` and `Pipfile.lock`:
    * These are the configuration files for the `pipenv` virtual environment.
    * The actual virtual environment executable files are located in the virtual environment directory noted above:
        * `C:\Users\Bruce\.virtualenvs\django-starter-DkNTxm58`

1. **INFO:** We have created the virtual environment, now we need to activate it to use the packages which are installed in the virtual environment. We use a command `pipenv shell` to activate the virtual environment.

1. **ACTION:** Activate the virtual environment:
    * `pipenv shell`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\django-starter> pipenv shell
            Launching subshell in virtual environment...
            PowerShell 7.2.6
            Copyright (c) Microsoft Corporation.

            https://aka.ms/powershell
            Type 'help' to get help.

            PS C:\Users\Bruce\Programming\examples\django\django-starter>
        </details>
    * Note the part:
        * `Launching subshell...`

1. **INFO:** Verify the virtual environment installed packages:
    * `pip list`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\django-starter> pip list
            Package    Version
            ---------- -------
            asgiref    3.5.2
            Django     4.0
            pip        22.2.2
            setuptools 65.0.2
            sqlparse   0.4.2
            tzdata     2022.2
            wheel      0.37.1
            PS C:\Users\Bruce\Programming\examples\django\django-starter>
        </details>

1. **ACTION:** Create a Django Project `the_project`:
    * `django-admin startproject the_project .`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\django-starter> django-admin startproject the_project .
            PS C:\Users\Bruce\Programming\examples\django\django-starter>
        </details>

1. **INFO:** Examine current directory structure:
    * `tree /f /a`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\django-starter-project> tree /f /a
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
            |       00_create_django_starter.md
            |       00_useful_commands_and_links.md
            |       00_use_this_django_starter.md
            |       
            \---the_project
                    asgi.py
                    settings.py
                    urls.py
                    wsgi.py
                    __init__.py
                    
            PS C:\Users\Bruce\Programming\examples\django\django-starter-project>
        </details>

1. **ACTION:** Start development server to test the Django Project:
    * `python .\manage.py runserver`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\django-starter> python .\manage.py runserver
            Watching for file changes with StatReloader
            Performing system checks...

            System check identified no issues (0 silenced).

            You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
            Run 'python manage.py migrate' to apply them.
            September 14, 2022 - 15:43:44
            Django version 4.0, using settings 'the_project.settings'
            Starting development server at http://127.0.0.1:8000/
            Quit the server with CTRL-BREAK.
        </details>

1. **INFO:** Open internet browser to server root:
    * http://localhost:8000/

1. **INFO:** Verify Django Green Rocket and accompanying text:
    * Accompanying text:
        * `The install worked successfully! Congratulations!`

1. **ACTION:** Use \<Ctrl+C\>, while terminal is in focus, to stop the development server.

1. **INFO:** We now have a simple Django Project with pre-configured `pipenv`.



