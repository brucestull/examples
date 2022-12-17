# Notes

## `django.contrib.auth`-provided URLs

```console
    users/login/ [name='login']
    users/logout/ [name='logout']
    users/password_change/ [name='password_change']
    users/password_change/done/ [name='password_change_done']
    users/password_reset/ [name='password_reset']
    users/password_reset/done/ [name='password_reset_done']
    users/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    users/reset/done/ [name='password_reset_complete']
```

## DEBUG Pages in Browser

### <http://localhost:8000/users/>

```console
Page not found (404)
Request Method: GET
Request URL: http://localhost:8000/users/
Using the URLconf defined in django_project.urls, Django tried these URL patterns, in this order:

[name='home']
admin/
users/ signup/ [name='signup']
users/ login/ [name='login']
users/ logout/ [name='logout']
users/ password_change/ [name='password_change']
users/ password_change/done/ [name='password_change_done']
users/ password_reset/ [name='password_reset']
users/ password_reset/done/ [name='password_reset_done']
users/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
users/ reset/done/ [name='password_reset_complete']
The current path, users/, didn’t match any of these.

You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.
```

### <http://localhost:8000/orange/>

```console
Page not found (404)
Request Method: GET
Request URL: http://localhost:8000/orange/
Using the URLconf defined in django_project.urls, Django tried these URL patterns, in this order:

[name='home']
admin/
users/
users/
The current path, orange/, didn’t match any of these.

You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.
```

* [`users/urls.py`](../users/urls.py):

    ```python
    urlpatterns = [
        path(
            '',
            TemplateView.as_view(template_name='home.html'),
            name='home'
        ),
        path('admin/', admin.site.urls),
        path('users/', include('users.urls')),
        path('users/', include('django.contrib.auth.urls')),
    ]
    ```
