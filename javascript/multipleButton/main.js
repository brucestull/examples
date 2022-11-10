let oneButton = document.createElement('button')
CLICK_ME = "Click Me!"
oneButton.innerText = CLICK_ME

function createAButton() {
    let newButton = document.createElement('button')
    const randoString = Math.random().toString(16)
    newButton.innerText = randoString.slice(-8,-1)
    return newButton
}

let divOne = document.getElementById('div-one')
divOne.appendChild(createAButton())

let divTwo = document.getElementById('div-two')
divTwo.appendChild(createAButton())

let divThree = document.getElementById('div-three')
divThree.appendChild(createAButton())

