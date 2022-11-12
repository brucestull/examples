// Start server:
// python -m http.server 8000

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