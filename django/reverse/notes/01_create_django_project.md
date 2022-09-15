# 01 - Create Django Project


## Resources:
* [Writing your first Django app, part 1 - docs.djangoproject.com](https://docs.djangoproject.com/en/4.0/intro/tutorial01/#writing-your-first-django-app-part-1)
* [Django Tutorial Part 2: Creating a skeleton website - developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website)


## Code Examples Repository links:
* [Code Examples Repository - README.md](../../../README.md)
    * [`examples/`](../../../)
* [Django Code Examples - README.md](../../README.md)
    * [`examples/django/`](../../)


## Tag meanings for this guide:
* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.


## Process:
1. **ACTION:** Start in project root, where the `pipenv` configuration files (`Pipfile`, `Pipfile.lock`) are located:
    * Sample location:
        * `C:\Users\Bruce\Programming\examples\django\reverse\`

1. **ACTION:** Activate the virtual environment:
    * `pipenv shell`
        <details>
        <summary>Sample output with launch of subshell:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> pipenv shell
            Launching subshell in virtual environment...
            PowerShell 7.2.6
            Copyright (c) Microsoft Corporation.

            https://aka.ms/powershell
            Type 'help' to get help.

            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>

        <details>
        <summary>Sample output when virtual environment already activated:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> pipenv shell
            Shell for C:\Users\Bruce\.virtualenvs\reverse-gikyn-XH already activated.
            No action taken to avoid nested environments.
            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>

1. **INFO:** Verify we are using the virtual environment packages by checking the location of the current Python interpreter:
    * `Get-Command python | Format-List *`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> Get-Command python | Format-List *

            HelpUri            :
            FileVersionInfo    : File:             C:\Users\Bruce\.virtualenvs\reverse-gikyn-XH\Scripts\python.exe
                                 InternalName:     Python Launcher
                                 OriginalFilename: py.exe
                                 FileVersion:      3.9.13
                                 FileDescription:  Python
                                 Product:          Python
                                 ProductVersion:   3.9.13
                                 Debug:            False
                                 Patched:          False
                                 PreRelease:       False
                                 PrivateBuild:     False
                                 SpecialBuild:     False
                                 Language:         Language Neutral

            Path               : C:\Users\Bruce\.virtualenvs\reverse-gikyn-XH\Scripts\python.exe
            Extension          : .exe
            Definition         : C:\Users\Bruce\.virtualenvs\reverse-gikyn-XH\Scripts\python.exe
            Source             : C:\Users\Bruce\.virtualenvs\reverse-gikyn-XH\Scripts\python.exe
            Version            : 3.9.13150.1013
            Visibility         : Public
            OutputType         : {System.String}
            Name               : python.exe
            CommandType        : Application
            ModuleName         :
            Module             :
            RemotingCapability : PowerShell
            Parameters         :
            ParameterSets      :


            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>
    * Note line with `Path`:
        * `Path : C:\Users\Bruce\.virtualenvs\reverse-gikyn-XH\Scripts\python.exe`
        * This is the current python interpreter `python.exe`. The interpreter is located inside the virtual environment's directory.


1. **INFO:** Examine the directory structure before we create the Django Project directory and files:
    * `tree /f /a`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   Pipfile
            |   Pipfile.lock
            |   README.md
            |
            \---notes
                    00_commands_and_links.md
                    00_create_pipenv.md
                    01_create_django_project.md

            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>
    * Notes:
        * There are no Django directories of files in the project yet.
        * We only have `pipenv`-related files and documentation-related files.

1. **ACTION:** Create a Django Project `the_project` using the `django-admin` command with sub-command `startproject`:
    * `django-admin startproject the_project .`
        * Command: `django-admin`
        * Sub-command: `startproject`
        * Project name: `the_project`
        * Directory location for the project files: `.`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> django-admin startproject the_project .
            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>

1. **INFO:** Examine the directory structure:
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
            |       00_commands_and_links.md
            |       00_create_pipenv.md
            |       01_create_django_project.md
            |
            \---the_project
                    asgi.py
                    settings.py
                    urls.py
                    wsgi.py
                    __init__.py

            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>
    * Notes:
        * The following directory and files have been added:
            * Directory `the_project` files:
                * `asgi.py`
                * `settings.py`
                * `urls.py`
                * `wsgi.py`
                * `__init__.py`
            * Files:
                * `manage.py`

1. **ACTION:** Start development server to test the Django skeleton project:
    * `python .\manage.py runserver`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> python .\manage.py runserver
            Watching for file changes with StatReloader
            Performing system checks...

            System check identified no issues (0 silenced).

            You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
            Run 'python manage.py migrate' to apply them.
            September 15, 2022 - 08:00:15
            Django version 4.0, using settings 'the_project.settings'
            Starting development server at http://127.0.0.1:8000/
            Quit the server with CTRL-BREAK.
        </details>

1. **ACTION:** Open internet browser to server root:
    * http://localhost:8000/

1. **INFO:** Verify Django Green Rocket and associated success text:
    * Semple associated success text:
        * `The install worked successfully! Congratulations!`

1. We now have a basic Django skeleton project. We will now add a Django application.

1. Proceed to 

## Repository Links:
* Back to [Create a `pipenv` Virtual Environment](./00_create_pipenv.md)