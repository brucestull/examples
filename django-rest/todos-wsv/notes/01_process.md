# Process:

## Basic Setup:

1. Start in the root directory of the project.

1. Create a new `pipenv` virtual environment for the current directory and install some needed packages:
    * Needed packages:
        * `django`
        * `djangorestframework`
        * `docutils`
    * `pipenv install django==4.1 djangorestframework==3.14.0 docutils==0.19`

1. Activate the `pipenv` virtual environment:
    * `pipenv shell`:

1. Create a new Django project:
    * `django-admin startproject config .`

1. Create a new Django app:
    * `django-admin startapp todos`

1. Add the app config for `todos` to the `INSTALLED_APPS` list in `config/settings.py`:
    ```
    INSTALLED_APPS = [
        #...
        'todos.apps.TodosConfig',
        #...
    ]
    ```

1. Add model 'Todo' to [`todos/models.py`](../todos/models.py):
    ```
    from django.db import models


    class Todo(models.Model):
        title = models.CharField(max_length=120)
        description = models.CharField(max_length=255)
        completed = models.BooleanField(default=False)

        def __str__(self):
            return self.title
    ```

1. Perform migrations:
    1. `python manage.py makemigrations`
    1. `python manage.py migrate`

1. Add the `Todo` model to the admin site:
    1. Add `from .models import Todo` to [`todos/admin.py`](../todos/admin.py)
    1. Add `admin.site.register(Todo)` to [`todos/admin.py`](../todos/admin.py)
    ```
    from django.contrib import admin


    from .models import Todo

    admin.site.register(Todo)
    ```

1. Create a superuser:
    * `python manage.py createsuperuser`

1. Test the admin site:
    * `python manage.py runserver`
    * http://localhost:8000/admin/

1. Add a few `Todo` objects to the admin site.

1. Create the `api` app:
    * `django-admin startapp api`

1. Add the app config for `api` to the `INSTALLED_APPS` list in [`config/settings.py`](../config/settings.py):
    ```
    INSTALLED_APPS = [
        #...
        'api.apps.ApiConfig',
        #...
    ]
    ```

1. Django Admin Documentation Generator:
    1. Add `django.contrib.admindocs` to the `INSTALLED_APPS` list in [`config/settings.py`](../config/settings.py):
        ```
        INSTALLED_APPS = [
            #...
            'django.contrib.admindocs',
            #...
        ]
        ```
    1. Add import for `include` from `django.urls` to [`config/urls.py`](../config/urls.py):
        ```
        from django.urls import include
        ```
    1. Add `path('admin/doc/', include('django.contrib.admindocs.urls')),` to the `urlpatterns` list in [`config/urls.py`](../config/urls.py):
        * IMPORTANT: This must be added before the `path('admin/', admin.site.urls),` line.
        ```
        from django.urls import include

        urlpatterns = [
            #...
            path('admin/doc/', include('django.contrib.admindocs.urls')),
            #...
        ]
        ```

1. Test the admin documentation generator:
    * `python manage.py runserver`
    * http://localhost:8000/admin/doc/
    * http://localhost:8000/admin/doc/models/
    * http://localhost:8000/admin/doc/models/todos.todo/

1. Add `rest_framework` to the `INSTALLED_APPS` list in [`config/settings.py`](../config/settings.py):
    ```
    INSTALLED_APPS = [
        #...
        'rest_framework',
        #...
    ]
    ```

1. Add a `DEFAULT_PERMISSION_CLASSES` list to the `REST_FRAMEWORK` dict in [`config/settings.py`](../config/settings.py):
    ```
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.AllowAny',
        ],
    }
    ```


1. Add a file [`api/serializers.py`](../api/serializers.py) with following contents:
    ```
    from rest_framework import serializers
    
    from todos import models
    
    
    class TodoSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Todo
            fields = (
                'id',
                'title',
                'description',
                'completed'
            )
    ```

1. Add `TodoList` and `TodoDetail` classes to [`api/views.py`](../api/views.py):
    ```
    from rest_framework import generics
    
    from todos import models
    from . import serializers
    
    
    class TodoList(generics.ListCreateAPIView):
        queryset = models.Todo.objects.all()
        serializer_class = serializers.TodoSerializer
    
    
    class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = models.Todo.objects.all()
        serializer_class = serializers.TodoSerializer
    ```

1. Add a URL endpoint to `urlpatterns` list for the API app to [`config/urls.py`](../config/urls.py):
    ```
    urlpatterns = [
        #...
        path('api/v1/', include('api.urls')),
        #...
    ]
    ```

1. Add a file [`api/urls.py`](../api/urls.py) with following contents:
    ```
    from django.urls import path

    from . import views


    urlpatterns = [
        path('', views.TodoList.as_view()),
        path('<int:pk>/', views.TodoDetail.as_view()),
    ]
    ```

1. Test the API:
    * `python manage.py runserver`
    * http://localhost:8000/api/v1/
    * http://localhost:8000/api/v1/1/
    * http://localhost:8000/api/v1/2/

## Change use of `generic` views to `viewsets`:

1. Modify [`api/views.py`](../api/views.py) to use `viewsets` instead of `generics`:
    ```
    from rest_framework import viewsets
    
    from todos import models
    from . import serializers
    
    
    class TodoViewSet(viewsets.ModelViewSet):
        queryset = models.Todo.objects.all()
        serializer_class = serializers.TodoSerializer
    ```

1. Modify [`api/urls.py`](../api/urls.py) to use `viewsets` instead of `generics`:
    ```
    from . import views

    from rest_framework.routers import DefaultRouter


    router = DefaultRouter()
    router.register('', views.TodoViewSet, basename='todos')
    urlpatterns = router.urls
    ```

1. Test the API:
    * `python manage.py runserver`
    * http://localhost:8000/api/v1/
    * http://localhost:8000/api/v1/1/
    * http://localhost:8000/api/v1/2/

1. Investigate the API by adding and removing models in the Django Browsable API.
    * The Browsable API is a great way to explore the API and test it out.
    * It has buttons for all the HTTP methods:
        * GET
        * POST
        * PUT
        * PATCH
        * DELETE
