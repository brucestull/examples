// Start server:
// python -m http.server
// Resources:

const app1 = new Vue({
    el: '#app',
    data: {
        name: 'app1',
        storageVariable: '',
        isThisChecked: false,
        words: [
            'A Word',
            'Another Thing',
            'Yet Another Word',
        ]
    },
    methods: {
        sayHello: function (thing) {
            console.log("Welcome to: ", this.name)
            console.log("The Thing: ", thing)
        }
    },
    computed: {
        wordsWithWord: function () {
            return this.words.filter(function(word) {
                return word.includes('Word')
            })
        }
    }
})