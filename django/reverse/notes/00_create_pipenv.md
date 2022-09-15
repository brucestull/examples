# 00 - Create a `pipenv` Virtual Environment

## Resources:
* [Installing Pipenv - python-guide.org](https://docs.python-guide.org/dev/virtualenvs/#installing-pipenv)
* [Pipenv: Python Dev Workflow for Humans - pipenv.pypa.io](https://pipenv.pypa.io/en/latest/)
* [`pipenv` - pypi.org](https://pypi.org/project/pipenv/)

## Code Examples Repository links:
* [Code Examples Repository - README.md](../../../README.md)
    * [`examples/`](../../../)
* [Django Code Examples - README.md](../../README.md)
    * [`examples/django/`](../../)

## Tag meanings for this guide:
* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.

## Process:
1. **ACTION:** Start in the directory which will be the root of the project:
    * Sample location:
        * `C:\Users\Bruce\Programming\examples\django\reverse\`

1. **INFO:** Examine the directory structure:
    * `tree /f /a`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   README.md
            |
            \---notes
                    commands_and_links.md
                    create_pipenv.md

            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>

1. Investigate current globally installed packages:
    * `pip list`
        <details>
        <summary>Sample output for author:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> pip list
            Package             Version
            ------------------- -----------
            asgiref             3.5.2
            attrs               22.1.0
            certifi             2022.5.18.1
            charset-normalizer  2.0.12
            click               8.1.3
            colorama            0.4.5
            distlib             0.3.4
            Django              4.0
            djangorestframework 3.13.1
            docutils            0.19
            filelock            3.7.1
            Flask               2.2.2
            idna                3.3
            iniconfig           1.1.1
            itsdangerous        2.1.2
            Jinja2              3.1.2
            MarkupSafe          2.1.1
            packaging           21.3
            pip                 22.2.2
            pipenv              2022.8.24
            platformdirs        2.5.2
            pluggy              1.0.0
            py                  1.11.0
            pyparsing           3.0.9
            pytest              7.1.3
            pytz                2022.2.1
            requests            2.28.0
            setuptools          63.2.0
            six                 1.16.0
            sqlparse            0.4.2
            tomli               2.0.1
            tzdata              2022.2
            urllib3             1.26.9
            virtualenv          20.14.1
            virtualenv-clone    0.5.7
            Werkzeug            2.2.2
            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>
    * Notes:
        * These are all the globally installed packages that the author has installed on their system.
        * We will run `pip list` after we create and activate the virtual environment and we will then see a significantly smaller number of installed packages.

1. **ACTION:** Create a new `pipenv` virtual environment:
    * We will use a command which both creates the virtual environment and installs a package in it.
        * The following are three options:
            * `pipenv install` createS a virtual environment.
            * `pipenv install PACKAGE_NAME` creates the virtual environment and install the package `PACKAGE_NAME` in the virtual environment.
            * `pipenv install PACKAGE_NAME==VERSION` creates the virtual environment and installs the package `PACKAGE_NAME` with version `VERSION` in the virtual environment.
    * `pipenv install django==4.0`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> pipenv install django==4.0
            Creating a virtualenv for this project...
            Pipfile: C:\Users\Bruce\Programming\examples\django\reverse\Pipfile
            Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.6) to create virtualenv...
            [=== ] Creating virtual environment...created virtual environment CPython3.10.6.final.0-64 in 2878ms
              creator CPython3Windows(dest=C:\Users\Bruce\.virtualenvs\reverse-gikyn-XH, clear=False, no_vcs_ignore=False, global=False)
              seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Bruce\AppData\Local\pypa\virtualenv)
                added seed packages: pip==22.2.2, setuptools==65.0.2, wheel==0.37.1
              activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

            Successfully created virtual environment!
            Virtualenv location: C:\Users\Bruce\.virtualenvs\reverse-gikyn-XH
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
            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>
    * Note line with `Virtualenv location`, this is the location of the executable files for the virtual environment.
        * Sample location:
            * `C:\Users\Bruce\.virtualenvs\reverse-gikyn-XH`

1. **INFO:** Examine the directory structure:
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
                    commands_and_links.md
                    create_pipenv.md

            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>
    * Note presense of two new files. These files are the configuration files for the `pipenv` virtual environment:
        * `Pipfile`
        * `Pipfile.lock`

1. **ACTION:** Activate the `pipenv` virtual environment:
    * `pipenv shell`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> pipenv shell
            Launching subshell in virtual environment...
            PowerShell 7.2.6
            Copyright (c) Microsoft Corporation.

            https://aka.ms/powershell
            Type 'help' to get help.

            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>
    * Note the line with `Launching subshell...`:
        * This is indicating that we are launching a subshell of the terminal in the virtual environment.

1. **INFO:** Investigate current installed packages available in the virtual environment:
    * `pip list`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> pip list
            Package    Version
            ---------- -------
            asgiref    3.5.2
            Django     4.0
            pip        21.3.1
            setuptools 60.2.0
            sqlparse   0.4.2
            tzdata     2022.2
            wheel      0.37.1
            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>
    * Notes:
        * There are a significantly smaller number of packages installed in the virtual environment than globally installed packages.
        * This is expected since we want to control the specific packages installed in the virtual environment.
        * We may want to use a specific package version for different projects. `pipenv` lets us do that.

1. **INFO:** We can use the following to exit the virtual environment subshell:
    * `exit`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> exit
            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>
    * If we didn't use `pipenv shell` to activate the virtual environment, this command will exit the terminal session immediately without notice.
        * If this happens, we can just start new terminal session.

1. **INFO:** When we're ready to continue the project in a new terminal session, we need to activate the virtual environment again. This is done by running the following command, same as above:
    * `pipenv shell`

1. **INFO:** We now have a functioning `pipenv` virtual environment. We can use it to build out our Django Project.

1. Proceed to [Create Django Project](./01_create_django_project.md).

