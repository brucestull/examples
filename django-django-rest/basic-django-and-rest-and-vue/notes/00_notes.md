# Notes

## Information

* Django Authentication Routes and Views

    ```python
    accounts/login/ [name='login']
    accounts/logout/ [name='logout']
    accounts/password_change/ [name='password_change']
    accounts/password_change/done/ [name='password_change_done']
    accounts/password_reset/ [name='password_reset']
    accounts/password_reset/done/ [name='password_reset_done']
    accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    accounts/reset/done/ [name='password_reset_complete']
    ```

## Resources

* [Django Best Practices: Custom User Model - learndjango.com](https://learndjango.com/tutorials/django-custom-user-model)
* [Django Signup Tutorial - learndjango.com](https://learndjango.com/tutorials/django-signup-tutorial)
* [Django Login and Logout Tutorial - learndjango.com](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
