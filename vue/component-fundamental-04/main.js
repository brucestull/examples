// Start server:
// python -m http.server 8000

Vue.component('component-element-name', {
    props: {
        theloneprop: Object,
    },
    template: `
    <p>
    {{ theloneprop.id }} : {{ theloneprop.description }}!
    </p>
    `
})


const app1 = new Vue({
    el: '#app1',
    data: {
        globalPropertyList: [
            {
                id: 1,
                description: 'The First Thing in the List!'
            },
            {
                id: 2,
                description: 'The SECOND Thing in the List?'
            },
        ]
    }
})