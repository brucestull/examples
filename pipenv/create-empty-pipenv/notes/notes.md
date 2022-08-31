# Create `pipenv` Virtual Environment

* This guide uses PowerShell terminal. Other terminal commands to be added later.

## Resources:

* [Installing Pipenv - python-guide.org](https://docs.python-guide.org/dev/virtualenvs/#installing-pipenv)
* [Pipenv: Python Dev Workflow for Humans - pipenv.pypa.io](https://pipenv.pypa.io/en/latest/)
* [Pipenv: A Guide to the New Python Packaging Tool - realpython.com](https://realpython.com/pipenv-guide/)
* [pipenv - pypi.org](https://pypi.org/project/pipenv/)

## Requirements:

* User has functioning `python` installation.
* User has functioning `pip` installation.
* User has functioning `<OTHER_PACKAGE_OR_PROGRAM>` installation.

## Tag meanings for this guide:

* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info and not necessarily functional or code changes.

## Process:

1. **INFO:** Use `pip list` to list globally installed python packages and verify `pip` is installed so we can use it to install `pipenv`:
    * `pip list`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\pipenv\create-empty-pipenv> pip list
            Package            Version
            ------------------ -----------
            asgiref            3.5.2
            certifi            2022.5.18.1
            charset-normalizer 2.0.12
            click              8.1.3
            colorama           0.4.5
            distlib            0.3.4
            Django             4.0
            filelock           3.7.1
            Flask              2.2.2
            idna               3.3
            itsdangerous       2.1.2
            Jinja2             3.1.2
            MarkupSafe         2.1.1
            pip                22.2.2
            platformdirs       2.5.2
            requests           2.28.0
            setuptools         63.2.0
            six                1.16.0
            sqlparse           0.4.2
            tzdata             2022.2
            urllib3            1.26.9
            virtualenv         20.14.1
            virtualenv-clone   0.5.7
            Werkzeug           2.2.2
            PS C:\Users\Bruce\Programming\examples\pipenv\create-empty-pipenv>
        </details>
    * There might be quite a few python packages listed here. That is okay. When we create the virtual environment, there will be mininal packages in it and we will control which packages are installed in it.

1. Install `pipenv` using `pip install --user pipenv`:
    * `pip install --user pipenv`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\pipenv\create-empty-pipenv> pip install --user pipenv
            Collecting pipenv
            Using cached pipenv-2022.8.24-py2.py3-none-any.whl (3.4 MB)
            Requirement already satisfied: virtualenv-clone>=0.2.5 in c:\users\bruce\appdata\roaming\python\python310\site-packages (from pipenv) (0.5.7)
            Requirement already satisfied: virtualenv in c:\users\bruce\appdata\roaming\python\python310\site-packages (from pipenv) (20.14.1)
            Requirement already satisfied: setuptools>=36.2.1 in c:\users\bruce\appdata\local\programs\python\python310\lib\site-packages (from pipenv) (63.2.0)
            Requirement already satisfied: certifi in c:\users\bruce\appdata\roaming\python\python310\site-packages (from pipenv) (2022.5.18.1)
            Requirement already satisfied: six<2,>=1.9.0 in c:\users\bruce\appdata\roaming\python\python310\site-packages (from virtualenv->pipenv) (1.16.0)
            Requirement already satisfied: platformdirs<3,>=2 in c:\users\bruce\appdata\roaming\python\python310\site-packages (from virtualenv->pipenv) (2.5.2)
            Requirement already satisfied: filelock<4,>=3.2 in c:\users\bruce\appdata\roaming\python\python310\site-packages (from virtualenv->pipenv) (3.7.1)
            Requirement already satisfied: distlib<1,>=0.3.1 in c:\users\bruce\appdata\roaming\python\python310\site-packages (from virtualenv->pipenv) (0.3.4)
            Installing collected packages: pipenv
            Successfully installed pipenv-2022.8.24
            PS C:\Users\Bruce\Programming\examples\pipenv\create-empty-pipenv>
        </details>        

1. **INFO:** Use `pip list` to list globally installed python packages and verify `pipenv` is now installed so we can use it to create our virtual environment:
    * `pip list`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\pipenv\create-empty-pipenv> pip list
            Package            Version
            ------------------ -----------
            ...
            pipenv             2022.8.24
            ...
            PS C:\Users\Bruce\Programming\examples\pipenv\create-empty-pipenv>
        </details>
    * There might be quite a few python packages listed here. That is okay. When we create the virtual environment, there will be mininal packages in it and we will control which packages are installed in it.
    * The "Sample output" above has all packages other than `pipenv` redacted (as indicated by the `...` above and below the line for `pipenv`) so it's easier to see that `pipenv` is installed.

1. **ACTION:** Start in the directory which will contain the code we are writing for the project or lab or assignment. Our project directory is `create-empty-pipenv`.
    * Sample location:
        * `C:\Users\Bruce\Programming\examples\pipenv\create-empty-pipenv`

1. **ACTION:** Use `pipenv install` to create the virtual environment:
    * `pipenv install`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\pipenv\create-empty-pipenv> pipenv install
            Creating a virtualenv for this project...
            Pipfile: C:\Users\Bruce\Programming\examples\pipenv\create-empty-pipenv\Pipfile
            Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.6) to create virtualenv...
            [ ===] Creating virtual environment...created virtual environment CPython3.10.6.final.0-64 in 2165ms
            creator CPython3Windows(dest=C:\Users\Bruce\.virtualenvs\create-empty-pipenv-Xeso9zoU, clear=False, no_vcs_ignore=False, global=False)
            seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Bruce\AppData\Local\pypa\virtualenv)
                added seed packages: pip==22.2.2, setuptools==63.3.0, wheel==0.37.1
            activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

            Successfully created virtual environment!
            Virtualenv location: C:\Users\Bruce\.virtualenvs\create-empty-pipenv-Xeso9zoU
            Creating a Pipfile for this project...
            Pipfile.lock not found, creating...
            Locking [dev-packages] dependencies...
            Locking [packages] dependencies...
            Updated Pipfile.lock (e4eef2)!
            Installing dependencies from Pipfile.lock (e4eef2)...
            ================================ 0/0 - 00:00:00
            To activate this project's virtualenv, run pipenv shell.
            Alternatively, run a command inside the virtualenv with pipenv run.
            PS C:\Users\Bruce\Programming\examples\pipenv\create-empty-pipenv>
        </details>

1. Some notes about the above "Sample output":
    * The line with `Virtualenv location` indicates the location of the actual location:
        * Sample line output:
            ```
            Virtualenv location: C:\Users\Bruce\.virtualenvs\create-empty-pipenv-Xeso9zoU
            ```
        * `pipenv` created a directory named `create-empty-pipenv-Xeso9zoU` inside `C:\Users\Bruce\.virtualenvs\`.
        * The name of the directory `create-empty-pipenv-Xeso9zoU` is constructed by taking the directory name where the `pipenv install` command is executed and then adding a dash followed by a unique string `Xeso9zoU`.
        * The directory `create-empty-pipenv-Xeso9zoU` is the directory which contains all of the virtual environment's packages.

1. **INFO:**" Use `tree /f /a` to examine directory contents:
    * `tree /f /a`

1. Note presense of `Pipfile` and `Pipfile.lock` above.
    * `Pipfile` is one `pipenv` configuration file for the project.
        * This configuration file is located inside the same directory as the project code.
        * The actual virtual environment files and packages are in a different directory noted above. Usually, in Windows, the parent directory of the virutal environment is `C:\Users\Bruce\.virtualenvs\`.
    * [`Pipfile.lock`](https://pipenv.pypa.io/en/latest/basics/#pipenv-lock) is one other `pipenv`  configuration file for the project.

1. **ACTION:** Activate the virtual environment by using `pipenv shell`:
    * `pipenv shell`
        <details>
        <summary>Sample output when the <code>pipenv shell</code> command is executed and a subshell (the virtual environment) is launched</summary>

            PS C:\Users\Bruce\Programming\examples\pipenv\create-empty-pipenv> pipenv shell
            Launching subshell in virtual environment...
            PowerShell 7.2.6
            Copyright (c) Microsoft Corporation.

            https://aka.ms/powershell
            Type 'help' to get help.

            PS C:\Users\Bruce\Programming\examples\pipenv\create-empty-pipenv>
        </details>

        <details>
        <summary>Sample output when the <code>pipenv shell</code> command is executed in an already activated virtual environment</summary>

            PS C:\Users\Bruce\Programming\examples\pipenv\create-empty-pipenv> pipenv shell
            Shell for C:\Users\Bruce\.virtualenvs\create-empty-pipenv-Xeso9zoU already activated.
            No action taken to avoid nested environments.
            PS C:\Users\Bruce\Programming\examples\pipenv\create-empty-pipenv>
        </details>

1. ADD_SOME_EXPLANATION_OR_DESCRIPTION_HERE

1. **INFO:**" List the Python packages which are installed in the virtual environment by using `pip list`:
    * `pip list`
        <details>
        <summary>Sample output</summary>

            PS C:\Users\Bruce\Programming\examples\pipenv\create-empty-pipenv> pip list
            Package    Version
            ---------- -------
            pip        22.2.2
            setuptools 63.3.0
            wheel      0.37.1
            PS C:\Users\Bruce\Programming\examples\pipenv\create-empty-pipenv>
        </details>     

1. Notes about the above `pip list` output:
    * There can be significantly fewer python packages installed in the virtual environment than those globally installed. This is expected. The reason we use a virtual environment is to ensure we only install the packages we need for the project.

1. The `pipenv` virtual environment has been created for the project. You can add your code for your specific project and then run the code using the packages within the virtual environment.

1. We will now use `pipenv install $PACKAGE_NAME` whenever we want to install another python package `$PACKAGE_NAME` in our virtual environment.
    * It is advised to run the `pipenv` commands while current directory is the same directory as `Pipfile` and `Pipfile.lock`.
    * The commands may work in other directories but the author of this document hasen't tested that yet.

1. Whenever we open a new terminal and we want to use the virtual environment:
    1. Change directory into the directory which contains `Pipfile` and `Pipfile.lock`.
    1. Use `pipenv shell` to activate the virtual environment.