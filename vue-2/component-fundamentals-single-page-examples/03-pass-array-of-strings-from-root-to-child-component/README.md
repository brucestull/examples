# Pass Array of Strings from Root to Child Component

* JavaScript:

    ```javascript
    const app1 = new Vue({
        ...
        data: {
            ...
            globalVariableAttribute: [
                'The first string in list',
                'The second string in list',
                'The third string in list',
            ],
            ...
        }
        ...
    })
    ```

  * `globalVariableAttribute`

* HTML:

    ```html
    <the-component-name
        v-bind:props-variable-in-component="globalVariableAttribute"
    ></the-component-name>
    ```

  * `props-variable-in-component` ==> `propsVariableInComponent`

* JavaScript:

    ```javascript
    Vue.component('the-component-name', {
        ...
        props: {
            propsVariableInComponent: Array,
        },
        ...
    })
    ```

    ```javascript
    Vue.component('the-component-name', {
        ...
        template: `
        <p>
            {{ propsVariableInComponent }}
        </p>
        `
        ...
    })
    ```
