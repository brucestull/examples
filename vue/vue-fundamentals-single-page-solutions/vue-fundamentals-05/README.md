# Use JavaScript Keys to Access Values in `anObjectArray` on Page

## Resources:

* [Maintaining State - v2.vuejs.org](https://v2.vuejs.org/v2/guide/list.html#Maintaining-State)

* HTML in [`index.html`](./index.html):
    ```
    <main id='app1'>
            <li
                v-for="singleItem in anObjectArray"
                v-bind:key="singleItem.id"
                >
                {{ singleItem.id }} - {{ singleItem.description }}
            </li>
    </main>
    ```

* JavaScript in [`index.html`](./index.html):
    ```
        const app1 = new Vue({
            ...
            data: {
                ...
                anObjectArray: [
                    { id: 1, description: 'First Thing' },
                    { id: 2, description: 'Second Thing'},
                    { id: 3, description: 'Third Thing' },
                    ],
                ...
            },
            ...
        })
    ```

* Image:


* [Vue Fundamentals](../README.md)