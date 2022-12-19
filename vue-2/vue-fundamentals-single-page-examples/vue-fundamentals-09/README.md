# Add `status` Button to Toggle the Item's `status` property

## Resources:


* HTML in [`index.html`](./index.html):
    ```
    <main id='app1'>
        <li
            v-for="singleItem in anObjectArray"
            v-bind:key="singleItem.id"
            >
            <button
                v-if="!singleItem.status"
                v-on:click="toggleItem(singleItem)"
                >
                C &check;
            </button>
            <button
                v-if="singleItem.status"
                v-on:click="toggleItem(singleItem)"
                >
                I &cularr;
            </button>
            {{ singleItem.id }} - {{ singleItem.description }} - {{ singleItem.status }}
        </li>
    </main>
    ```

* JavaScript in [`index.html`](./index.html):
    ```
        const app1 = new Vue({
            data: {
                ...
                anObjectArray: [
                    { id: 1, description: 'First Thing',  status: true  },
                    { id: 2, description: 'Second Thing', status: false },
                    { id: 3, description: 'Third Thing',  status: false },
                    { id: 4, description: 'Fourth Thing', status: true  },
                    ],
                ...
            },
            methods: {
                ...
                toggleItem: function(payload) {
                    console.log("Toggling: ", payload.id, payload.description, "from", payload.status)
                    payload.status = !payload.status
                },
                ...
            }
        })
    ```

* Image:


* [Vue Fundamentals](../README.md)