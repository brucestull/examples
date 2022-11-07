let numbers = { zero: "Is the literal 'zero'!", one: "Is the literal 'one'?" }

console.log('numbers: ', numbers)

// let firstUserInput = prompt("Enter 'zero' or 'one', NOW!!!")
let firstUserInput = 'zero'

console.log('firstUserInput: ', firstUserInput)

console.log('numbers.zero: ', numbers.zero)
console.log('numbers.one: ', numbers.one)

// Now, try to get the value, which the user enters, from the object 'numbers'.

console.log('numbers.firstUserInput: ', numbers.firstUserInput)
// numbers.firstUserInput:  undefined
console.log('numbers[firstUserInput]: ', numbers[firstUserInput])
// numbers[firstUserInput]:  Is the literal 'zero'!