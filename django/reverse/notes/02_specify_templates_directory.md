# 02 - Specify Templates Directory

## Resources:
* [`settings`](https://docs.djangoproject.com/en/4.1/ref/settings/#settings)
* [`TEMPLATES`](https://docs.djangoproject.com/en/4.1/ref/settings/#templates)

## Code Examples Repository links:
* [Code Examples Repository](../../../README.md)
* [Django Code Examples](../../README.md)

## Tag meanings for this guide:
* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.

## Process:

1. **ACTION:** Modify the [`TEMPLATES`](https://docs.djangoproject.com/en/4.1/ref/settings/#templates) attribute of [`the_project/settings.py`](../the_project/settings.py) so that we can place a [`templates`](../templates/) directory in the root of the project:
    * Add import of `os`
        * `import os`
    * Add the following dictionary entry to the `TEMPLATES` attribute:
        * `'DIRS': [os.path.join(BASE_DIR, 'templates')]`
    <details>
    <summary>Sample <code>the_project/settings.py</code> attribute change:</summary>

        #...
        import os
        #...

        #...
        TEMPLATES = [
            {
                #...
                'DIRS': [os.path.join(BASE_DIR, 'templates')],
                #...
            },
        ]
        #...

    </details>

1. **INFO:** We can now create our templates in the `templates` directory, which is located in the root of the poject instead of individual application directories.

1. Proceed to [03 - Add an Index View](./03_add_an_index_view.md)

## Repository Links:
* Back to [01 - Create a New `pipenv` Virtual Environment for the Project](./01_create_virtual_environment.md)