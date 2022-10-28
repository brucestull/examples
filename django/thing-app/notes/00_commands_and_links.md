# Useful Commands and Links

## Development Server Web Links:
* Server Root:
    * http://localhost:8000/
* Other views:
    * http://localhost:8000/url-route-to-the-app/show-all-things-url/
    * http://localhost:8000/url-route-to-the-app/url-route-for-simple-view-function
    * http://localhost:8000/url-route-to-the-app/url-route-for-simple-view-function/

## Django Admin Links:
* Django Admin:
    * http://localhost:8000/admin/
* Django Admin Documentation:
    * http://localhost:8000/admin/doc/
    * http://localhost:8000/admin/doc/tags/
    * http://localhost:8000/admin/doc/filters/
    * http://localhost:8000/admin/doc/models/
    * http://localhost:8000/admin/doc/models/auth.user/

## Commands:

### Django:
* `python .\manage.py makemigrations`
* `python .\manage.py migrate`
* `python .\manage.py createsuperuser`
* `python .\manage.py createsuperuser --email admin@email.app --username admin`
* `python .\manage.py test`

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

### Django Create `SECRET_KEY`:
* `python manage.py shell`
* `from django.core.management.utils import get_random_secret_key`
* `print(get_random_secret_key())`

### Heroku:
* `git push heroku main`
* Can't have leading `.\` when running command with `heroku run`:
    * `heroku run python manage.py createsuperuser --email admin@email.app --username admin`
* `heroku login`
* `heroku run python manage.py migrate users`
* `heroku run python manage.py migrate`

### PowerShell:
* `Get-Command python | Format-List *`

### Misc:
* `tree /f /a`

### Git:
* `git remote -v`

## Production deployment links:
* Dashboard:
* Server Root:
* Models Home:
* Create user:
* Django Admin:
* Django Admin Documentation:

