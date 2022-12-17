# Code Samples

* [`api/views.py`](./api/views.py):

  ```python
  class ThingDescriptionSearchView(generics.ListAPIView):
      """
      ListAPIView for a list of things, filtered by description.
      """
      queryset = models.Thing.objects.all()
      serializer_class = serializers.ThingSerializer
      search_fields = ['description']
      filter_backends = [
          filters.SearchFilter
      ]
  ```

* [`api/urls.py`](../api/urls.py):

  ```python
  urlpatterns = [
      #...
      path('things/description/', views.ThingDescriptionSearchView.as_view()),
      #...
  ] + router.urls
  ```

* Sample search URLs:
  * [](../templates/home.html)

    ```html
    <a
        href="/api/v1/things/description/?search=My"
        >
    </a>
    <a
        href="/api/v1/things/description/?search=my"
        >
    </a>
    <a
        href="/api/v1/things/description/?search=the"
        >
    </a>
    <a
        href="/api/v1/things/description/?search=purr"
        >
    </a>
    <a
        href="/api/v1/things/name/?search=itt"
        >
    </a>
    ```
