# `related_name` - **UNDER CONSTRUCTION**

## Resources

* [`CASCADE`](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.CASCADE)
* [`django.views.generic.list.ListView`](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#django.views.generic.list.ListView)
* [How to manage static files (e.g. images, JavaScript, CSS)](https://docs.djangoproject.com/en/4.1/howto/static-files/#how-to-manage-static-files-e-g-images-javascript-css)

## Lessons Learned

* File load order is determined by the order of HTTP requests:

  ```console
  [11/Dec/2022 03:10:13] "GET /things/ HTTP/1.1" 200 1250
  [11/Dec/2022 03:10:13] "GET /static/images/auth_user_theme_light.png HTTP/1.1" 200 15208
  [11/Dec/2022 03:10:13] "GET /static/images/auth_user_theme_dark.png HTTP/1.1" 200 14895
  [11/Dec/2022 03:10:13] "GET /static/images/things_thing_theme_dark.png HTTP/1.1" 200 5329
  [11/Dec/2022 03:10:13] "GET /static/images/things_thing_theme_light.png HTTP/1.1" 200 5104
  ```

## TODO

## Notes

## Directory Structure

## Tags

* cascade
* django
* related_name
* static
* staticfiles
* STATICFILES_DIRS
* ListView
