# Use an Array of Objects instead of an Array of Strings

* HTML in [`index.html`](./index.html):
    ```
    <main id='app1'>
        <ul>
            <li v-for="singleItem in anObjectArray">
                {{ singleItem }}
            </li>
        </ul>
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