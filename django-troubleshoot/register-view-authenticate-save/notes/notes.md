# Test of User Management with Forms

## Resources:
* [Django Docs - Module Index](https://docs.djangoproject.com/en/4.1/py-modindex/)
* [Django Docs - General Index](https://docs.djangoproject.com/en/4.1/genindex/)
* [`pillow` - pypi.org](https://pypi.org/project/Pillow/)
* [`pillow` - python-pillow.org](https://python-pillow.org/)
* [ModelForm - docs.djangoproject.com](https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/#modelform)
* [save() - docs.djangoproject.com](https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/#the-save-method)
* [`authenticate()`](https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.authenticate)

## Official process:
1. Add `print()` executions for troubleshooting:
    <details>
    <summary>Sample <code>register</code> view function in <code>users\views.py</code> contents:</summary>

        def register(request):
            if request.method == 'POST':
                print('request.POST: ', request.POST)
                form =  NewUserForm(request.POST)
        
                if form.is_valid():
        
                    username = form.cleaned_data.get('username')
                    print('username: ', username)
                    raw_password = form.cleaned_data.get('password1')
                    print('raw_password: ', raw_password)
                    email = form.cleaned_data.get('email')
                    print('email: ', email)
        
                    user = authenticate(username=username, password=raw_password, email=email)
                    print('authenticate(username=username, password=raw_password, email=email): ', authenticate(username=username, password=raw_password, email=email))
                    print('User.objects.all() after authenticate(): ', User.objects.all())
                    print('user: ', user)
                    the_form = form.save()
                    print('User.objects.all() after form.save(): ', User.objects.all())
                    print('the_form: ', the_form)
                    print('type(the_form): ', type(the_form))
                    login(request, user)
        
                    return redirect('index')
            else:
                form = NewUserForm()
            return render(request, 'registration/register.html', {'form': form})
    </details>

1. Check that I haven't changed the actual functionality of the code:
    * `git diff .\users\views.py`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\class_HB2\code\Ronnie\user_management_w_forms> git diff .\users\views.py
            diff --git a/code/Ronnie/user_management_w_forms/users/views.py b/code/Ronnie/user_management_w_forms/users/views.py
            index 9bc5a50..44bcb23 100644
            --- a/code/Ronnie/user_management_w_forms/users/views.py
            +++ b/code/Ronnie/user_management_w_forms/users/views.py
            @@ -3,22 +3,33 @@ from django.contrib.auth import login, authenticate
            from .forms import NewUserForm
            from django.contrib.auth.decorators import login_required
            
            +from .models import User
            +
            @login_required
            def profile(request):
                return render(request, 'registration/profile.html', {'user': request.user})
            
            def register(request):
                if request.method == 'POST':
            +        print('request.POST: ', request.POST)
                    form =  NewUserForm(request.POST)
            
                    if form.is_valid():
            
                        username = form.cleaned_data.get('username')
            +            print('username: ', username)
                        raw_password = form.cleaned_data.get('password1')
            +            print('raw_password: ', raw_password)
                        email = form.cleaned_data.get('email')
            +            print('email: ', email)
            
                        user = authenticate(username=username, password=raw_password, email=email)
            -            form.save()
            +            print('authenticate(username=username, password=raw_password, email=email): ', authenticate(username=username, password=raw_password, email=email))
            +            print('User.objects.all() after authenticate(): ', User.objects.all())
            +            print('user: ', user)
            +            the_form = form.save()
            +            print('User.objects.all() after form.save(): ', User.objects.all())
            +            print('the_form: ', the_form)
            +            print('type(the_form): ', type(the_form))
                        login(request, user)
            
                        return redirect('index')
            PS C:\Users\Bruce\Programming\class_HB2\code\Ronnie\user_management_w_forms>
        </details>

1. Perfom migrations:
    1. `python .\manage.py makemigrations users`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\class_HB2\code\Ronnie\user_management_w_forms> python .\manage.py makemigrations users
            Migrations for 'users':
            users\migrations\0001_initial.py
                - Create model Profile
            PS C:\Users\Bruce\Programming\class_HB2\code\Ronnie\user_management_w_forms>
        </details>
    1. `python .\manage.py migrate`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\class_HB2\code\Ronnie\user_management_w_forms> python .\manage.py migrate
            Operations to perform:
            Apply all migrations: admin, auth, contenttypes, sessions, users
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
            Applying users.0001_initial... OK
            PS C:\Users\Bruce\Programming\class_HB2\code\Ronnie\user_management_w_forms>
        </details>

1. Create a `superuser`:
    * `python manage.py createsuperuser --email admin@email.app --username admin`
    * username: `admin`
    * password: `password`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\class_HB2\code\Ronnie\user_management_w_forms> python manage.py createsuperuser --email admin@email.app --username admin
            Password:
            Password (again):
            This password is too common.
            Bypass password validation and create user anyway? [y/N]: y
            Superuser created successfully.
            PS C:\Users\Bruce\Programming\class_HB2\code\Ronnie\user_management_w_forms>
        </details>

1. Test Django Admin Interface:
    1. `python .\manage.py runserver`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\class_HB2\code\Ronnie\user_management_w_forms> python .\manage.py runserver
            Watching for file changes with StatReloader
            Performing system checks...
            
            System check identified no issues (0 silenced).
            September 12, 2022 - 09:38:34
            Django version 4.0, using settings 'project.settings'
            Starting development server at http://127.0.0.1:8000/
            Quit the server with CTRL-BREAK.
        </details>
    1. Open internet browser to Django Admin Interface URL:
        * http://localhost:8000/admin/
    1. Log in using superuser credentials provided above:
        * SUCCESS
    1. Add a new (non-superuser) user:
        * Credentials:
            * username: `NotAnAdmin`
            * password: `1234test`
        * SUCCESS
    1. Delete `User` `NotAnAdmin` in Django Admin Interface:
        * SUCCESS
    1. Add a new (non-superuser) user (in Django Admin Interface) for login testing:
        * Credentials:
            * username: `NotAnAdmin`
            * password: `1234test`
        * SUCCESS

1. Test application login:
    1. Ensure no user is logged in.
    1. Open browser to application root:
        * http://localhost:8000/
    1. Click `Sign-In` link:
        * SUCCESS
            * Routed to a login page.
    1. Enter `NotAnAdmin` credentials provided above:
        * Credentials:
            * username: `NotAnAdmin`
            * password: `1234test`
    1. Click `Sing In` button:
        * SUCCESS

1. Test user creation in the application:
    1. Ensure no user is logged in.
    1. Open browser to application root:
        * http://localhost:8000/
    1. Click `Sign-Up` link:
        * SUCCESS
            * Routed to a sign up page.
    1. Enter user credentials:
        * Credentials:
            * username: `NotAnotherAdmin`
            * password: `1234test`
    1. Click `Sign Up` button:
        * Exception in browser:
            * `Exception Value:	'AnonymousUser' object has no attribute '_meta'`
        * AttributeError in console:
            * `AttributeError: 'AnonymousUser' object has no attribute '_meta'`
                <details>
                <summary>Sample output:</summary>

                    request.POST:  <QueryDict:
                        {
                            'csrfmiddlewaretoken': ['hbZpp0Tve1KGt5rQrTqpBDSyNZqqS02TnqEzchMaAUaViZpfVcSMUJKC8heDYzTs'],
                            'username': ['NotAnotherAdmin'],
                            'email': ['NotAnAdmin@email.app'],
                            'password1': ['1234test'],
                            'password2': ['1234test']
                        }
                    >
                    username:  NotAnotherAdmin
                    raw_password:  1234test
                    email:  NotAnAdmin@email.app
                    authenticate(username=username, password=raw_password, email=email):  None
                    User.objects.all() after authenticate():  <QuerySet [<User: admin>, <User: NotAnAdmin>]>
                    user:  None
                    User.objects.all() after form.save():  <QuerySet [<User: admin>, <User: NotAnAdmin>, <User: NotAnotherAdmin>]>
                    the_form:  NotAnotherAdmin
                    type(the_form):  <class 'django.contrib.auth.models.User'>
                    Internal Server Error: /accounts/register/
                    Traceback (most recent call last):
                    File "C:\Users\Bruce\.virtualenvs\user_management_w_forms-XHGniG9b\lib\site-packages\django\core\handlers\exception.py", line 47, in inner
                        response = get_response(request)
                    File "C:\Users\Bruce\.virtualenvs\user_management_w_forms-XHGniG9b\lib\site-packages\django\core\handlers\base.py", line 181, in _get_response
                        response = wrapped_callback(request, *callback_args, **callback_kwargs)
                    File "C:\Users\Bruce\Programming\class_HB2\code\Ronnie\user_management_w_forms\users\views.py", line 33, in register
                        login(request, user)
                    File "C:\Users\Bruce\.virtualenvs\user_management_w_forms-XHGniG9b\lib\site-packages\django\contrib\auth\__init__.py", line 129, in login
                        request.session[SESSION_KEY] = user._meta.pk.value_to_string(user)
                    File "C:\Users\Bruce\.virtualenvs\user_management_w_forms-XHGniG9b\lib\site-packages\django\utils\functional.py", line 249, in inner
                        return func(self._wrapped, *args)
                    AttributeError: 'AnonymousUser' object has no attribute '_meta'
                    [12/Sep/2022 10:03:23] "POST /accounts/register/ HTTP/1.1" 500 76821
                </details>
        * Note these lines from above output:
            <details>
            <summary>Sample output:</summary>

                ...
                authenticate(username=username, password=raw_password, email=email):  None
                User.objects.all() after authenticate():  <QuerySet [<User: admin>, <User: NotAnAdmin>]>
                user:  None
                User.objects.all() after form.save():  <QuerySet [<User: admin>, <User: NotAnAdmin>, <User: NotAnotherAdmin>]>
                the_form:  NotAnotherAdmin
                type(the_form):  <class 'django.contrib.auth.models.User'>
                ...
            </details>
        * Observations:
            * `authenticate(username=username, password=raw_password, email=email):  None`
                * `authenticate(username=username, password=raw_password, email=email)` is returning `None` since the new `User` (`NotAnotherAdmin`) has not been created yet.
            * `User.objects.all() after form.save():  <QuerySet [<User: admin>, <User: NotAnAdmin>, <User: NotAnotherAdmin>]>`
                * The `form.save()` is the part which actually creates a new `User` (`NotAnotherAdmin`).

1. Open Django Admin Interface and check status of new `User` (`NotAnotherAdmin`):
    * http://localhost:8000/admin/auth/user/
    * The specific URL for the new `User` (`NotAnotherAdmin`):
        * http://localhost:8000/admin/auth/user/7/change/
    * Username is set:
        * username: `NotAnotherAdmin`
    * Password is not set:
        <details>
        <summary>Sample browser display contents:</summary>

            No password set.
            Raw passwords are not stored, so there is no way to see this user’s password, but you can change the password using this form.
        </details>
    * INSERT_IMAGE_HERE
    * The new `User` (`NotAnotherAdmin`) is being created but there is no password being set by `form.save()`.
        * Maybe the form needs a field of `password` instead of the one of the two `password1` and `password2` fields since that is the field name used in [`django.contrib.auth.models.User`](https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#user-model).

1. Modify `fields` attribute of class `Meta` in `NewUserForm` of [`users/forms.py`](../users/forms.py) for testing:
    * Change `password1` to `password`.
        <details>
        <summary>Sample current <code></code> partial content:</summary>

            class Meta:
                ...
                fields = ('username', 'email', 'password', 'password2')
                ...
        </details>



## Summary:

* Notes:
    * `authenticate()` on line `20` returns `None` since `User` has not been created yet.
    * `form.save()` on line `21` is the code that is actually adding a user to the database.

* Suggestions:
    * Suggest adding the migrations to the example code so student doesn't have to remember to run the migrations in the proper order. It would be useful for the student to only have to run `migrate`. Since this is example code to provide sample code for the student to emulate, it can be useful for the student to be able to focus on understanding the view functions rether than the migrations themselves.
        * When code is run with following migration flow, the Django Admin Interface fails when deleting a `User`:
            1. `python .\manage.py migrate`
                * Error:
                    * `Exception Value:	no such table: users_profile`
        * When code is run with following migration flow, the Django Admin Interface works as expected when deleting a `User`:
            1. `python .\manage.py makemigrations users`
            1. `python .\manage.py migrate`
    * Suggest indenting `return render(request, 'registration/register.html', {'form': form})` one more tab (adding it to the `else` line `25` block) since `return redirect('index')` is handled by the `if` line `11` block.
        * The `if` (line `11`) block, or the `else` (line `25`) will be executed. So there is no need to have the `return render(request, 'registration/register.html', {'form': form})` logic follow the if/else (lines `11` through `26`) block. It would be more readable to have it included in the `else` (line `25`) block.
