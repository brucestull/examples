# Notes

## Resources:
* [Composing with Components - v2.vuejs.org](https://v2.vuejs.org/v2/guide/#Composing-with-Components)

* Images:
    * Element identifiers - Vue Dev Tools in Chrome:
    ![Element identifiers - Vue Dev Tools in Chrome](https://user-images.githubusercontent.com/47562501/201470122-c0dfe8d1-be04-411f-81c2-d189f8af9e51.png)


## HTML:
```
    <main id='app1'>

        <the-lone-element></the-lone-element>

    </main>
```

## JavaScript:
* Notes:
    * The 'p' element is included since a template requires some HTML element inside it.
```
Vue.component('the-lone-element', {
    template: `
    <p>
    BIG STRING in Vue.component('the-lone-element', {template})!!!
    </p>
    `
})

const app1 = new Vue({
    el: '#app1'
    })
```
