# Django Starter
* Django Starter with Django Project `the_project`, Django Admin Documentation Generator, and pre-made `Pipfile` and `Pipfile.lock`.

## Resources:
* [The Django admin documentation generator](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/admindocs/)
* [docutils](https://pypi.org/project/docutils/)

## Code Examples Repository links:
* [Create this Django Starter Project](./notes/00_create_django_starter.md)
* [Useful Commands and Links](./notes/00_useful_commands_and_links.md)
* [Code Examples Repository - `README.md`](../../README.md)
    * [`examples\`](../../)
* [Django Code Examples - `README.md`](../README.md)
    * [`examples\django\`](../)

## **NOTE:**
* This project directory contains a `notes` directory which contains markdown files for the documentation. These files do not affect the Django Project code.

## Process:
1. Examine current directory structure:
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

1. Directory currently contains `notes` files and a `README.md` file.

1. Create a `pipenv` virtual environment for the project:
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


