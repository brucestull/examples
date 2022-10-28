# Add the Application `the_app` to `settings.py`

## Resources:

## Process:

1. Add the `AppConfig` of the new application `the_app`, specified in [`the_app/apps.py`](../the_app/apps.py), to `INSTALLED_APPS` in [`the_project/settings.py`](../the_project/settings.py):
    ```
    INSTALLED_APPS = [
        #...
        'the_app.apps.TheAppConfig',
        #...
    ]
    ```

1. Continue to []()

* Back to [Create Django Project and Application](./01_create_django_project_and_app.md)