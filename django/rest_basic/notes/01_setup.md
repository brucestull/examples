# Project Setup

## Repository Links:
* [Examples Repository](../../../README.md)
* [Django REST - Basic - `README.me`](../README.md)

## Development server links and such:
* `python .\manage.py runserver`
* http://localhost:8000/admin/

## Tag meanings for this guide:
* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.

## Process:
1. Start inside project directory:
    * Sample directory location:
        * `C:\Users\Bruce\Programming\examples\django\rest_basic`

1. Create a new `pipenv` virtual environment:
    * `pipenv install django==4.0`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\rest_basic> pipenv install django==4.0
            Creating a virtualenv for this project...
            Pipfile: C:\Users\Bruce\Programming\examples\django\rest_basic\Pipfile
            Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.6) to create virtualenv...
            [ ===] Creating virtual environment...created virtual environment CPython3.10.6.final.0-64 in 2995ms
              creator CPython3Windows(dest=C:\Users\Bruce\.virtualenvs\rest_basic-8EvQpMVS, clear=False, no_vcs_ignore=False, global=False)
              seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Bruce\AppData\Local\pypa\virtualenv)
                added seed packages: pip==22.2.2, setuptools==63.4.3, wheel==0.37.1
              activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
            
            Successfully created virtual environment!
            Virtualenv location: C:\Users\Bruce\.virtualenvs\rest_basic-8EvQpMVS
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
            PS C:\Users\Bruce\Programming\examples\django\rest_basic>
        </details>

1. Activate the `pipenv` virtual environment:
    * `pipenv shell`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\rest_basic> pipenv shell
            Launching subshell in virtual environment...
            PowerShell 7.2.6
            Copyright (c) Microsoft Corporation.

            https://aka.ms/powershell
            Type 'help' to get help.

            PS C:\Users\Bruce\Programming\examples\django\rest_basic>
        </details>

1. Create a Django "Project":
    * 

