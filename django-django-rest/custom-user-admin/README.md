# Django User Admin Example - **UNDER CONSTRUCTION**

## Resources

* [The Django admin documentation generator - docs.djangoproject.com](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/admindocs/)
* [Django Best Practices: Custom User Model - learndjango.com](https://learndjango.com/tutorials/django-custom-user-model)
* [Django Password Reset Tutorial - learndjango.com](https://learndjango.com/tutorials/django-password-reset-tutorial)
* [Django Signup Tutorial - learndjango.com](https://learndjango.com/tutorials/django-signup-tutorial)
* [Django Login and Logout Tutorial - learndjango.com](https://learndjango.com/tutorials/django-login-and-logout-tutorial)

## Lessons Learned

### URL Routes

* `config/urls.py`:
  * `path('', TemplateView.as_view(template_name='home.html'), name='home')`:

    ```console
    / [name='home']
    ```

  * `path('accounts/', include('django.contrib.auth.urls'))`:

    ```console
    accounts/login/ [name='login']
    accounts/logout/ [name='logout']
    accounts/password_change/ [name='password_change']
    accounts/password_change/done/ [name='password_change_done']
    accounts/password_reset/ [name='password_reset']
    accounts/password_reset/done/ [name='password_reset_done']
    accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    accounts/reset/done/ [name='password_reset_complete']
    ```

* `accounts/urls.py`:
  * `path('signup/', SignUpView.as_view(), name='signup')`:

    ```console
    accounts/signup/ [name='signup']
    ```

## TODO

## Notes

## Directory Structure

## Links

* [Commands and Links](./notes/00_commands_and_links.md)
