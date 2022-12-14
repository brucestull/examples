# `models.Model` : `related_name` - **UNDER CONSTRUCTION**

## Resources

* [The Django admin documentation generator - docs.djangoproject.com](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/admindocs/)
* [Django Best Practices: Custom User Model - learndjango.com](https://learndjango.com/tutorials/django-custom-user-model)
* [Django Password Reset Tutorial - learndjango.com](https://learndjango.com/tutorials/django-password-reset-tutorial)
* [Django Signup Tutorial - learndjango.com](https://learndjango.com/tutorials/django-signup-tutorial)
* [Django Login and Logout Tutorial - learndjango.com](https://learndjango.com/tutorials/django-login-and-logout-tutorial)

## Lessons Learned

* `related_name`:
  * [`api/serializers.py`](./api/serializers.py):

    ```python
    class CurrentUserSerializer(serializers.ModelSerializer):
        #...
        things_detail = NestedThingSerializer(
            #...
            source='things',
            #...
        )
        #...
    ```

  * [`things/models.py`](./things/models.py):

    ```python
    class Thing(models.Model):
        #...
        owner = models.ForeignKey(
            #...
            related_name='things',
            #...
        )
        #...
    ```

## URL Routes

## TODO

## Notes

## Directory Structure

## Links

* [Commands and Links](./notes/00_commands_and_links.md)
