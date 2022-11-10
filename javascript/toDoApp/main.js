let addButton = document.getElementById("add-button")
let textInput = document.getElementById("the-input")

let completeListUL = document.getElementById("complete-list")
let incompleteListUL = document.getElementById("incomplete-list")


// Function to add a ToDo:
function addToDo(text=textInput.value) {

    let completeButton = document.createElement("button")
    completeButton.id = "complete-button"
    completeButton.innerText = "Complete"
    completeButton.addEventListener('click', function() {
        console.log("Completing: ", completeButton.previousSibling.innerText)
        completeTheTodo(completeButton.previousSibling)
    })

    let deleteButton = document.createElement("button")
    deleteButton.id = "delete-button"
    deleteButton.innerText = "Delete"
    deleteButton.addEventListener('click', function() {
        deleteElementAndParent(deleteButton)
    })

    let newToDoLI = document.createElement("li")
    let newToDoSpan = document.createElement("span")
    newToDoSpan.innerText = text

    newToDoLI.appendChild(newToDoSpan)
    newToDoLI.appendChild(completeButton)
    newToDoLI.appendChild(deleteButton)

    incompleteListUL.append(newToDoLI)
    textInput.value = ''
    textInput.focus()
}


// Function to complete a ToDo:
function completeTheTodo(toDoItem) {

    let incompleteButton = document.createElement("button")
    incompleteButton.id = "incomplete-button"
    incompleteButton.innerText = "Incomplete"
    incompleteButton.addEventListener('click', function() {
        console.log("Incompleting or Adding: ", incompleteButton.previousSibling.innerText)
        incompleteTheTodo(incompleteButton.previousSibling)
    })

    let deleteButton = document.createElement("button")
    deleteButton.id = "delete-button"
    deleteButton.innerText = "Delete"
    deleteButton.addEventListener('click', function() {
        deleteElementAndParent(deleteButton)
    })

    let newCompletedLI = document.createElement("li")
    let newCompletedSpan = document.createElement("span")
    newCompletedSpan.innerText = toDoItem.innerText
    newStrikeThroughSpan = addSTag(newCompletedSpan)

    newCompletedLI.appendChild(newStrikeThroughSpan)
    newCompletedLI.appendChild(incompleteButton)
    newCompletedLI.appendChild(deleteButton)

    completeListUL.append(newCompletedLI)

    toDoItem.parentElement.remove()
}

function incompleteTheTodo(toDoItem) {
    addToDo(toDoItem.innerText)
    toDoItem.parentElement.remove()
}


function addSTag(element) {
    let newSTag = document.createElement('s')
    newSTag.appendChild(element)
    return newSTag
}


function deleteElementAndParent(element) {
    console.log("Deleting: ", element.parentElement.firstChild.innerText)
    element.parentElement.remove()
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





