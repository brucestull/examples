# Fix Bug Where Item With Empty `description` Can be Added

## Resources:


* HTML in [`index.html`](./index.html):
    ```
    <main id='app1'>
        <h2>Add a New One</h2>
        <input
            v-model="inputElementText"
            v-on:keyup.enter="addObjectToAnObjectArray"
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
            ...
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
                    if (this.inputElementText !== '') {
                        console.log("Input NOT empty so we're gonna add!")
                        let newObject = {
                            id: this.nextObjectID,
                            description: this.inputElementText,
                        }
                        this.anObjectArray.push(newObject)
                        this.nextObjectID++
                        this.inputElementText = ''
                    } else {
                        console.log("Input IS empty so we're not gonna add!")
                    }
                }
            }
        })
    ```

* Image:


* [Vue Fundamentals](../README.md)