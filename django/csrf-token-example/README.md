# CSRF Token Example - **UNDER CONSTRUCTION**

* Simple Django app to demonstrate use of a CSRF token for a given session ID.

## Resources

* [Django CSRF Protection](https://docs.djangoproject.com/en/4.1/ref/csrf/)
* [`django` - pypi.org](https://pypi.org/project/Django/)
* [`djangorestframework` - pypi.org](https://pypi.org/project/djangorestframework/)
* [`docutils` - pypi.org](https://pypi.org/project/docutils/)
* [The Django admin documentation generator](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/admindocs/)
* [Django Login and Logout Tutorial - learndjango.com](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
* [Django Signup Tutorial - learndjango.com](https://learndjango.com/tutorials/django-signup-tutorial)

## Lessons Learned

* It seems that the CSRF token is only required on POST requests for the current code base. Need to try other permissions settings to see if this continues to be true.

* Request URL `/api/v1/things/`:
  * `IsAuthenticated`:
    | Logged In | CSRF Token | Method | Result |
    | --- | --- | --- | --- |
    | No | No | REQUEST_METHOD | RESPONSE_STATUS |
    | No | No | REQUEST_METHOD | RESPONSE_STATUS |
    | No | Yes | REQUEST_METHOD | RESPONSE_STATUS |
    | No | Yes | REQUEST_METHOD | RESPONSE_STATUS |
    | Yes | No | REQUEST_METHOD | RESPONSE_STATUS |
    | Yes | No | REQUEST_METHOD | RESPONSE_STATUS |
    | Yes | Yes | REQUEST_METHOD | RESPONSE_STATUS |
    | Yes | Yes | REQUEST_METHOD | RESPONSE_STATUS |

* API URL routes:

    ```python
    #...
    router.register('thingsss', views.ThingViewSet, basename='things')
    #...
    ```

    ![image](https://user-images.githubusercontent.com/47562501/205686663-102cc2c5-07d3-4a80-8e25-13002f10829f.png)

## TODO

## Notes

## Directory Structure
