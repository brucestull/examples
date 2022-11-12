// Start server:
// python -m http.server 8000



Vue.component('the-component-name', {
    props: {
        propVariableInComponent: String,
    },
    template: `
    <p>
    {{ propVariableInComponent }}
    </p>
    `
})

const app1 = new Vue({
    el: '#app1',
    data: {
        appName: 'Application Number 1!',
        globalVariableAttribute: 'Some global string?'
    },
    methods: {

    },
    computed: {

    },

})