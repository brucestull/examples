# Add Model Functionality

## Resources:
* [Models](https://docs.djangoproject.com/en/4.0/topics/db/models/)
* [Fields](https://docs.djangoproject.com/en/4.0/topics/db/models/#fields)
* [Field types](https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types)
* [Field options](https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options)
* [Migrations](https://docs.djangoproject.com/en/4.0/topics/migrations/#module-django.db.migrations)
* [`makemigrations`](https://docs.djangoproject.com/en/4.1/ref/django-admin/#makemigrations)
* [`migrate`](https://docs.djangoproject.com/en/4.1/ref/django-admin/#migrate)

## Tag meanings for this guide:
* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.

## Process:
1. **ACTION:** Create a [`model`](https://docs.djangoproject.com/en/4.0/topics/db/models/) `AwesomeCat` in [`the_app/models.py`](../the_app/models.py):
    * Import `models` from `django.db`
    * Model attribute field name: `name`
    * Model attribute field type: `CharField`
    * Model class name: `AwesomeCat`
        <details>
        <summary>Sample <code>the_app/models.py</code> contents:</summary>

            from django.db import models

            class AwesomeCat(models.Model):
                name = models.CharField(max_length=50)
        </details>

1. [`register`](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#modeladmin-objects) the new model `AwesomeCat` with the Django admin [`the_app/admin.py`](../the_app/admin.py):
    * Import `admin` from `django.contrib`.
    * Import our model `AwesomeCat` from `.models`.
    * Use `admin.site.register()` to register our model `AwesomeCat`.
    <details>
    <summary>Sample <code>the_app/admin.py</code> contents:</summary>

        from django.contrib import admin

        from .models import AwesomeCat

        admin.site.register(AwesomeCat)
    </details>

1. **ACTION:** Perform `makemigrations`:
    * `python .\manage.py makemigrations`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\list-view-with-home> python .\manage.py makemigrations
            Migrations for 'the_app':
            the_app\migrations\0001_initial.py
                - Create model AwesomeCat
            PS C:\Users\Bruce\Programming\examples\django\list-view-with-home>
        </details>

1. **ACTION:** Perform `migrate`:
    * `python .\manage.py migrate`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\list-view-with-home> python .\manage.py migrate
            Operations to perform:
              Apply all migrations: admin, auth, contenttypes, sessions, the_app
            Running migrations:
              Applying contenttypes.0001_initial... OK
              Applying auth.0001_initial... OK
              Applying admin.0001_initial... OK
              Applying admin.0002_logentry_remove_auto_add... OK
              Applying admin.0003_logentry_add_action_flag_choices... OK
              Applying contenttypes.0002_remove_content_type_name... OK
              Applying auth.0002_alter_permission_name_max_length... OK
              Applying auth.0003_alter_user_email_max_length... OK
              Applying auth.0004_alter_user_username_opts... OK
              Applying auth.0005_alter_user_last_login_null... OK
              Applying auth.0006_require_contenttypes_0002... OK
              Applying auth.0007_alter_validators_add_error_messages... OK
              Applying auth.0008_alter_user_username_max_length... OK
              Applying auth.0009_alter_user_last_name_max_length... OK
              Applying auth.0010_alter_group_name_max_length... OK
              Applying auth.0011_update_proxy_permissions... OK
              Applying auth.0012_alter_user_first_name_max_length... OK
              Applying sessions.0001_initial... OK
              Applying the_app.0001_initial... OK
            PS C:\Users\Bruce\Programming\examples\django\list-view-with-home>
        </details>

1. Create a superuser:
    * `python .\manage.py createsuperuser`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\list-view-with-home> python .\manage.py createsuperuser
            Username (leave blank to use 'bruce'): admin
            Email address: admin@email.app
            Password:
            Password (again):
            This password is too common.
            Bypass password validation and create user anyway? [y/N]: y
            Superuser created successfully.
            PS C:\Users\Bruce\Programming\examples\django\list-view-with-home>
        </details>

1. Start development server:
    * `python .\manage.py runserver`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\list-view-with-home> python .\manage.py runserver
            Watching for file changes with StatReloader
            Performing system checks...

            System check identified no issues (0 silenced).
            September 03, 2022 - 17:46:49
            Django version 4.0, using settings 'the_project.settings'
            Starting development server at http://127.0.0.1:8000/
            Quit the server with CTRL-BREAK.
        </details>

1. Open internet browser to Django Admin Interface URL:
    * http://localhost:8000/admin/

1. Log in to the Django Admin Interface using credentials provided above.

1. Create a couple new `AwesomeCat` objects in Django Admin Interface.

1. Proceed to [Add List View](./04_add_list_view.md).

## Navigation links:
* Back to [Home Page with String](./02_home_page_with_string.md)