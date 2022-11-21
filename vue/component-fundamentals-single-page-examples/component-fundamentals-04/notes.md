# Pass an Array of Objects from Vue Object to Vue Component

* JavaScript:
    ```
    const app1 = new Vue({
        ...
        data: {
            ...
            globalVariableAttribute: [
                { id: 1, description: 'The first string in list'    },
                { id: 2, description: 'The second string in list'   },
                { id: 3, description: 'The third string in list'    },
            ],
            ...
        }
        ...
    })
    ```
    * `globalVariableAttribute`

* HTML:
    * `theItem` is the local iterating variable within the Vue loop `v-for`, which iterates over `globalVariableAttribute`.
    * Each iteration of `theItem` is passed into the component as `props-variable-in-component`.
    ```
    <the-component-name
        v-for="theItem in globalVariableAttribute"
        v-bind:props-variable-in-component="theItem"
        v-bind:key="theItem.id"
    ></the-component-name>
    ```
    * `props-variable-in-component` [in HTML] ==> `propsVariableInComponent` [in JavaScript]
* JavaScript:
    ```
    Vue.component('the-component-name', {
        ...
        props: {
            propsVariableInComponent: Object,
        },
        ...
    ```
    ```
    Vue.component('the-component-name', {
        ...
        template: `
        <p>
            {{ propsVariableInComponent.id }} : {{ propsVariableInComponent.description }}
        </p>
        `
        ...
    })
    ```