# Create the API

## Code Examples Repository links:
* [Code Examples Repository](../../../README.md)
* [Django REST - Basic - `README.me`](../README.md)

## Development server links and such:
* `python .\manage.py runserver`
* http://localhost:8000/admin/
* http://localhost:8000/the-api/v1/
* http://localhost:8000/the-api/v1/users-api-url/
* http://localhost:8000/the-api/v1/users-api-url/1/
* http://localhost:8000/the-api/v1/users-api-url/2/
* http://localhost:8000/the-api/v1/groups-api-url/

## Tag meanings for this guide:
* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.

## Process:
1. **ACTION:** Install `djangorestframework`:
    * `pipenv install djangorestframework==3.13.1`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\rest_basic> pipenv install djangorestframework==3.13.1
            Installing djangorestframework==3.13.1...
            Adding djangorestframework to Pipfile's [packages]...
            Installation Succeeded
            Pipfile.lock (2d0928) out of date, updating to (fef611)...
            Locking [dev-packages] dependencies...
            Locking [packages] dependencies...
            Locking...
            Resolving dependencies...
            Success!
            Updated Pipfile.lock (fef611)!
            Installing dependencies from Pipfile.lock (fef611)...
            ================================ 0/0 - 00:00:00
            PS C:\Users\Bruce\Programming\examples\django\rest_basic>
        </details>

1. **ACTION:** Create a new module [`the_api/serializers.py`](../the_api/serializers.py).

1. **ACTION:** Edit [`the_api/serializers.py`](../the_api/serializers.py) to match the following:
    <details>
    <summary>Sample <code>the_api/serializers.py</code> implementation:</summary>

        from django.contrib.auth.models import User, Group
        from rest_framework import serializers


        class UserSerializer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = User
                fields = [
                    'id',
                    'username',
                    'email',
                    'first_name',
                    'last_name',
                    'groups',
                ]

        class GroupSerializer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Group
                fields = [
                    'url',
                    'name',
                ]
    </details>

1. **ACTION:** Edit [`the_api/views.py`](../the_api/views.py) to match the following:
    <details>
    <summary>Sample <code>the_api/views.py</code> implementation:</summary>

        from django.contrib.auth.models import User, Group
        from rest_framework import viewsets
        from rest_framework import permissions

        from .serializers import UserSerializer, GroupSerializer


        class UserViewSet(viewsets.ModelViewSet):
            """
            API endpoint that allows users to be viewed or edited.
            """
            queryset = User.objects.all().order_by('-date_joined')
            serializer_class = UserSerializer
            permission_classes = [permissions.IsAuthenticated]


        class GroupViewSet(viewsets.ModelViewSet):
            """
            API endpoint that allows groups to be viewed or edited.
            """
            queryset = Group.objects.all()
            serializer_class = GroupSerializer
            permission_classes = [permissions.IsAuthenticated]

    </details>

1. Add routes for the API to `urlpatterns` in [`the_project/urls.py`](../the_project/urls.py):
    <details>
    <summary>Sample <code></code> implementation:</summary>

        urlpatterns = [
            #...
            path('api/v1/', include('the_api.urls')),
            path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
            #...

        ]
    </details>

1. **ACTION:** Create [`the_api/urls.py`](../the_api/urls.py) and add the following implementation:
    <details>
    <summary>Sample <code>the_api/urls.p</code> implementation:</summary>

        from django.urls import include, path
        from rest_framework import routers
        
        from . import views
        
        
        router = routers.DefaultRouter()
        router.register(r'users-api-url', views.UserViewSet, basename='users_url_namespace')
        router.register('groups-api-url', views.GroupViewSet, basename='groups_url_namespace')
        
        urlpatterns = router.urls + [
        
        ]

    </details>

1. **ACTION:** Add the following to [`the_project/settings.py`](../the_project/settings.py):
    <details>
    <summary>Sample addition of <code>rest_framework</code> to <code>INSTALLED_APPS</code> in <code>the_project/settings.py</code> implementation:</summary>

        INSTALLED_APPS = [
            #...
            'rest_framework',
            #...
        ]
    </details>

    <details>
    <summary>Sample addition of <code>REST_FRAMEWORK</code> to <code>the_project/settings.py</code> implementation:</summary>

        REST_FRAMEWORK = {
            'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
            'PAGE_SIZE': 7
        }
    </details>

1. Start development server:
    * `python .\manage.py runserver`

1. Open internet browser to test Django REST Browsable API Interface:
    * http://localhost:8000/the-api/v1/
    * http://localhost:8000/the-api/v1/users-api-url/
    * http://localhost:8000/the-api/v1/users-api-url/1/
    * http://localhost:8000/the-api/v1/users-api-url/2/
    * http://localhost:8000/the-api/v1/groups-api-url/

1. API functions. But breaks if a `Group` is added to the database.

1. Will test further.
