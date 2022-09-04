# Project Setup

## Repository Links:
* [Examples Repository](../../../README.md)
* [Django REST - Basic - `README.me`](../README.md)

## Development server links and such:
* `python .\manage.py runserver`
* http://localhost:8000/admin/

## Tag meanings for this guide:
* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.

## Process:
1. Start inside project directory:
    * Sample directory location:
        * `C:\Users\Bruce\Programming\examples\django\rest_basic`

1. Create a new `pipenv` virtual environment:
    * `pipenv install django==4.0`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\rest_basic> pipenv install django==4.0
            Creating a virtualenv for this project...
            Pipfile: C:\Users\Bruce\Programming\examples\django\rest_basic\Pipfile
            Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.6) to create virtualenv...
            [ ===] Creating virtual environment...created virtual environment CPython3.10.6.final.0-64 in 2995ms
              creator CPython3Windows(dest=C:\Users\Bruce\.virtualenvs\rest_basic-8EvQpMVS, clear=False, no_vcs_ignore=False, global=False)
              seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Bruce\AppData\Local\pypa\virtualenv)
                added seed packages: pip==22.2.2, setuptools==63.4.3, wheel==0.37.1
              activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

            Successfully created virtual environment!
            Virtualenv location: C:\Users\Bruce\.virtualenvs\rest_basic-8EvQpMVS
            Creating a Pipfile for this project...
            Installing django==4.0...
            Adding django to Pipfile's [packages]...
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
            PS C:\Users\Bruce\Programming\examples\django\rest_basic>
        </details>

1. Activate the `pipenv` virtual environment:
    * `pipenv shell`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\rest_basic> pipenv shell
            Launching subshell in virtual environment...
            PowerShell 7.2.6
            Copyright (c) Microsoft Corporation.

            https://aka.ms/powershell
            Type 'help' to get help.

            PS C:\Users\Bruce\Programming\examples\django\rest_basic>
        </details>

1. Check installed packages:
    * `pip list`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\rest_basic> pip list
            Package    Version
            ---------- -------
            asgiref    3.5.2
            Django     4.0
            pip        22.2.2
            setuptools 63.4.3
            sqlparse   0.4.2
            tzdata     2022.2
            wheel      0.37.1
            PS C:\Users\Bruce\Programming\examples\django\rest_basic>
        </details>

1. Examine directory structure:
    * `tree /f /a`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\rest_basic> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   Pipfile
            |   Pipfile.lock
            |   README.md
            |
            \---notes
                    01_setup.md
                    commands_and_links.md

            PS C:\Users\Bruce\Programming\examples\django\rest_basic>
        </details>

1. Create a Django "Project":
    * `django-admin startproject the_project .`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\rest_basic> django-admin startproject the_project .
            PS C:\Users\Bruce\Programming\examples\django\rest_basic>
        </details>

1. Examine directory structure:
    * `tree /f /a`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\rest_basic> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   manage.py
            |   Pipfile
            |   Pipfile.lock
            |   README.md
            |
            +---notes
            |       01_setup.md
            |       commands_and_links.md
            |
            \---the_project
                    asgi.py
                    settings.py
                    urls.py
                    wsgi.py
                    __init__.py

            PS C:\Users\Bruce\Programming\examples\django\rest_basic>
        </details>

1. Test development server:
    * `python .\manage.py runserver`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\rest_basic> python .\manage.py runserver
            Watching for file changes with StatReloader
            Performing system checks...

            System check identified no issues (0 silenced).

            You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
            Run 'python manage.py migrate' to apply them.
            September 04, 2022 - 08:52:24
            Django version 4.0, using settings 'the_project.settings'
            Starting development server at http://127.0.0.1:8000/
            Quit the server with CTRL-BREAK.
        </details>

1. Open internet browser to server root:
    * http://localhost:8000/

1. Verify Django Green Rocket and success text:
    * Sample success text:
        * `The install worked successfully! Congratulations!`

1. Stop the development server:
    * \<Ctrl+C\>

1. Create Django app:
    * `python .\manage.py startapp the_api`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\rest_basic> python .\manage.py startapp the_api
            PS C:\Users\Bruce\Programming\examples\django\rest_basic>
        </details>

1. Perform migrations:
    * `python .\manage.py migrate`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\rest_basic> python .\manage.py migrate
            Operations to perform:
              Apply all migrations: admin, auth, contenttypes, sessions
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
            PS C:\Users\Bruce\Programming\examples\django\rest_basic>
        </details>

1. Create a superuser:
    * `python manage.py createsuperuser --email admin@email.app --username admin`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\rest_basic> python manage.py createsuperuser --email admin@email.app --username admin
            Password:
            Password (again):
            This password is too common.
            Bypass password validation and create user anyway? [y/N]: y
            Superuser created successfully.
            PS C:\Users\Bruce\Programming\examples\django\rest_basic>
        </details>

1. Start development server and test Django Admin Interface:
    * `python .\manage.py runserver`
    * http://localhost:8000/admin/
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\examples\django\rest_basic> python .\manage.py runserver
            Watching for file changes with StatReloader
            Performing system checks...

            System check identified no issues (0 silenced).
            September 04, 2022 - 09:04:24
            Django version 4.0, using settings 'the_project.settings'
            Starting development server at http://127.0.0.1:8000/
            Quit the server with CTRL-BREAK.
            [04/Sep/2022 09:04:29] "GET /admin/ HTTP/1.1" 302 0
            [04/Sep/2022 09:04:29] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 2215
            [04/Sep/2022 09:04:29] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 200 2616
            [04/Sep/2022 09:04:29] "GET /static/admin/css/base.css HTTP/1.1" 200 19513
            [04/Sep/2022 09:04:29] "GET /static/admin/css/login.css HTTP/1.1" 200 954
            [04/Sep/2022 09:04:29] "GET /static/admin/css/responsive.css HTTP/1.1" 200 18545
            [04/Sep/2022 09:04:29] "GET /static/admin/css/fonts.css HTTP/1.1" 304 0
            [04/Sep/2022 09:04:29] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 200 3401
            [04/Sep/2022 09:04:29] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 304 0
            [04/Sep/2022 09:04:29] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 304 0
            [04/Sep/2022 09:04:34] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
            [04/Sep/2022 09:04:34] "GET /admin/ HTTP/1.1" 200 3327
            [04/Sep/2022 09:04:34] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 380
            [04/Sep/2022 09:04:34] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380
            [04/Sep/2022 09:04:34] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
            [04/Sep/2022 09:04:34] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 304 0
        </details>

1. Add implementation of [The Django admin documentation generator](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/admindocs/):
    1. Add `django.contrib.admindocs` to `INSTALLED_APPS` in [`the_project/settings.py`](../the_project/settings.py).
    1. Add the following to [`the_project/urls.py`](../the_project/urls.py):
        1. Import for `include` from `django.urls`.
        1. `path` function (with arguments) to `URLPATTERNS` in [`the_project/urls.py`](../the_project/urls.py). Make sure to add if before the `admin/` entry.
            * `path('admin/doc/', include('django.contrib.admindocs.urls'))`
            <details>
            <summary>Relavent file edits:</summary>

                from django.urls import include

                urlpatterns = [
                    #...
                    path('admin/doc/', include('django.contrib.admindocs.urls')),
                    #...
                ]
            </details>
    1. Use `pipenv install`, since we are using a `pipenv` virtual environment, to install `docutils`. We don't use `pip install` when using a `pipenv`:
        * `pipenv install docutils==0.19`
            <details>
            <summary>Sample output (with failed install):</summary>

                PS C:\Users\Bruce\Programming\examples\django\rest_basic> pipenv install docutils==0.19
                Installing docutils==0.19...
                Adding docutils to Pipfile's [packages]...
                Installation Succeeded
                Pipfile.lock (036cf0) out of date, updating to (2d0928)...
                Locking [dev-packages] dependencies...
                Locking [packages] dependencies...
                Locking...
                Resolving dependencies...
                Locking Failed!

                Traceback (most recent call last):
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\connectionpool.py", line 699, in urlopen
                    httplib_response = self._make_request(
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\connectionpool.py", line 382, in _make_request
                    self._validate_conn(conn)
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\connectionpool.py", line 1010, in _validate_conn
                    conn.connect()
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\connection.py", line 411, in connect
                    self.sock = ssl_wrap_socket(
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\util\ssl_.py", line 449, in ssl_wrap_socket
                    ssl_sock = _ssl_wrap_socket_impl(
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\util\ssl_.py", line 493, in _ssl_wrap_socket_impl
                    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
                  File "C:\Users\Bruce\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 513, in wrap_socket
                    return self.sslsocket_class._create(
                  File "C:\Users\Bruce\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 1071, in _create
                    self.do_handshake()
                  File "C:\Users\Bruce\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 1342, in do_handshake
                    self._sslobj.do_handshake()
                ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host
                During handling of the above exception, another exception occurred:
                Traceback (most recent call last):
                  File "C:\Users\Bruce\.local\pipx\venvs\pipenv\Lib\site-packages\pipenv\vendor\requests\adapters.py", line 439, in send
                    resp = conn.urlopen(
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\connectionpool.py", line 755, in urlopen
                    retries = retries.increment(
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\util\retry.py", line 532, in increment
                    raise six.reraise(type(error), error, _stacktrace)
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\packages\six.py", line 769, in reraise
                    raise value.with_traceback(tb)
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\connectionpool.py", line 699, in urlopen
                    httplib_response = self._make_request(
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\connectionpool.py", line 382, in _make_request
                    self._validate_conn(conn)
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\connectionpool.py", line 1010, in _validate_conn
                    conn.connect()
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\connection.py", line 411, in connect
                    self.sock = ssl_wrap_socket(
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\util\ssl_.py", line 449, in ssl_wrap_socket
                    ssl_sock = _ssl_wrap_socket_impl(
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\util\ssl_.py", line 493, in _ssl_wrap_socket_impl
                    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
                  File "C:\Users\Bruce\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 513, in wrap_socket
                    return self.sslsocket_class._create(
                  File "C:\Users\Bruce\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 1071, in _create
                    self.do_handshake()
                  File "C:\Users\Bruce\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 1342, in do_handshake
                    self._sslobj.do_handshake()
                pipenv.vendor.urllib3.exceptions.ProtocolError: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
                During handling of the above exception, another exception occurred:
                Traceback (most recent call last):
                  File "C:\Users\Bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\resolver.py", line 766, in <module>
                    main()
                  File "C:\Users\Bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\resolver.py", line 760, in main
                    _main(parsed.pre, parsed.clear, parsed.verbose, parsed.system, parsed.write,
                  File "C:\Users\Bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\resolver.py", line 743, in _main
                    resolve_packages(pre, clear, verbose, system, write, requirements_dir, packages, dev)
                  File "C:\Users\Bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\resolver.py", line 704, in resolve_packages
                    results, resolver = resolve(
                  File "C:\Users\Bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\resolver.py", line 685, in resolve
                    return resolve_deps(
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\utils.py", line 1377, in resolve_deps
                    results, hashes, markers_lookup, resolver, skipped = actually_resolve_deps(
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\utils.py", line 1107, in actually_resolve_deps
                    hashes = resolver.resolve_hashes()
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\utils.py", line 981, in resolve_hashes
                    self.hashes[ireq] = self.collect_hashes(ireq)
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\utils.py", line 966, in collect_hashes
                    hashes = self._get_hashes_from_pypi(ireq)
                  File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\utils.py", line 928, in _get_hashes_from_pypi
                    r = session.get(pkg_url, timeout=10)
                  File "C:\Users\Bruce\.local\pipx\venvs\pipenv\Lib\site-packages\pipenv\vendor\requests\sessions.py", line 555, in get
                    return self.request('GET', url, **kwargs)
                  File "C:\Users\Bruce\.local\pipx\venvs\pipenv\Lib\site-packages\pipenv\vendor\requests\sessions.py", line 542, in request
                    resp = self.send(prep, **send_kwargs)
                  File "C:\Users\Bruce\.local\pipx\venvs\pipenv\Lib\site-packages\pipenv\vendor\requests\sessions.py", line 655, in send
                    r = adapter.send(request, **kwargs)
                  File "C:\Users\Bruce\.local\pipx\venvs\pipenv\Lib\site-packages\pipenv\vendor\requests\adapters.py", line 498, in send
                    raise ConnectionError(err, request=request)
                requests.exceptions.ConnectionError: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))

                PS C:\Users\Bruce\Programming\examples\django\rest_basic>
            </details>
            <details>
            <summary>Sample output (with succuessful install):</summary>

                PS C:\Users\Bruce\Programming\examples\django\rest_basic> pipenv install docutils==0.19
                Installing docutils==0.19...
                Adding docutils to Pipfile's [packages]...
                Installation Succeeded
                Pipfile.lock (036cf0) out of date, updating to (2d0928)...
                Locking [dev-packages] dependencies...
                Locking [packages] dependencies...
                           Building requirements...
                Resolving dependencies...
                Success!
                Updated Pipfile.lock (2d0928)!
                Installing dependencies from Pipfile.lock (2d0928)...
                  ================================ 0/0 - 00:00:00
                PS C:\Users\Bruce\Programming\examples\django\rest_basic>
            </details>

1. Start development server and test Django Admin Interface:
    * `python .\manage.py runserver`

1. Open interpreter browser to server admin interface URL (login if necessary):
    * http://localhost:8000/admin/

1. Check that `DOCUMENTATION` link functions properly.



