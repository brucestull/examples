# Pass an Array of Objects from Root to Child Component

* [Vue 2 Component Fundamentals : Single-Page Examples](../README.md)

* JavaScript:

    ```javascript
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

    ```html
    <the-component-name
        v-for="theItem in globalVariableAttribute"
        v-bind:props-variable-in-component="theItem"
        v-bind:key="theItem.id"
    ></the-component-name>
    ```

  * `props-variable-in-component` [in HTML] ==> `propsVariableInComponent` [in JavaScript]
* JavaScript:

    ```javascript
    Vue.component('the-component-name', {
        ...
        props: {
            propsVariableInComponent: Object,
        },
        ...
    ```

    ```javascript
    Vue.component('the-component-name', {
        ...
        template: `
        <div>
            {{ propsVariableInComponent }}
            <br>
            {{ propsVariableInComponent.id }} : {{ propsVariableInComponent.description }}
            <br>
            <br>
        </div>
        `
        ...
    })
    ```
