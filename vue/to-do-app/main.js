// Start server:
// python -m http.server 8000
// python -m http.server 8010
// Resources:
// https://v2.vuejs.org/
// https://vuejs.org/guide/introduction.html
// https://v2.vuejs.org/v2/guide/instance.html#Lifecycle-Diagram
// https://vuejs.org/guide/essentials/event-handling.html#key-modifiers

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator


const app1 = new Vue({
    el: '#app1',
    data: {
        appName: "Flynnt Knapp's Awesome Task App",
        taskText: 'Totally Awesome Task',

        nextID: 6,

        modelTask: {
            id: '',
            description: '',
            isCompleted: false,
        },

        tasks: [
            { id:  1, description: 'Scrub the Kitten',  isCompleted: false  },
            { id:  2, description: 'Grip the Vice',     isCompleted: true   },
            { id:  3, description: 'Order the Chaos!',  isCompleted: true   },
            { id:  4, description: 'Butter the Cat!',   isCompleted: false  },
            { id:  5, description: 'Flip the Bird',     isCompleted: false  },
        ]
    },

    methods: {
        addTask: function () {
            console.log("We're adding a task: ", this.taskText)
            // let currentTasksLength = this.tasks.length
            let aTask = {
                id: this.nextID,
                // id: currentTasksLength + 1,
                description: this.taskText,
                isCompleted: false,
            }
            this.tasks.push(aTask)
            this.taskText = ''
            this.nextID++
        },
        toggleTask: function (task) {
            console.log(
                "We're Toggling to",
                (task.isCompleted ? "Incomplete:" : "Complete:"),
                task.id,
                task.description
            )
            task.isCompleted = !task.isCompleted
        },
        removeTask: function (task) {
            console.log(
                "We're Removing: ",
                task.id,
                task.description
            )
            this.tasks.splice(this.tasks.indexOf(task), 1)
        },
    },

    computed: {
        incompletedTasks: function() {
            return this.tasks.filter(function(task) {
                return !task.isCompleted
            })
        },
        completedTasks: function() {
            return this.tasks.filter(function(task) {
                return task.isCompleted
            })
        },
    },
})