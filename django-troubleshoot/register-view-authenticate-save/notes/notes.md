# User Management with Forms

## Resources:
* [`pillow` - pypi.org](https://pypi.org/project/Pillow/)
* [`pillow` - python-pillow.org](https://python-pillow.org/)
* [ModelForm - docs.djangoproject.com](https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/#modelform)
* [save() - docs.djangoproject.com](https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/#the-save-method)

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
