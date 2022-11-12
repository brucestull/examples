// Start server:
// python -m http.server 8000



Vue.component('the-component-name', {
    props: {
        propVariableInComponent: Object,
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
        globalVariableAttribute: [
            { id: 1, description: 'The First Thing in the List!' },
            { id: 2, description: 'The SECOND Thing in the List?'},
        ],
    },
    methods: {

    },
    computed: {

    },

})