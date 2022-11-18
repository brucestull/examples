// Start server:
// python -m http.server 8000
// Resources:

const app1 = new Vue({
    el: '#app1',
    data: {
        name: 'Vue Application - Single List Toggle',
        listOfThings: [
            {id: 1, descriptor: "First Thing", status: true},
            {id: 2, descriptor: "Second Thing", status: true},
            {id: 3, descriptor: "Third Thing", status: false},
            {id: 4, descriptor: "Fourth Thing", status: true},
        ]
    },
    methods: {
        toggleTheObject: function(localVariableInFunction) {
            console.log("Patience, please. We're toggling: ", localVariableInFunction.descriptor)
            localVariableInFunction.status =!localVariableInFunction.status
        }
    },
    computed: {

    },

})