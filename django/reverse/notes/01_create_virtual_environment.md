# 01 - Create a New `pipenv` Virtual Environment for the Project

## Resources:
* [Installing Pipenv - python-guide.org](https://docs.python-guide.org/dev/virtualenvs/#installing-pipenv)
* [Pipenv: Python Dev Workflow for Humans - pypa.io](https://pipenv.pypa.io/en/latest/)
* [`pipenv` - pypi.org](https://pypi.org/project/pipenv/)


## Code Examples Repository links:
* [Code Examples Repository](../../../README.md)
* [Django Code Examples](../../README.md)

## Tag meanings for this guide:
* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.

## Process:
1. **ACTION:** Use the provided [Pipfile](../Pipfile) to create a `pipenv` virtual environment for the project:
    * The following command will use the [Pipfile](../Pipfile) to do the following:
        * Create a `pipenv` virtual environment.
        * Install the dependencies prescribed in [Pipfile](../Pipfile) into the newly created virtual environment.
    * `pipenv install`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> pipenv install
            Creating a virtualenv for this project...
            Pipfile: C:\Users\Bruce\Programming\examples\django\reverse\Pipfile
            Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.6) to create virtualenv...
            [=== ] Creating virtual environment...
              creator CPython3Windows(dest=C:\Users\Bruce\.virtualenvs\reverse-gikyn-XH, clear=False, no_vcs_ignore=False, global=False)
              seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Bruce\AppData\Local\pypa\virtualenv)
                added seed packages: pip==22.2.2, setuptools==64.0.3, wheel==0.37.1
              activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

            Successfully created virtual environment!
            Virtualenv location: C:\Users\Bruce\.virtualenvs\reverse-gikyn-XH
            Installing dependencies from Pipfile.lock (2d0928)...
              ================================ 5/5 - 00:00:08
            To activate this project's virtualenv, run pipenv shell.
            Alternatively, run a command inside the virtualenv with pipenv run.
            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>

1. **ACTION:** Activate the new `pipenv` virtual environment:
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

1. **INFO:** Verify the virtual environment's installed packages:
    * `pip list`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> pip list
            Package    Version
            ---------- -------
            asgiref    3.5.2
            Django     4.0
            docutils   0.19
            pip        22.2.2
            setuptools 64.0.3
            sqlparse   0.4.2
            tzdata     2022.2
            wheel      0.37.1
            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>

1. **INFO:** Verify our current terminal session is using the virtual environment's python interpreter:
    * `Get-Command python | Format-List *`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\reverse> Get-Command python | Format-List *

            HelpUri            :
            FileVersionInfo    : File:             C:\Users\Bruce\.virtualenvs\reverse-gikyn-XH\Scripts\python.exe
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

            Path               : C:\Users\Bruce\.virtualenvs\reverse-gikyn-XH\Scripts\python.exe
            Extension          : .exe
            Definition         : C:\Users\Bruce\.virtualenvs\reverse-gikyn-XH\Scripts\python.exe
            Source             : C:\Users\Bruce\.virtualenvs\reverse-gikyn-XH\Scripts\python.exe
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


            PS C:\Users\Bruce\Programming\examples\django\reverse>
        </details>
    * Take note of the line with `Path`.
        * Sample contents:
            * `Path : C:\Users\Bruce\.virtualenvs\reverse-gikyn-XH\Scripts\python.exe`
        * This is the location of the python interpreter which the virtual environment uses.
        * The virtual environment files are located in the directory:
            * `C:\Users\Bruce\.virtualenvs\reverse-gikyn-XH\`






## Repository Links:
* Back to [Demonstrate `reverse()` Method](./notes.md)