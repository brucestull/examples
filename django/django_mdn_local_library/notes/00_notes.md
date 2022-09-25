# Django MDN Local Library

## Resources:

## Process:

### Setup:

1. `C:\Users\Bruce\Programming\examples\django\django_mdn_local_library\`

1. `python .\manage.py createsuperuser --email admin@email.app --username admin`

1. `python .\manage.py runserver`

1. http://localhost:8000/

1. `heroku login`

1. `heroku create flynnt-knapp-mdn-local-library`
	* https://flynnt-knapp-mdn-local-library.herokuapp.com/
	* https://git.heroku.com/flynnt-knapp-mdn-local-library.git

1. `heroku git:remote -a flynnt-knapp-mdn-local-library`

1. Provision database server

1. Config Vars:
	* `DJANGO_SETTINGS_MODULE`:
		* `my_current_project.settings.production`

1. Config Vars:
	* `SECRET_KEY`
		* `THE_SPECIFIC_KEY`

1. Config Vars:
	* Database Credentials

1. `ALLOWED_HOSTS`:
	* ['flynnt-knapp-mdn-local-library.herokuapp.com']






## Repository Links:
* Back to Repository [`README.md`](../README.md).