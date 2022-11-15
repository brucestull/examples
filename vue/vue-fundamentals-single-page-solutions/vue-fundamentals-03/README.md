# Use `v-for` to Display Individual Elements of an Array on the Page

* HTML in [`index.html`](./index.html):
    ```
    <main id='app1'>
        <p>{{ aSimpleArray }}</p>
    </main>
    ```

* JavaScript in [`index.html`](./index.html):
    ```
        const app1 = new Vue({
            ...
            data: {
                ...
                aSimpleArray: [
                    'First Thing',
                    'Second Thing',
                    'Third Thing',
                ]
                ...
            },
        })
    ```

* Image:


* [Vue Fundamentals](../README.md)