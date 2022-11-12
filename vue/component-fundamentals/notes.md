# Notes

## Resources:
* [Composing with Components - v2.vuejs.org](https://v2.vuejs.org/v2/guide/#Composing-with-Components)
* [Style Guide - v2.vuejs.org](https://v2.vuejs.org/v2/style-guide/)

## Process:

1. Create simple Vue component:
    1. Add a simple Vue component to [`main.js`](./main.js):
        ```
        Vue.component('the-component-name', {
            template: `
            <p>
            A paragraph string goeth here!
            </p>
            `
        })
        ```
    1. Create an HTML element with the Vue component's name 'the-component-name' in [`index.html`](./index.html):
        ```
        <the-component-name></the-component-name>
        ```
    1. Start http server if not already running:
        * `python -m http.server 8000`
    1. Test Vue application:
        * http://localhost:8000/
    1. Summary:
        * `the-component-name`
        * The component currently only passes a hard-coded HTML element. We will add 'props' to pass values from Vue model.

1. Add `props` to the component:
    1. Add a `props` property to the component in [`main.js`](./main.js):
        ```
        Vue.component('the-component-name', {
            ...
            props: {
                propVariableInComponent: String,
            },
            ...
            `
        })
        ```
    1. Add a reference to `propVariableInComponent` to `template` property of Vue component in [`main.js`](./main.js):
        ```
        Vue.component('the-component-name', {
            ...
            template: `
            <p>
            {{ propVariableInComponent }}
            </p>
            `
            ...
        })
        ```

    1. Add a global property variable `globalVariableAttribute` to main Vue object in [`main.js`](./main.js):
        ```
        const app1 = new Vue({
            ...
            data: {
                ...
                globalVariableAttribute: 'Some global string?'
                ...
            },
            ...
        })
        ```
    1. Map the `globalVariableAttribute` to the `propVariableInComponent` in [`index.html`](./index.html):
        * Note: This is a weird one. Need to translate between camelCase and kebab-case for this to work.
        * Mapping of prop variable:
            * In [`main.js`](./main.js):
                * `propVariableInComponent`
            * In [`index.html`](./index.html):
                * `prop-variable-in-component`
        * Mapping of global model property in [`index.html`](./index.html):
            * `globalVariableAttribute`
        ```
        <the-component-name
            v-bind:prop-variable-in-component="globalVariableAttribute"
        ></the-component-name>
        ```
    1. Start http server if not already running:
        * `python -m http.server 8000`
    1. Test Vue application:
        * http://localhost:8000/
    1. Summary: 
        * We now pass a global Vue model property to the component.

1. Display the items in list `globalVariableAttribute` into parts in [`index.html`](./index.html):
    1. Add a list property to `data` part of Vue model in [`main.js`](./main.js):
        ```
        const app1 = new Vue({
            ...
            data: {
                ...
        globalVariableAttribute: [
            'The First Thing in the List!',
            'The SECOND Thing in the List?',
        ],
                ...
            }
            ...
        })
        ```
    1. Modify the element in the HTML [`index.html`](./index.html):
        ```
        <the-component-name
            v-for="theItem in globalVariableAttribute"
            v-bind:prop-variable-in-component="theItem"
            v-bind:key="theItem.id"
        ></the-component-name>
        ```
        * Iterate over the items in `globalVariableAttribute` and pass each one into an instance of component `the-component-name`.
    1. Start http server if not already running:
        * `python -m http.server 8000`
    1. Test Vue application:
        * http://localhost:8000/
    1. Summary:
        * The items in list `globalVariableAttribute` should display on webpage.
        * There should be one component for each item in list `globalVariableAttribute`.

1. Modify `globalVariableAttribute` so it is a list of objects instead of of a list of strings.
    1. Modify `globalVariableAttribute` in [`main.js`](./main.js):
        ```
        const app1 = new Vue({
            ...
            data: {
                ...
                globalVariableAttribute: [
                    { id: 1, description: 'The First Thing in the List!' },
                    { id: 2, description: 'The SECOND Thing in the List?'},
                ],
                ...
            },
            ...
        })
        ```
    1. Change the prop variable type from `String` to `Object`:
        ```
        Vue.component('the-component-name', {
            ...
            props: {
                propVariableInComponent: Array,
            },
            ...
        })
        ```
    1. Start http server if not already running:
        * `python -m http.server 8000`
    1. Test Vue application:
        * http://localhost:8000/
    1. Summary:
        * We now are passing an object into each instance of the component `the-component-name`.
        * We will not display each property of the object in each instance of the component.




