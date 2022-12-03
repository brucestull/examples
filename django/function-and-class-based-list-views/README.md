# Function and Class-Based List Views

* Example of Five (5) Different Types of Django Views

* Includes the following view types:
  * Function-based view:
    * Return a simple `HttpResponse` with text string.
  * Function-based view:
    * Return a `render()` function.
  * Class-based view which inherits from `View`:
    * Define a `get()` method which retrieves the needed objects from the database and renders them.
  * Class-based view which inherits from `TemplateView`:
    * Define a `get_context_data()` method which we add our own context `key`s and `value`s to it.
  * Class-based view which inherits from `ListView`.
    * We define the following:
      * The `model`s class which we want rendered.
      * Our `context_object_name` if we use a non-standard one.
      * Our `template_name` if we use a non-standard one.

## Notes

* [Notes - Django Function and Class-Based List Views](./notes/notes.md)

## Code Examples Repository links

* [Code Examples Repository](../../README.md)
* [Django Code Examples](../README.md)
