# `related_name` - **UNDER CONSTRUCTION**

## Related Code Snippets

* [`things/models.py`](./things/models.py):

  ```python
  class Thing(models.Model):
      #...
      owner = models.ForeignKey(
          #...
          related_name='owner_related_name_for_things',
          #...
      )
          #...
  ```

* [`api/serializers.py`](./api/serializers.py):

  ```python
  class UserSerializerWithThings(serializers.ModelSerializer):
      things = NestedThingSerializer(
          #...
          source='owner_related_name_for_things',
          #...
      )
        
          class Meta:
              #...
              fields = (
                  #...
                  'things',
                  #...
              )
  ```

* [`templates/home.html`](./templates/home.html):

  ```html
  <!--  -->
  <p>{{ user.owner_related_name_for_things.all }}</p>
  <!--  -->
  ```

## Related Django Admin Images

* Model: `auth.User`:
  * ![auth_user_theme_dark](https://user-images.githubusercontent.com/47562501/206894866-f7827cd7-7482-4cc3-a37d-1aeaba667dba.png)
  * ![auth_user_theme_dark](./static/images/auth_user_theme_dark.png)
  * ![auth_user_theme_light](https://user-images.githubusercontent.com/47562501/206894867-b709ca4c-226b-40f4-8b7c-694c451fe617.png)
  * ![auth_user_theme_light](./static/images/auth_user_theme_light.png)
* Model: `things.Thing`:
  * ![things_thing_theme_dark](https://user-images.githubusercontent.com/47562501/206894868-fcdad77f-fa94-425c-8fd9-2271511762a3.png)
  * ![things_thing_theme_dark](./static/images/things_thing_theme_dark.png)
  * ![things_thing_theme_light](https://user-images.githubusercontent.com/47562501/206894869-86354760-ed93-4361-b120-22fc0a323124.png)
  * ![things_thing_theme_light](./static/images/things_thing_theme_light.png)

## Resources

* [`CASCADE` - docs.djangoproject.com](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.CASCADE)
* [`django.views.generic.list.ListView` - docs.djangoproject.com](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#django.views.generic.list.ListView)
* [How to manage static files (e.g. images, JavaScript, CSS) - docs.djangoproject.com](https://docs.djangoproject.com/en/4.1/howto/static-files/#how-to-manage-static-files-e-g-images-javascript-css)

## Lessons Learned

* File load order is related to order of HTTP requests:

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
