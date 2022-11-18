// Start server:
// python -m http.server 8000
// Resources:

const app1 = new Vue({
    el: '#app1',
    data: {
        name: 'app1',
    },
    methods: {

    },
    computed: {

    },
    beforeMount: function() {
        console.log("About to mount!")
    },
    mounted: function() {
        console.log("Mounted")
    },
    destroyed: function() {
        console.log("Destroyed")
    },
    created: function() {
        console.log("Created")
    },
})