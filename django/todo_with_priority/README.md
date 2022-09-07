# django-starter-compare
Basic django starter, only includes the automatically generated Project `the_project` and App `the_app`. This will be used to compare what things have to be changed when making an actual app.

## Links:
* [`notes_startup.md`](./notes/notes_startup.md)

## **IMPORTANT**
* This example repository has the Django [`SECRET_KEY`](https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key) revealed in [`settings.py`](./the_project/settings.py). It is important in actual production projects to not push the actual `SECRET_KEY` to remote public repositories. There are ways to set this up which are beyond the scope of this document. One example, though, is used in [`settings`](https://github.com/brucestull/DjangoCustomUserStarter/tree/main/my_current_project/settings) directory which is part of [brucestull's DjangoCustomUserStarter](https://github.com/brucestull/DjangoCustomUserStarter)

## What is included:
* Django Project: `the_project`.
* Django App: `the_app`.
* `pipenv` settings files.

## What is not included:

## Files to ignore when checking `compare`:
* [`.gitignore`](./.gitignore)
* [`LICENSE`](./LICENSE)
* [`README.md`](./README.md)
* [`Pipfile`](./Pipfile)
* [`Pipfile.lock`](./Pipfile.lock)