# Useful Commands and Links

## Commands:

### `pipenv`:
* `pipenv install`
    * Create a `pipenv` virtual environment for the current directory.
* `pipenv install django==4.0`
* `pipenv install django==4.1`
* `pipenv install docutils==0.19`
* `pipenv shell`
* `exit`
    * Exit the current `pipenv` virtual environment.

### `pip`:
* `pip list`

### Django:
* `django-admin startproject the_project .`
* `python .\manage.py startapp the_app`
* `python .\manage.py runserver`
* `<Ctrl+C>`
* `python .\manage.py makemigrations`
* `python .\manage.py migrate`
* `python .\manage.py createsuperuser`
* `python .\manage.py createsuperuser --email admin@email.app --username admin`
* Can't have leading `.\` when running command with `heroku run`:
    * `heroku run python manage.py createsuperuser --email admin@email.app --username admin`


### PowerShell:
* `Get-Command python | Format-List *`

### Misc:
* `tree /f /a`

## Development server web links:
* Server Root:
    * http://localhost:8000/
* Django Admin:
    * http://localhost:8000/admin/
    * http://localhost:8000/admin/auth/user/
* Django Admin Documentation:
    * http://localhost:8000/admin/doc/
    * http://localhost:8000/admin/doc/tags/
    * http://localhost:8000/admin/doc/filters/
    * http://localhost:8000/admin/doc/models/
    * http://localhost:8000/admin/doc/models/auth.user/