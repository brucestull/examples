// Start server:
// python -m http.server 8000
// Resources:

const app1 = new Vue({
    el: '#app1',
    data: {
        name: 'app1',
        names: [
            "Earl",
        ],
        inputName: '',
        helloWho: '',
        isThisChecked: false,
        words: [
            'A Word',
            'Yet Another Word',
            'That which we do not say',
        ]
    },
    methods: {
        sayHello: function (who) {
            console.log("Welcome to: ", this.name)
            console.log("You: ", who)
        },
        
        addPerson: function () {
            this.names.push(this.inputName)
            this.inputName = ''
            this.isThisChecked = !this.isThisChecked
        }
    },
    computed: {
        wordsWithWord: function () {
            return this.words.filter(function(word) {
                return word.includes('Word')
            })
        }
    },
    updated: function () {
        // console.log("Did you just hear that?")
    },
})