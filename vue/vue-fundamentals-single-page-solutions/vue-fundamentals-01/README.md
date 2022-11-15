# Display a String on the Page

* HTML in [`index.html`](./index.html):
    ```
    <main id='app1'>
        <h1>{{ applicationName }}</h1>
    </main>
    ```

* JavaScript in [`index.html`](./index.html):
    ```
    const app1 = new Vue({
        el: '#app1',
        data: {
            applicationName: "Flynnt Knapp's Awesome Vue Fundamentals App???",
        },
    })
    ```

* Image: