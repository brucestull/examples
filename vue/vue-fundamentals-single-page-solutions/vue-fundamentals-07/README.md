# Add Input Element for Adding New Item

## Resources:


* HTML in [`index.html`](./index.html):
    ```
    <main id='app1'>
        <h2>Add a New One</h2>
        <input
            v-model="inputElementText"
            v-on:keyup.enter="addObjectToAnObjectArray"
            placeholder="Your new thing here..."
            >
        <button
            v-on:click="addObjectToAnObjectArray"
            >
            &plus;
        </button>
    </main>
    ```

* JavaScript in [`index.html`](./index.html):
    ```
    const app1 = new Vue({
        data: {
            anObjectArray: [
                ...
                ],
            nextObjectID: 4,
            inputElementText: '',
        },
        methods: {
            addObjectToAnObjectArray: function() {
                console.log("We're trying to add an object to array!")
                let newObject = {
                    id: this.nextObjectID,
                    description: this.inputElementText,
                }
                this.anObjectArray.push(newObject)
                this.nextObjectID++
                this.inputElementText = ''
            }
        }
    })
    ```

* Image:


* [Vue Fundamentals](../README.md)