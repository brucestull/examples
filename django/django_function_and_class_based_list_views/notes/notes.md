# Notes

## Resources:
* [Writing your first Django app, part 1 - djangoproject.com](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)
* [How to start a Django project  (PDXCG Style)](https://github.com/PdxCodeGuild/class_otter/blob/main/3%20Django/docs/Django%20Project%20Setup.md)
* [Django - General Index](https://docs.djangoproject.com/en/4.0/genindex/)
* [Django - Module Index](https://docs.djangoproject.com/en/4.0/py-modindex/)
* [Django - w3schools](https://www.w3schools.com/django/)
* [Django - MDN](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
* Links for [inherited](https://www.w3schools.com/python/python_inheritance.asp) views:
    * [Built-in class-based views API](https://docs.djangoproject.com/en/4.0/ref/class-based-views/)
    * [`View`](https://docs.djangoproject.com/en/4.0/ref/class-based-views/base/#view)
    * [`TemplateView`](https://docs.djangoproject.com/en/4.0/ref/class-based-views/base/#templateview)
    * [`ListView`](https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-display/#listview)

## Development server links and such:
* `python .\manage.py runserver`
* http://localhost:8000/admin/
* http://localhost:8000/the-app/index/
* http://localhost:8000/the-app/function-view/
* http://localhost:8000/the-app/class-view/
* http://localhost:8000/the-app/class-template-view/
* http://localhost:8000/the-app/class-list-view/

## Process:

1. Create virtual environment and install Django 4.0:
    * `pipenv install django==4.0`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views> pipenv install django==4.0
            Creating a virtualenv for this project...
            Pipfile: C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views\Pipfile
            Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.6) to create virtualenv...
            [   =] Creating virtual environment...created virtual environment CPython3.10.6.final.0-64 in 412ms
            creator CPython3Windows(dest=C:\Users\Bruce\.virtualenvs\django_function_and_class_based_views-KMseypp5, clear=False, no_vcs_ignore=False, global=False)
            seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Bruce\AppData\Local\pypa\virtualenv)
                added seed packages: pip==22.2.2, setuptools==63.2.0, wheel==0.37.1
            activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

            Successfully created virtual environment!
            Virtualenv location: C:\Users\Bruce\.virtualenvs\django_function_and_class_based_views-KMseypp5
            Installing django==4.0...
            Adding django to Pipfile's [packages]...
            Installation Succeeded
            Pipfile.lock not found, creating...
            Locking [dev-packages] dependencies...
            Locking [packages] dependencies...
                    Building requirements...
            Resolving dependencies...
            Success!
            Updated Pipfile.lock (036cf0)!
            Installing dependencies from Pipfile.lock (036cf0)...
            ================================ 0/0 - 00:00:00
            To activate this project's virtualenv, run pipenv shell.
            Alternatively, run a command inside the virtualenv with pipenv run.
            PS C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views>
            ```

1. Activate virtual environment:
    * `pipenv shell`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views> pipenv shell
            Launching subshell in virtual environment...
            PowerShell 7.2.5
            Copyright (c) Microsoft Corporation.

            https://aka.ms/powershell
            Type 'help' to get help.

            PS C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views>
            ```

1. Create Django project skeleton:
    * `django-admin startproject the_project .`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views> django-admin startproject the_project .
            PS C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views>
            ```

1. Examine directory structure:
    * `tree /f /a`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   manage.py
            |   Pipfile
            |   Pipfile.lock
            |
            +---notes
            |       notes.md
            |
            \---the_project
                    asgi.py
                    settings.py
                    urls.py
                    wsgi.py
                    __init__.py

            PS C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views>
            ```

1. Test development server:
    * `python .\manage.py runserver`
    * http://localhost:8000/

1. Create the app `the_app`:
    * `python .\manage.py startapp the_app`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views> python .\manage.py startapp the_app
            PS C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views>
            ```

1. Examine directory structure:
    * `tree /f /a`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   db.sqlite3
            |   manage.py
            |   Pipfile
            |   Pipfile.lock
            |
            +---notes
            |       notes.md
            |
            +---the_app
            |   |   admin.py
            |   |   apps.py
            |   |   models.py
            |   |   tests.py
            |   |   views.py
            |   |   __init__.py
            |   |
            |   \---migrations
            |           __init__.py
            |
            \---the_project
                    asgi.py
                    settings.py
                    urls.py
                    wsgi.py
                    __init__.py

            PS C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views>
            ```

1. Add the application config for our app `'the_app.apps.TheAppConfig'` to `INSTALLED_APPS` list in [`the_project\settings.py`](../the_project/settings.py):
    ```
    INSTALLED_APPS = [
        ...
        'the_app.apps.TheAppConfig',
        ...
    ]
    ```
    * Relavent concepts:
        * [`django.apps`](https://docs.djangoproject.com/en/4.0/ref/applications/)
        * [`AppConfig`](https://docs.djangoproject.com/en/4.0/ref/applications/#application-configuration)
        * [`INSTALLED_APPS`](https://docs.djangoproject.com/en/4.0/ref/settings/#installed-apps)

1. Create a basic view which returns an `HttpResponse` for testing:
    * Add an `index` view function to [`the_app\views.py`](../the_app/views.py):
        ```
        from django.http import HttpResponse

        def index(request):
            response_string = "Looks like we might have successful request-response!"
            return HttpResponse(response_string)
        ```
    * Relevent concepts:
        * [`django.http`](https://docs.djangoproject.com/en/4.0/ref/request-response/)
        * [`HttpResponse` objects](https://docs.djangoproject.com/en/4.0/ref/request-response/#httpresponse-objects)
        * [`def`](https://www.w3schools.com/python/python_functions.asp)

1. Create a URL route `index` for the `index` view:
    * Create [`the_app\urls.py`](../the_app/urls.py) and add following contents:
        ```
        from django.urls import path
        from . import views

        app_name = 'app_name_in_html'
        urlpatterns = [
            path('index/', views.index, name='index'),
        ]
        ```
    * We added a `path()` object with following arguments to `urlpatterns` list:
        * `index/` is the `route` argument.
        * `views.index` is the `view` argument.
        * `name='index'` is the `name` argument.
    * Relevent links:
        * [`django.urls`](https://docs.djangoproject.com/en/4.0/ref/urls/)
        * [`path()`](https://docs.djangoproject.com/en/4.0/ref/urls/#path)
        * [URL namespaces and included URLconfs](https://docs.djangoproject.com/en/4.1/topics/http/urls/#url-namespaces-and-included-urlconfs) to test out if `app_name_in_html` will work.

1. Modify [`the_project\urls.py`](../the_project/urls.py) as follows:
    * Add import for `include()` from `django.urls`.
    * Add `path()` constructor with arguments to `urlpatterns` list.
        * `the-app/` url route.
        * `'the_app.urls'` namespace.
    ```
    from django.urls import path, include

    urlpatterns = [
        ...
        path('the-app/', include('the_app.urls')),
        ...
    ]
    ```

1. Test the route we just made in development server:
    * `python .\manage.py runserver`
    * http://localhost:8000/the-app/index/
    * The string `response_string` displays in internet browser.

1. Investigate some properties of the `request` object:
    * `request.__dict__`
    * `request.environ.keys()`

1. Perform `migrate`:
    * `python .\manage.py migrate`

1. Make migrations for app `the_app`:
    * `python .\manage.py makemigrations the_app`

1. Perform `migrate`:
    * `python .\manage.py migrate`

1. Table name for `the_app`s model `StringValue`:
    * `the_app_stringvalue`

1. Create `superuser`:
    * `python .\manage.py createsuperuser`

1. Test `admin/` and `the_app/index/` endpoints:
    * `python .\manage.py runserver`
    * http://localhost:8000/the-app/index/
    * http://localhost:8000/admin/


1. Model doesn't show in `admin` view. Need to add the model to [`the_app\admin.py`](../the_app/admin.py):
    ```
    from django.contrib import admin
    from .models import StringValue

    admin.site.register(StringValue)
    ```
    * Relevent links:
        * [`django.contrib.admin`](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/)
        * [`admin.site.urls` on stackoverflow](https://stackoverflow.com/a/21247209)
        * [Project Board issue to document understanding `admin.site.urls`](https://github.com/brucestull/examples/issues/1)
        * [`AdminSite` methods](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#adminsite-methods)

1. Edited `name` and `verbose_name` for `StringValue`. Need to do migrations?

1. Perform migrations:
    * `python .\manage.py makemigrations`
    * `python .\manage.py migrate`

1. Create a function-based view `function_view` in [`the_app\views.py`](../the_app/views.py). We will temporarily just print the `QueryDict` info to console:
    ```
    def function_view(request):
        """
        Function-based view to show a list view of model `StringValue`.
        """
        the_string_values = StringValue.objects.all()
        print('the_string_values', the_string_values)
        print('type(the_string_values)', type(the_string_values))
        pass
    ```

1. Add `path()` for `function-view` to [`the_app\urls.py`](../the_app/urls.py):
    ```
    urlpatterns = [
        ...
        path('function-view', views.function_view, name='function_view'),
        ...
    ]
    ```

1. Test development server:
    * `python .\manage.py runserver`
    * http://localhost:8000/admin/
    * http://localhost:8000/the-app/index/
    * http://localhost:8000/the-app/function-view/

1. Error on http://localhost:8000/the-app/function-view/:
    ```
    Page not found (404)
    Request Method:	GET
    Request URL:	http://localhost:8000/the-app/function-view/
    Using the URLconf defined in the_project.urls, Django tried these URL patterns, in this order:

    admin/
    the-app/ index/ [name='index']
    the-app/ function-view [name='function_view']
    The current path, the-app/function-view/, didn’t match any of these.

    You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.
    ```

1. Thought I might need to add the trailing `/` to route for `function-view`.
    * Modify [`the_app\urls.py`](../the_app/urls.py):
        ```
        urlpatterns = [
            ...
            path('function-view/', views.function_view, name='function_view'),
            ...
        ]
        ```

1. Test development server:
    * `python .\manage.py runserver`
    * http://localhost:8000/admin/
    * http://localhost:8000/the-app/index/
    * http://localhost:8000/the-app/function-view/

1. Error on http://localhost:8000/the-app/function-view/:
    ```
    ValueError at /the-app/function-view/
    The view the_app.views.function_view didn't return an HttpResponse object. It returned None instead.
    Request Method:	GET
    Request URL:	http://localhost:8000/the-app/function-view/
    Django Version:	4.0
    Exception Type:	ValueError
    Exception Value:	
    The view the_app.views.function_view didn't return an HttpResponse object. It returned None instead.
    Exception Location:	C:\Users\Bruce\.virtualenvs\django_function_and_class_based_views-KMseypp5\lib\site-packages\django\core\handlers\base.py, line 309, in check_response
    Python Executable:	C:\Users\Bruce\.virtualenvs\django_function_and_class_based_views-KMseypp5\Scripts\python.exe
    Python Version:	3.10.6
    Python Path:	
    ['C:\\Users\\Bruce\\Programming\\examples\\django\\django_function_and_class_based_views',
    'C:\\Users\\Bruce\\Programming',
    'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip',
    'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\DLLs',
    'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\lib',
    'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310',
    'C:\\Users\\Bruce\\.virtualenvs\\django_function_and_class_based_views-KMseypp5',
    'C:\\Users\\Bruce\\.virtualenvs\\django_function_and_class_based_views-KMseypp5\\lib\\site-packages']
    Server time:	Mon, 22 Aug 2022 00:16:45 +0000
    ```

1. `function-view/` view found but still failed since it didn't return an `HttpResponse` object.

1. Modify [`the_app\views.py`](../the_app/views.py) to have it return an `HttpResponse` object:
    ```
    def function_view(request):
        """
        Function-based view to show a list view of model `StringValue`.
        """
        the_string_values = StringValue.objects.all()
        context = {
            'the_string_things': the_string_values
        }
        return render(request, 'the_app/the_app_template.html', context)
    ```

1. `function_view` view works as expected.

1. Create a class-based view in [`the_app\views.py`](../the_app/views.py):
    ```
    class ClassView(View):
        """
        Class-based view inheriting `View`.
        """
        def get(delf, request):
            the_string_values = StringValue.objects.all()
            context = {
                'the_string_things': the_string_values
            }
            return render(request, 'the_app/the_app_template.html', context)
    ```

1. Add `path()` for `ClassView` to `urlpatterns` in [`the_app\urls.py`](../the_app/urls.py):
    ```
    urlpatterns = [
        ...
        path('class-view/', views.ClassView.as_view(), name='class_view'),
        ...
    ]
    ```

1. Test development server:
    * `python .\manage.py runserver`
    * http://localhost:8000/admin/
    * http://localhost:8000/the-app/index/
    * http://localhost:8000/the-app/function-view/
    * http://localhost:8000/the-app/class-view/

1. `class-view` view works as expected.

1. Create class-based template view `ClassTemplateView` in [`the_app\views.py`](../the_app/views.py):
    ```
    class ClassTemplateView(TemplateView):
        template_name = 'the_app_template.html'
        def get_context_data(self, **kwargs):
            context = super.get_context_data(**kwargs)
            context['the_string_things'] = StringValue.objects.all()
            return context
    ```

1. Add `path()` for `ClassTemplateView` to `urlpatterns` in [`the_app\urls.py`](../the_app/urls.py):
    ```
    urlpatterns = [
        ...
        path('class-template-view/', TemplateView.as_view(), name='class_template_view'),
        ...
    ]
    ```

1. Test development server:
    * `python .\manage.py runserver`
    * http://localhost:8000/admin/
    * http://localhost:8000/the-app/index/
    * http://localhost:8000/the-app/function-view/
    * http://localhost:8000/the-app/class-view/
    * http://localhost:8000/the-app/class-template-view/

1. `class-template-view` view fails:
    ```
    ImproperlyConfigured at /the-app/class-template-view/
    TemplateResponseMixin requires either a definition of 'template_name' or an implementation of 'get_template_names()'
    Request Method:	GET
    Request URL:	http://localhost:8000/the-app/class-template-view/
    Django Version:	4.0
    Exception Type:	ImproperlyConfigured
    Exception Value:	
    TemplateResponseMixin requires either a definition of 'template_name' or an implementation of 'get_template_names()'
    Exception Location:	C:\Users\Bruce\.virtualenvs\django_function_and_class_based_views-KMseypp5\lib\site-packages\django\views\generic\base.py, line 150, in get_template_names
    Python Executable:	C:\Users\Bruce\.virtualenvs\django_function_and_class_based_views-KMseypp5\Scripts\python.exe
    Python Version:	3.10.6
    Python Path:	
    ['C:\\Users\\Bruce\\Programming\\examples\\django\\django_function_and_class_based_views',
    'C:\\Users\\Bruce\\Programming',
    'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip',
    'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\DLLs',
    'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\lib',
    'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310',
    'C:\\Users\\Bruce\\.virtualenvs\\django_function_and_class_based_views-KMseypp5',
    'C:\\Users\\Bruce\\.virtualenvs\\django_function_and_class_based_views-KMseypp5\\lib\\site-packages']
    Server time:	Mon, 22 Aug 2022 01:01:18 +0000
    ```

1. Try different `template_name` in `ClassTemplateView` by adding `the_app/` to route:
    ```
    class ClassTemplateView(TemplateView):
        template_name = 'the_app/the_app_template.html'
        def get_context_data(self, **kwargs):
            context = super.get_context_data(**kwargs)
            context['the_string_things'] = StringValue.objects.all()
            return context
    ```

1. `class-template-view` view fails:
    ```
    ImproperlyConfigured at /the-app/class-template-view/
    TemplateResponseMixin requires either a definition of 'template_name' or an implementation of 'get_template_names()'
    Request Method:	GET
    Request URL:	http://localhost:8000/the-app/class-template-view/
    Django Version:	4.0
    Exception Type:	ImproperlyConfigured
    Exception Value:	
    TemplateResponseMixin requires either a definition of 'template_name' or an implementation of 'get_template_names()'
    Exception Location:	C:\Users\Bruce\.virtualenvs\django_function_and_class_based_views-KMseypp5\lib\site-packages\django\views\generic\base.py, line 150, in get_template_names
    Python Executable:	C:\Users\Bruce\.virtualenvs\django_function_and_class_based_views-KMseypp5\Scripts\python.exe
    Python Version:	3.10.6
    Python Path:	
    ['C:\\Users\\Bruce\\Programming\\examples\\django\\django_function_and_class_based_views',
    'C:\\Users\\Bruce\\Programming',
    'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip',
    'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\DLLs',
    'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\lib',
    'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310',
    'C:\\Users\\Bruce\\.virtualenvs\\django_function_and_class_based_views-KMseypp5',
    'C:\\Users\\Bruce\\.virtualenvs\\django_function_and_class_based_views-KMseypp5\\lib\\site-packages']
    Server time:	Mon, 22 Aug 2022 01:04:41 +0000
    ```

1. Try adding `template_name='the_app_template.html'` to `path(TemplateView.as_view())` in `urlpatterns` in [`the_app\urls.py`](../the_app/urls.py) and removing `template_name` from `ClassTemplateView` in [`the_app\views.py`](../the_app/views.py):
    ```
    urlpatterns = [
        ...
        path('class-template-view/', TemplateView.as_view(template_name='the_app_template.html'), name='class_template_view'),
        ...
    ]
    ```
    ```
    class ClassTemplateView(TemplateView):
        # template_name = 'the_app/the_app_template.html'
        def get_context_data(self, **kwargs):
            context = super.get_context_data(**kwargs)
            context['the_string_things'] = StringValue.objects.all()
            return context
    ```

1. Test development server:
    * `python .\manage.py runserver`
    * http://localhost:8000/admin/
    * http://localhost:8000/the-app/index/
    * http://localhost:8000/the-app/function-view/
    * http://localhost:8000/the-app/class-view/
    * http://localhost:8000/the-app/class-template-view/

1. `class-template-view` view fails:
    ```
    TemplateDoesNotExist at /the-app/class-template-view/
    the_app_template.html
    Request Method:	GET
    Request URL:	http://localhost:8000/the-app/class-template-view/
    Django Version:	4.0
    Exception Type:	TemplateDoesNotExist
    Exception Value:	
    the_app_template.html
    Exception Location:	C:\Users\Bruce\.virtualenvs\django_function_and_class_based_views-KMseypp5\lib\site-packages\django\template\loader.py, line 47, in select_template
    Python Executable:	C:\Users\Bruce\.virtualenvs\django_function_and_class_based_views-KMseypp5\Scripts\python.exe
    Python Version:	3.10.6
    Python Path:	
    ['C:\\Users\\Bruce\\Programming\\examples\\django\\django_function_and_class_based_views',
    'C:\\Users\\Bruce\\Programming',
    'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip',
    'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\DLLs',
    'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\lib',
    'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310',
    'C:\\Users\\Bruce\\.virtualenvs\\django_function_and_class_based_views-KMseypp5',
    'C:\\Users\\Bruce\\.virtualenvs\\django_function_and_class_based_views-KMseypp5\\lib\\site-packages']
    Server time:	Mon, 22 Aug 2022 01:10:55 +0000
    ```

1. Try adding `the_app/` to `template_name` in `urlpatterns`:
    ```
    urlpatterns = [
        ...
        path('class-template-view/', TemplateView.as_view(template_name='the_app/the_app_template.html'), name='class_template_view'),
        ...
    ]
    ```

1. `class-template-view` view fails with blank screen. So context not set up properly, maybe.

1. Maybe forgot `()` on `super` in `context` part of `ClassTemplateView` in [`the_app\views.py`](../the_app/views.py):
    ```
    class ClassTemplateView(TemplateView):
            ...
            context = super.get_context_data(**kwargs)
            ...
    ```

1. Add `()` on `super` in `context` part of `ClassTemplateView` in [`the_app\views.py`](../the_app/views.py):
    ```
    class ClassTemplateView(TemplateView):
            ...
            context = super().get_context_data(**kwargs)
            ...
    ```

1. Test development server:
    * `python .\manage.py runserver`
    * http://localhost:8000/admin/
    * http://localhost:8000/the-app/index/
    * http://localhost:8000/the-app/function-view/
    * http://localhost:8000/the-app/class-view/
    * http://localhost:8000/the-app/class-template-view/

1. `class-template-view` view fails. Had incorrect `TemplateView.as_view()` in `urlpatterns` in [`the_app\urls.py`](../the_app/urls.py):
    ```
    urlpatterns = [
        ...
        path(
            'class-template-view/',
            TemplateView.as_view(template_name='the_app/the_app_template.html'), # Error here
            name='class_template_view'
        ),
        ...
    ]
    ```

1. Change `TemplateView.as_view` to `views.ClassTemplateView.as_view` in `urlpatterns` in [`the_app\urls.py`](../the_app/urls.py):
    ```
    urlpatterns = [
        ...
        path(
            ...
            views.ClassTemplateView.as_view(
                ...
            ),
            ...
        ),
        ...
    ]
    ```
    * Relevent link:
        * [`TemplateView`](https://docs.djangoproject.com/en/3.2/ref/class-based-views/base/#templateview)

1. Test development server:
    * `python .\manage.py runserver`
    * http://localhost:8000/admin/
    * http://localhost:8000/the-app/index/
    * http://localhost:8000/the-app/function-view/
    * http://localhost:8000/the-app/class-view/
    * http://localhost:8000/the-app/class-template-view/

1. Create a `ListView` view called `ClassListView` in [`the_app\views.py`](../the_app/views.py):
    ```
    class ClassListView(generic.ListView):
        model = StringValue
        context_object_name = 'the_string_things'
        template_name = 'the_app/the_app_template.html'
    ```
    * Resource:
        * [`ListView`](https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-display/#listview)

1. Add `path()` for `ClassListView` in `urlpatterns` in [`the_app\urls.py`](../the_app/urls.py):
    ```
    urlpatterns = [
        ...
        path('class-list-view/', views.ClassListView.as_view(), name='class_list_view'),
        ...
    ]
    ```

1. Test development server:
    * `python .\manage.py runserver`
    * http://localhost:8000/admin/
    * http://localhost:8000/the-app/index/
    * http://localhost:8000/the-app/function-view/
    * http://localhost:8000/the-app/class-view/
    * http://localhost:8000/the-app/class-template-view/
    * http://localhost:8000/the-app/class-list-view/

1. Git action: Delete branches on the remote `origin`:
    * Branches to delete:
        * django-function-and-class-based-views
        * django-function-and-class-based-views-comments
    * Commands to delete the branches:
        * Reference:
            * [Deleting branches - git-tower.com](https://www.git-tower.com/learn/git/faq/delete-remote-branch)
        * `git push origin --delete django-function-and-class-based-views`
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views> git push origin --delete django-function-and-class-based-views
            To https://github.com/brucestull/examples.git
            - [deleted]         django-function-and-class-based-views
            PS C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views>
            ```
        * `git push origin --delete django-function-and-class-based-views-comments`
            ```
            PS C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views> git push origin --delete django-function-and-class-based-views-comments
            To https://github.com/brucestull/examples.git
            - [deleted]         django-function-and-class-based-views-comments
            PS C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views>
            ```

1. Have virtual environment issues with multiple django projects in same repository. Will try creating a repo-wide `pipenv`.

1. Remove `Pipfile` and `Pipfile.lock` from `examples\django\django_function_and_class_based_views`:
    * New directory contents:
        ```
        PS C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views> Get-ChildItem 

            Directory: C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views

        Mode                 LastWriteTime         Length Name
        ----                 -------------         ------ ----
        d----          2022-08-22    07:35                local_things
        d----          2022-08-22    07:35                notes
        d----          2022-08-22    07:35                the_app
        d----          2022-08-22    07:35                the_project
        -a---          2022-08-21    20:31         135168 db.sqlite3
        -a---          2022-08-21    22:52            689 manage.py

        PS C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views>
        ```

1. Delete the `django_function_and_class_based_views-KMseypp5` virtual environment.

1. Search repo for `Pipfile`:
    * `Get-ChildItem -Recurse -Filter 'Pipfile*'`
        ```
        PS C:\Users\Bruce\Programming\examples> Get-ChildItem -Recurse -Filter 'Pipfile*'
        PS C:\Users\Bruce\Programming\examples>
        ```

1. No results show, so let's search for something we know is in the repo so we can see if we are using proper command:
    * `Get-ChildItem -Recurse -Filter 'the_app_template*'`
        ```
        PS C:\Users\Bruce\Programming\examples> Get-ChildItem -Recurse -Filter 'the_app_template*'

            Directory: C:\Users\Bruce\Programming\examples\django\django_function_and_class_based_views\the_app\templates\the_app

        Mode                 LastWriteTime         Length Name
        ----                 -------------         ------ ----
        -a---          2022-08-21    22:57            195 the_app_template.html

        PS C:\Users\Bruce\Programming\examples>
        ```

1. It seems the search command worked. Now, create `pipenv` in root of repo:
    * `pipenv install django==4.0`
        ```
        ...
        Locking Failed!
        ...
        requests.exceptions.ConnectionError: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
        ...
        ```

1. `Locking Failed!` so try again:
    * `pipenv install django==4.0`
        ```
        PS C:\Users\Bruce\Programming\examples> pipenv install django==4.0
        Installing django==4.0...
        [====] Installing django...
        Installation Succeeded
        Pipfile.lock not found, creating...
        Locking [dev-packages] dependencies...
        Locking [packages] dependencies...
        Locking...Building requirements...
        Resolving dependencies...
        Success!
        Updated Pipfile.lock (036cf0)!
        Installing dependencies from Pipfile.lock (036cf0)...
        ================================ 0/0 - 00:00:00
        To activate this project's virtualenv, run pipenv shell.
        Alternatively, run a command inside the virtualenv with pipenv run.
        PS C:\Users\Bruce\Programming\examples>
        ```

1. Activate virtual environment:
    * `pipenv shell`
        ```
        PS C:\Users\Bruce\Programming\examples> pipenv shell
        Launching subshell in virtual environment...
        PowerShell 7.2.5
        Copyright (c) Microsoft Corporation.

        https://aka.ms/powershell
        Type 'help' to get help.

        PS C:\Users\Bruce\Programming\examples>
        ```

1. Verify `pipenv` Python interpreter:
    * `Get-Command python | fl *`
        ```
        PS C:\Users\Bruce\Programming\examples> Get-Command python | fl *

        HelpUri            : 
        FileVersionInfo    : File:             C:\Users\Bruce\.virtualenvs\examples-yqA5vS_k\Scripts\python.exe
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

        Path               : C:\Users\Bruce\.virtualenvs\examples-yqA5vS_k\Scripts\python.exe
        Extension          : .exe
        Definition         : C:\Users\Bruce\.virtualenvs\examples-yqA5vS_k\Scripts\python.exe
        Source             : C:\Users\Bruce\.virtualenvs\examples-yqA5vS_k\Scripts\python.exe
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


        PS C:\Users\Bruce\Programming\examples>
        ```

1. Confirm `pip list`:
    * `pip list`
        ```
        PS C:\Users\Bruce\Programming\examples> pip list
        Package    Version
        ---------- -------
        asgiref    3.5.2
        Django     4.0
        pip        22.2.2
        setuptools 63.2.0
        sqlparse   0.4.2
        tzdata     2022.2
        wheel      0.37.1
        PS C:\Users\Bruce\Programming\examples>
        ```

1. Set Python interpreter to workspace level so I don't have to use `pipenv shell` each time I start vscode.



