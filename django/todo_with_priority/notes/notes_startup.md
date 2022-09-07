# Startup Notes for Django Starter Compare

## Information:
* These process steps are being performed in a PowerShell terminal but most commands, I think, are compatible with several other terminal evironments.

## Links:
* [`README.md`](../README.md)

## Useful commands and URL links:
* `python .\manage.py runserver`
* http://localhost:8000/


## Process:

1. Start in root of repository:
    * Sample location:
        * `C:\Users\Bruce\Programming\django-starter-compare\`

1. Examine directory contents. Directory doesn't have any Django files yet:
    * `tree /a /f`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\django-starter-compare> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   .gitignore
            |   LICENSE
            |   README.md
            |
            \---notes
                    notes.md

            PS C:\Users\Bruce\Programming\django-starter-compare>
            ```

1. Create `pipenv` virtual environment for our project and install Django V4.0 package:
    * `pipenv install django==4.0`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\django-starter-compare> pipenv install django==4.0
            Creating a virtualenv for this project...
            Pipfile: C:\Users\Bruce\Programming\django-starter-compare\Pipfile
            Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.6) to create virtualenv...
            [  ==] Creating virtual environment...created virtual environment CPython3.10.6.final.0-64 in 3113ms
            creator CPython3Windows(dest=C:\Users\Bruce\.virtualenvs\django-starter-compare-2tpqlLoP, clear=False, no_vcs_ignore=False, global=False)
            seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Bruce\AppData\Local\pypa\virtualenv)
                added seed packages: pip==22.2.2, setuptools==63.2.0, wheel==0.37.1
            activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

            Successfully created virtual environment!
            Virtualenv location: C:\Users\Bruce\.virtualenvs\django-starter-compare-2tpqlLoP
            Creating a Pipfile for this project...
            Installing django==4.0...
            Adding django to Pipfile's [packages]...
            Installation Succeeded
            Pipfile.lock not found, creating...
            Locking [dev-packages] dependencies...
            Locking [packages] dependencies...

            Resolving dependencies...
            Success!
            Updated Pipfile.lock (036cf0)!
            Installing dependencies from Pipfile.lock (036cf0)...
            ================================ 0/0 - 00:00:00
            To activate this project's virtualenv, run pipenv shell.
            Alternatively, run a command inside the virtualenv with pipenv run.
            PS C:\Users\Bruce\Programming\django-starter-compare>
            ```

1. Note the output line above with `Virtualenv location`. This is where the actual virtual environment files are located.
    * Sample location from above:
        * `Virtualenv location: C:\Users\Bruce\.virtualenvs\django-starter-compare-2tpqlLoP`
    
1. Examine current directory structure:
    * NOTES:
        * Two files have been added after creating the `pipenv` virtual environment. These are the config files for our `pipenv` virtual environment:
            * [`Pipfile`](../Pipfile)
            * [`Pipfile.lock`](../Pipfile.lock)
    * `tree /f /a`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\django-starter-compare> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   .gitignore
            |   LICENSE
            |   Pipfile
            |   Pipfile.lock
            |   README.md
            |
            \---notes
                    notes.md

            PS C:\Users\Bruce\Programming\django-starter-compare>
            ```

1. Activate virtual environment:
    * `pipenv shell`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\django-starter-compare> pipenv shell
            Launching subshell in virtual environment...
            PowerShell 7.2.6
            Copyright (c) Microsoft Corporation.

            https://aka.ms/powershell
            Type 'help' to get help.

            PS C:\Users\Bruce\Programming\django-starter-compare>
            ```

1. Verify Django is installed by checking installed packages:
    * `pip list`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\django-starter-compare> pip list
            Package    Version
            ---------- -------
            asgiref    3.5.2
            Django     4.0
            pip        22.2.2
            setuptools 63.2.0
            sqlparse   0.4.2
            tzdata     2022.2
            wheel      0.37.1
            PS C:\Users\Bruce\Programming\django-starter-compare>
            ```

1. Verify our current terminal session is using the the virtual environment for `python`:
    * `Get-Command python | fl *`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\django-starter-compare> Get-Command python | fl *

            HelpUri            :
            FileVersionInfo    : File:
                                C:\Users\Bruce\.virtualenvs\django-starter-compare-2tpqlLoP\Scripts\python.exe
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

            Path               : C:\Users\Bruce\.virtualenvs\django-starter-compare-2tpqlLoP\Scripts\python.exe
            Extension          : .exe
            Definition         : C:\Users\Bruce\.virtualenvs\django-starter-compare-2tpqlLoP\Scripts\python.exe
            Source             : C:\Users\Bruce\.virtualenvs\django-starter-compare-2tpqlLoP\Scripts\python.exe
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


            PS C:\Users\Bruce\Programming\django-starter-compare>
            ```

1. Note line with `Path`, this is the location of the Python interpreter which is being currently used:
    * Sample line contents:
        * `Path : C:\Users\Bruce\.virtualenvs\django-starter-compare-2tpqlLoP\Scripts\python.exe`

1. Verify our current terminal session is using the the virtual environment for `django-admin`:
    * `Get-Command django-admin | fl *`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\django-starter-compare> Get-Command django-admin | fl *

            HelpUri            :
            FileVersionInfo    : File:
                                C:\Users\Bruce\.virtualenvs\django-starter-compare-2tpqlLoP\Scripts\django-admin.exe
                                InternalName:
                                OriginalFilename:
                                FileVersion:
                                FileDescription:
                                Product:
                                ProductVersion:
                                Debug:            False
                                Patched:          False
                                PreRelease:       False
                                PrivateBuild:     False
                                SpecialBuild:     False
                                Language:

            Path               : C:\Users\Bruce\.virtualenvs\django-starter-compare-2tpqlLoP\Scripts\django-admin.exe
            Extension          : .exe
            Definition         : C:\Users\Bruce\.virtualenvs\django-starter-compare-2tpqlLoP\Scripts\django-admin.exe
            Source             : C:\Users\Bruce\.virtualenvs\django-starter-compare-2tpqlLoP\Scripts\django-admin.exe
            Version            : 0.0.0.0
            Visibility         : Public
            OutputType         : {System.String}
            Name               : django-admin.exe
            CommandType        : Application
            ModuleName         :
            Module             :
            RemotingCapability : PowerShell
            Parameters         :
            ParameterSets      :


            PS C:\Users\Bruce\Programming\django-starter-compare>
            ```

1. Create Django project `the_project`:
    * `django-admin startproject the_project .`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\django-starter-compare> django-admin startproject the_project .
            PS C:\Users\Bruce\Programming\django-starter-compare>
            ```
    
1. Examine current directory structure:
    * NOTES:
        * New [`manage.py`](../manage.py) file added to project root.
        * New [`the_project`](../the_project/) directory (with contents) added to project root:
            * [`asgi.py`](../the_project/asgi.py)
            * [`settings.py`](../the_project/settings.py)
            * [`urls.py`](../the_project/urls.py)
            * [`wsgi.py`](../the_project/wsgi.py)
            * [`__init__.py`](../the_project/__init__.py)
    * `tree /f /a`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\django-starter-compare> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   .gitignore
            |   LICENSE
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

            PS C:\Users\Bruce\Programming\django-starter-compare>
            ```

1. Test development server:
    * `python .\manage.py runserver`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\django-starter-compare> python .\manage.py runserver
            Watching for file changes with StatReloader
            Performing system checks...

            System check identified no issues (0 silenced).

            You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
            Run 'python manage.py migrate' to apply them.
            August 26, 2022 - 08:16:43
            Django version 4.0, using settings 'the_project.settings'
            Starting development server at http://127.0.0.1:8000/
            Quit the server with CTRL-BREAK.
            ```

1. Open internet browser to server address:
    * NOTES:
        * Author is using http://localhost:8000/ since since it usually maps to http://127.0.0.1:8000/ and is easier to link in notes.
    * http://localhost:8000/

1. Verify presence of Django Green Rocket and some text like the following:
    * Sample text:
        * `The install worked successfully! Congratulations!`
    * Sample image:
        * INSERT_DJANGO_GREEN_ROCKET_IMAGE_HERE

1. Stop the development server:
    * Keystroke, in terminal:
        * `<Ctrl+C>`

1. Create Django app:
    * `python .\manage.py startapp the_app`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\django-starter-compare> python .\manage.py startapp the_app
            PS C:\Users\Bruce\Programming\django-starter-compare>
            ```

1. Examine current directory structure:
    * NOTES:
        * New [`the_app`](../the_app/) directory (with contents) added to project root:
            * [`admin.py`](../the_app/admin.py)
            * [`apps.py`](../the_app/apps.py)
            * [`models.py`](../the_app/models.py)
            * [`tests.py`](../the_app/tests.py)
            * [`views.py`](../the_app/views.py)
            * [`__init__.py`](../the_app/__init__.py)
            * [`migrations`](../the_app/migrations/)
                * [`__init__.py`](../the_app/migrations/__init__.py)
        * New `db.sqlite3` shows up now since we started the development server in an earlier step.
    * `tree /f /a`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\django-starter-compare> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   .gitignore
            |   db.sqlite3
            |   LICENSE
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

            PS C:\Users\Bruce\Programming\django-starter-compare>
            ```

1. Add an entry for the `AppConfig` of our app `the_app` to the `INSTALLED_APPS` part of [`the_project/settings.py`](../the_project/settings.py):
    <details>
    <summary>Sample addition to <code>INSTALLED_APPS</code> implementation:</summary>

        INSTALLED_APPS = [
            #...
            'the_app.apps.TheAppConfig',
            #...
        ]
    </details>

1. This concludes the creation of the Django Starter Compare. This repo can be used to compare the state of a project that has had application functionality added.
