let numbers = { zero: "Is the literal 'zero'!", one: "Is the literal 'one'?" }

console.log('numbers: ', numbers)

// let firstUserInput = prompt("Enter 'zero' or 'one', NOW!!!")
let firstUserInput = 'zero'

console.log('firstUserInput: ', firstUserInput)
// firstUserInput:  zero

console.log('numbers.zero: ', numbers.zero)
// numbers.zero:  Is the literal 'zero'!
console.log('numbers.one: ', numbers.one)
// numbers.one:  Is the literal 'one'?

// Now, try to get the value, which the user enters, from the object 'numbers'.

console.log('numbers.firstUserInput: ', numbers.firstUserInput)
// numbers.firstUserInput:  undefined
console.log('numbers[firstUserInput]: ', numbers[firstUserInput])
// numbers[firstUserInput]:  Is the literal 'zero'!