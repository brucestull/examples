# Add List View

* Modify `home` page so it displays a list of our `AwesomeCat` objects.

## Resources

* [`Model.objects`](https://docs.djangoproject.com/en/4.0/ref/models/class/#django.db.models.Model.objects)
* [`QuerySet` API reference](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#queryset-api-reference)
* Template [Variables](https://docs.djangoproject.com/en/4.0/ref/templates/language/#variables)

## Tag meanings for this guide

* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.

## Process

1. We will use the same URL configuration for named URL `home`.

1. Edit the view function `home` in [`the_app/views.py`](../the_app/views.py) to see if we can get the database values and print them to console:
    * Use our instance of [class Manager](https://docs.djangoproject.com/en/4.0/topics/db/managers/#django.db.models.Manager) `objects` to get a [`QuerySet`](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#queryset-api-reference) of our model [`AwesomeCat`](../the_app/models.py) objects.
        * Import the model `AwesomeCat` from `.models`.
        <details>
        <summary>Sample addition to <code>the_app/views.py</code> contents:</summary>

            def home(request):
                #...
                queryset_of_awesome_cats = AwesomeCat.objects.all()
                print(queryset_of_awesome_cats)
                #...
                return HttpResponse("Goodbuy, World! Enjoy the sail!")
        </details>

1. Start the development server:
    * `python .\manage.py runserver`

1. Open internet browser to application `home` URL:
    * <http://localhost:8000/the-app/home/>

1. Note output of console:
    <details>
    <summary>Sample console output:</summary>

        <QuerySet [
            <AwesomeCat: AwesomeCat object (1)>,
            <AwesomeCat: AwesomeCat object (2)>,
            <AwesomeCat: AwesomeCat object (3)>
        ]>
    </details>

1. We can get the `QuerySet` to display in console, let's see if we can get it to display on the `home` URL.

1. We can use a context dictionary to pass the data to be rendered on the template. Edit the current `home` view function in [`the_app/views.py`](../the_app/views.py) to pass a context dictionary to the `render` function:
    * Import `render` from `django.shortcuts`.
    * Create the context dictionary `context`:
        * key: `'view_to_template_object'`
        * value: `queryset_of_awesome_cats`
    * We will need to create a `home.html` template in a `templates` directory in the app directory `the_app`. We will do that next.
    <details>
    <summary>Sample <code>context</code> dictionary:</summary>

        context = {
            'view_to_template_object': queryset_of_awesome_cats
            }
    </details>
    <details>
    <summary>Sample <code>home</code> view function contents:</summary>

        def home(request):
            queryset_of_awesome_cats = AwesomeCat.objects.all()
            context = {
                'view_to_template_object': queryset_of_awesome_cats
                }
            return render(request, 'the_app/home.html', context)
    </details>

1. Add a directory `the_app/templates/` and create a template `home.html` in it:
    * Add a Django template tag for the [`variable`](https://docs.djangoproject.com/en/4.0/ref/templates/language/#variables):
        <details>
        <summary>Sample <code>the_app/templates/the_app/home.html</code> contents:</summary>

            {{ view_to_template_object }}
        </details>

1. Start the development server:
    * `python .\manage.py runserver`

1. Open internet browser to application `home` URL:
    * <http://localhost:8000/the-app/home/>
        <details>
        <summary>Sample browser display contents:</summary>

            <QuerySet [<AwesomeCat: AwesomeCat object (1)>, <AwesomeCat: AwesomeCat object (2)>, <AwesomeCat: AwesomeCat object (3)>]>
        </details>

1. We can now display the `QuerySet` object on the `home` URL. Let's see how to display the individual `QuerySet` elements on the `home` URL using Django template tag [`for`](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#for).
    * Each `QuerySet` element will be an `AwesomeCat` object.

1. Create a a Django template `for` loop in [`the_app/home.html`](../the_app/templates/the_app/home.html):
    <details>
    <summary>Sample <code>for</code> loop contents in <code>the_app/home.html</code>:</summary>

        {% for cat in view_to_template_object %}
        {{ cat }}
        {% endfor %}
    </details>

1. We now can see each `AwesomeCat` object on the `home` URL. Let's see how to get the actual `name` attribute of each [`AwesomeCat`](../the_app/models.py) object.

1. Append a `.` followed by the attribute `name` to the `AwesomeCat` object variable `cat` in [`the_app/home.html`](../the_app/templates/the_app/home.html):
    <details>
    <summary>Sample <code>for</code> loop contents in <code>the_app/home.html</code>:</summary>

        {% for cat in view_to_template_object %}
        {{ cat.name }}
        {% endfor %}
    </details>

1. Start the development server:
    * `python .\manage.py runserver`

1. Open internet browser to application `home` URL:
    * <http://localhost:8000/the-app/home/>
        <details>
        <summary>Sample browser display contents:</summary>

            Dezzi Bunbun Greta
        </details>
    * These are the three sample `AwesomeCat` entries in the database.

1. We now have a List View on display. The user can now add styling to their preferences.

## Navigation links

* Back to [Add Model Functionality](./03_add_model_functionality.md)
