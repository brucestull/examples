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
    beforeCreate: function() {
        console.log("About to Create!")
    },
    created: function() {
        console.log("Created")
    },
    beforeMount: function() {
        console.log("About to Mount!")
    },
    mounted: function() {
        console.log("Mounted")
    },
    beforeUpdate: function() {
        console.log("About to Update!")
    },
    updated: function() {
        console.log("Updated")
    },
    beforeDestroy: function() {
        console.log("About to Destroy!")
    },
    destroyed: function() {
        console.log("Destroyed")
    },
})