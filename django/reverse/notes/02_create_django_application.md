# 02 - Create Django Application

* This project's directory: [`reverse/`](./../)

## Resources

* [Writing your first Django app, part 1 - docs.djangoproject.com](https://docs.djangoproject.com/en/4.0/intro/tutorial01/#writing-your-first-django-app-part-1)
* [Django Tutorial Part 2: Creating a skeleton website - developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website)

## Code Examples Repository links

* [Code Examples Repository - README.md](../../../README.md)
  * [`examples/`](../../../)
* [Django Code Examples - README.md](../../README.md)
  * [`examples/django/`](../../)

## Tag meanings for this guide

* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.

## Process

1. **INFO:** Examine the directory structure before we create the Django Application directory and files:
    * `tree /f /a`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> tree /f /a
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
            |       00_commands_and_links.md
            |       00_create_pipenv.md
            |       01_create_django_project.md
            |       02_create_django_application.md
            |
            \---the_project
                    asgi.py
                    settings.py
                    urls.py
                    wsgi.py
                    __init__.py
            
            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>

1. **ACTION:** Create a Django application in the project root directory:
    * `python .\manage.py startapp the_app`

        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> python .\manage.py startapp the_app
            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>

1. **INFO:** Examine the directory structure and we will see a new directory with some files in it:
    * `tree /f /a`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> tree /f /a
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
            |       00_commands_and_links.md
            |       00_create_pipenv.md
            |       01_create_django_project.md
            |       02_create_django_application.md
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

            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>

1. **INFO:** The new application directory `the_app` contains the following:
    * Directory: `migrations`
        * This directory will hold the database `migrations` we will be performing as we build the application.
    * Files:
        * `admin.py`
        * `apps.py`
        * `models.py`
        * `tests.py`
        * `views.py`
        * `__init__.py`

1. Add the application [`the_app`](../the_app/)'s [`AppConfig`](../the_app/apps.py) `TheAppConfig` to the `INSTALLED_APPS` attribute of the project [`the_project/settings.py`](../the_project/settings.py) file:
    <details>
    <summary>Sample <code>INSTALLED_APPS</code> attribute contents:</summary>

        INSTALLED_APPS = [
            #...
            'the_app.apps.TheAppConfig',
            #...
        ]
    </details>

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
            September 15, 2022 - 16:18:56
            Django version 4.0, using settings 'the_project.settings'
            Starting development server at http://127.0.0.1:8000/
            Quit the server with CTRL-BREAK.
        </details>

1. **ACTION:** Open internet browser to server root:
    * <http://localhost:8000/>

1. **INFO:** Verify Django Green Rocket and associated success text:
    * Semple associated success text:
        * `The install worked successfully! Congratulations!`

1. **ACTION:** Use the following key-stroke, in the operating server terminal, to stop the development server:
    * \<Ctrl+C\>

1. **INFO:** We now have a basic Django skeleton Project and Application. There is no added functionlality yet.

1. **ACTION:** Proceed to [Create Index View](./03_create_index_view.md)

## Repository Links

* Back to [Create Django Project](./01_create_django_project.md)
