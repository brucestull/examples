# Notes

## Resources:
* [`TemplateView` - docs.djangoproject.com](https://docs.djangoproject.com/en/4.1/ref/class-based-views/base/#django.views.generic.base.TemplateView)
* [HTML \<input> Tag - www.w3schools.com](https://www.w3schools.com/tags/tag_input.asp)
* [HTML \<label> Tag - www.w3schools.com](https://www.w3schools.com/tags/tag_label.asp)

* `TemplateView`
    ```
    from django.views.generic.base import TemplateView
        #...
        path('', TemplateView.as_view(template_name="home.html"), name='home'),
        #...
    ```