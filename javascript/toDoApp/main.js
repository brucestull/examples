let addButton = document.getElementById("add-button")
let textInput = document.getElementById("the-input")

let completeListUL = document.getElementById("complete-list")
let incompleteListUL = document.getElementById("incomplete-list")

let styleButton = document.getElementById("style-button")

let testDiv = document.getElementById("test-div")


// <ul>
// <li>string<button></button></li>
// </ul>


// Function to add a ToDo:
function addToDo() {
    console.log("We're trying to add a new item!!!")

    let completeButton = document.createElement("button")
    completeButton.id = "complete-button"
    completeButton.innerText = "Complete"
    completeButton.addEventListener('click', function() {
        // console.log("'Complete' button clicked!!")
        console.log("Completing: ", completeButton.previousSibling)
        completeTheTodo(completeButton.previousSibling)
    })

    console.log(completeButton)

    let newToDoLI = document.createElement("li")
    newToDoLI.innerText = textInput.value
    newToDoLI.appendChild(completeButton)

    incompleteListUL.append(newToDoLI)
    // textInput.value = ""
    textInput.focus()
}


function completeTheTodo(toDoItem) {
    // console.log("We're trying to complete the ITEM!")
    console.log('The ITEM: ', toDoItem)

    let incompleteButton = document.createElement("button")
    incompleteButton.id = "incomplete-button"
    incompleteButton.innerText = "Incomplete"
    incompleteButton.addEventListener('click', function() {
        // console.log("'Incomplete' button clicked!!")
        console.log("Incompleting: ", incompleteButton.previousSibling)
    })
    // console.log(incompleteButton)

    // toDoItem = "Totally a New String... Not an old one."

    let newCompletedLI = document.createElement("li")
    newCompletedLI.innerText = toDoItem
    newCompletedLI.appendChild(incompleteButton)

    completeListUL.append(newCompletedLI)

    toDoItem.parentElement.remove()
}


// Add listener for 'Enter' keyup event:
textInput.addEventListener("keyup", function(e) {
    if (e.key === "Enter") {
        addToDo()
    }
})


// Add listener for 'addButton' click event:
addButton.addEventListener("click", () => {
    addToDo()
})


styleButton.addEventListener("click", function() {
    console.log("We're trying to change the STYLE???")
})

// document.getElementById(id).style.property = new style


////////////////////////////////////////
// Create <ol> element:
let testListOL = document.createElement('ol')
// Create <li> element:
let testLI = document.createElement('li')
// Add 'innerText' to the <li> element:
testLI.innerText = "The Stuff in the LI!"
// Add a <button> at the end of the <li> element, right after the 'innerText':
testLI.appendChild(document.createElement("button"))
// Put the <li> at the end of the <ol> element:
testListOL.appendChild(testLI)
// Puth the <ol> element at the end of the <div> element:
testDiv.appendChild(testListOL)



//     newToDoLI.classList.add("incomplete-todo")
