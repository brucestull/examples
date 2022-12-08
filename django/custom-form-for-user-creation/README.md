# Custom Form for User Creation - **UNDER CONSTRUCTION**

## Resources

* [Django Best Practices: Custom User Model - learndjango.com](https://learndjango.com/tutorials/django-custom-user-model)
* [Django Signup Tutorial - learndjango.com](https://learndjango.com/tutorials/django-signup-tutorial)
* [Django Login and Logout Tutorial - learndjango.com](https://learndjango.com/tutorials/django-login-and-logout-tutorial)

## Notes

* `forms.py`

    ```python
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth.models import User


    class UserCreationFormWithEmail(UserCreationForm):
        class Meta:
            model = User
            fields = [
                'username',
                'email'
            ]
    ```

* `views.py`

    ```python
    from django.urls import reverse_lazy
    from django.views import generic

    from .forms import UserCreationFormWithEmail


    class SignUpView(generic.CreateView):

        form_class = UserCreationFormWithEmail
        success_url = reverse_lazy("login")
        template_name = "registration/signup.html"
    ```
