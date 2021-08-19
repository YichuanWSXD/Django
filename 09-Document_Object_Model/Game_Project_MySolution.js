
var restartBut = document.querySelector('#restartBut')
restartBut.addEventListener('click', clearBoard)



var gameContent = document.querySelector('.gameContent');
var square = gameContent.querySelectorAll('td');

for (var td of square){
  td.addEventListener('click', playGame);
}






function playGame(){
  if (this.textContent === 'X'){
    this.textContent = 'O';
  }else if (this.textContent === ''){
    this.textContent = 'X';
  }else if (this.textContent === 'O'){
    this.textContent = '';
  }
}

function clearBoard(){
  for (var td of square){
    td.textContent = '';
  }
}
