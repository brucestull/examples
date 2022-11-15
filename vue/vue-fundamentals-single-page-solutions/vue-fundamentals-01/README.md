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
![image_01](https://user-images.githubusercontent.com/47562501/201955814-f26401b0-4d84-4410-9c58-27a71ae3aa1b.png)

* [Vue Fundamentals](../README.md)