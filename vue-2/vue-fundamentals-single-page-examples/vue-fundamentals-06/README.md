# Include Function to Add Hard-coded Object to the Array Object `anObjectArray`

## Resources:

* [Maintaining State - v2.vuejs.org](https://v2.vuejs.org/v2/guide/list.html#Maintaining-State)

* HTML in [`index.html`](./index.html):
    ```

    ```

* JavaScript in [`index.html`](./index.html):
    ```
    const app1 = new Vue({
        data: {
            ...
            anObjectArray: [
                ...
                ],
            nextObjectID: 4,
        },
        methods: {
            addObjectToAnObjectArray: function() {
                console.log("We're trying to add an object to array!")
                let newObject = {
                    id: this.nextObjectID,
                    description: 'Fourth Thing',
                }
                this.nextObjectID++
                this.anObjectArray.push(newObject)
            }
        },
    })
    ```

* Image:


* [Vue Fundamentals](../README.md)