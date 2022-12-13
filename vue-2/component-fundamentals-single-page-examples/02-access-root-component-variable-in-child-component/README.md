# Access Root Component Variable in Child Component

* JavaScript:

    ```javascript
    const app1 = new Vue({
        ...
        data: {
            ...
            globalVariableAttribute: 'Global Attribute String HERE!!!',
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
    props: {
        propsVariableInComponent: String,
    },
    ```

    ```javascript
    template: `
    <p>
    {{ propsVariableInComponent }}
    </p>
    `
    ```

* Image:  
![vue_component_basics](https://user-images.githubusercontent.com/47562501/202300640-b7fa4f91-dcd7-473b-b87a-a4360313d2ed.png)
