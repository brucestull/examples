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