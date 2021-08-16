
var firstName = prompt('What is your first name?')
var lastName = prompt('What is your last name?')
var age = prompt('How old are you?')
var height = prompt("How tall are you?")
var petName = prompt("What is your pet's name?")
alert("Thank you so much for the information!")


var nameCheck = false
var ageCheck = false;
var heightCheck = false;
var petNameCheck = false;

// name condition
if (firstName[0] === lastName[0]){
  nameCheck = true
}

// age condition
if (20 < age < 30){
  ageCheck = true
}

// height condition
if (height >= 170){
  heightCheck = true
}

// Pet condition

if (petName[petName.length - 1] === 'y'){
  petNameCheck = true
}


if (nameCheck && ageCheck && heightCheck && petNameCheck){
  console.log("Welcome Comrade! You've passed the Spy Test")
}
