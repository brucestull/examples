# Notes

## Resources:
* [Composing with Components - v2.vuejs.org](https://v2.vuejs.org/v2/guide/#Composing-with-Components)
* [Style Guide - v2.vuejs.org](https://v2.vuejs.org/v2/style-guide/)

## HTML:
```
    <component-element-name
        v-bind:theloneprop="globalVariableAttribute"
    ></component-element-name>
```

## JavaScript:
```
Vue.component('component-element-name', {
    props: {
        theloneprop: String,
    },
    template: `
    <s>
    {{ theloneprop }}!!!
    </s>
    `
})

const app1 = new Vue({
    el: '#app1',
    data: {
        globalVariableAttribute: 'Global Attribute String HERE!!!',
    }
})
```