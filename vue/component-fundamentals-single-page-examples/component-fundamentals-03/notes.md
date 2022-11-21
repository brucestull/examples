# Pass Array of Strings from Vue Object to Vue Component

* JavaScript:
    ```
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
    ```
    <the-component-name
        v-bind:props-variable-in-component="globalVariableAttribute"
    ></the-component-name>
    ```
    * `props-variable-in-component` ==> `propsVariableInComponent`

* JavaScript:
    ```
    Vue.component('the-component-name', {
        ...
        props: {
            propsVariableInComponent: Array,
        },
        ...
    })
    ```
    ```
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


