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


