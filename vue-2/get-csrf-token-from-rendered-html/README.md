# Get CSRF token from rendered HTML

* **NOTE**: This Vue app needs a Django backend to provide the CSRF token.

* This is a simple example of how to get the CSRF token from a rendered HTML page.
* This is useful when you want to use the CSRF token in a Vue.js application.
* This example needs to have a Django application to add the CSRF token to the HTML page.
  * The CSRF token is added to the rendered HTML template in the csrf token template tag:

    ```html
    <form action="" method="post">
      {% csrf_token %}
      <input type="text" name="text-the-user-provided"/>
      <input type="submit" value="Submit the form, NOW!"/>
    </form>
    ```
