# Notes

## Resources:
* [`TemplateView` - docs.djangoproject.com](https://docs.djangoproject.com/en/4.1/ref/class-based-views/base/#django.views.generic.base.TemplateView)
* [The Django admin documentation generator - docs.djangoproject.com](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/admindocs/#module-django.contrib.admindocs)
* [`@login_required`](https://docs.djangoproject.com/en/4.1/topics/auth/default/#the-login-required-decorator)
    * `from django.contrib.auth.decorators import login_required`
    * `@login_required`
* [HTML \<input> Tag - www.w3schools.com](https://www.w3schools.com/tags/tag_input.asp)
* [HTML \<label> Tag - www.w3schools.com](https://www.w3schools.com/tags/tag_label.asp)
* [HTML \<select> Tag - www.w3schools.com](https://www.w3schools.com/tags/tag_select.asp)
* [`datetime.now()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.now)

* `TemplateView`
    ```
    from django.views.generic.base import TemplateView
        #...
        path('', TemplateView.as_view(template_name="home.html"), name='home'),
        #...
    ```