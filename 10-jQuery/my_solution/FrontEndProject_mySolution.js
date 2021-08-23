

var player1 = prompt('Player One: Enter Your Name, you will be Blue')
var player1Color = 'rgb(86, 151, 255)';
var player2 = prompt('Player two: Enter Your Name, you will be Red')
var player2Color = 'rgb(237, 45, 73)';
var defaultColor = 'rgb(51, 51, 51)';

// update the names when the names were not assigned by users.
if (player1 === null){
  player1 = 'player1'
}

if (player2 === null){
  player2 = 'player2'
}

var round = 1;
var keep_playing = true;
var result = 0;

updateH3(round % 2);




$('button').click(function(){
  if (result == 1){
    return;
  }
  var col = $(this).closest('td').index();

  var row = updateBoard(col, round % 2);
  if (row === -1){
    return;
  }
  result = checkWinner(col, row);
  if (result){
    if (round % 2 == 0){
      $('h1').html(player2 + ' has won! Refresh your browser to play again!')
    }else{
      $('h1').html(player1 + ' has won! Refresh your browser to play again!')
    }
    $('h2').html('');
    $('h3').html('');

  }
  round += 1;
  if (!result){
    updateH3(round % 2);
  }

})

function updateBoard(col, player){
  // given the clicked column and current player, put the chess into the board if the column is not full and return the row of the chess. Otherwise return -1.
  for (var row = 5; row >= 0; row--){
    // console.log($('tr').eq(row).children(0).eq(col).children(0).css('background-color'));
    if ($('tr').eq(row).children(0).eq(col).children(0).css('background-color') === 'rgb(128, 128, 128)'){
      foundColor = 1
      break;
    }
  }
  if (row == -1){
    return row;
  }
  if (player == 1){
    $('tr').eq(row).children(0).eq(col).children(0).css('background-color', 'rgb(86,151,255)')
  } else{
    $('tr').eq(row).children(0).eq(col).children(0).css('background-color', 'rgb(237, 45, 73)')
  }
  return row;
}

function updateH3(player){
  // take the player id (0 for player2; 1 for player1) and update the game status with palyer name
  if (player == 1){
    $('h3').html(player1 + ': it is your turn, please pick a column to drop your blue chip.')
  } else{
    $('h3').html(player2 + ': it is your turn, please pick a column to drop your red chip.')
  }
}

function checkWinner(col, row){
  // input: last chess location
  // return: 1 if this is a win move, 0 otherwise.
  curColor = $('tr').eq(row).children(0).eq(col).children(0).css('background-color');
  // horizontal
  var cnt = 1;
  for (let shiftCol = 1; shiftCol < 7; shiftCol++){
    let newCol = col + shiftCol;
    if (newCol < 0 || newCol > 6 || $('tr').eq(row).children(0).eq(newCol).children(0).css('background-color') != curColor){
      break;
    }
    cnt ++;
  }
  for (let shiftCol = -1; shiftCol > -7; shiftCol--){
    let newCol = col + shiftCol;
    if (newCol < 0 || newCol > 6 || $('tr').eq(row).children(0).eq(newCol).children(0).css('background-color') != curColor){
      break;
    }
    cnt ++
  }
  if (cnt >= 4){
    return 1;
  }

  // vertical
  cnt = 1;
  for (let shiftRow = 1; shiftRow < 7; shiftRow++){
    let newRow = row + shiftRow;
    if (newRow < 0 || newRow > 5 || $('tr').eq(newRow).children(0).eq(col).children(0).css('background-color') != curColor){
      break;
    }
    cnt ++;
  }
  for (let shiftRow = -1; shiftRow > -7; shiftRow--){
    let newRow = row + shiftRow;
    if (newRow < 0 || newRow > 5 || $('tr').eq(newRow).children(0).eq(col).children(0).css('background-color') != curColor){
      break;
    }
    cnt ++;
  }
  if (cnt >= 4){
    return 1;
  }

  // diagonal top left
  cnt = 1;
  for (let shift = 1; shift < 7; shift++){
    let newRow = row + shift;
    let newCol = col - shift;
    if (newRow < 0 || newRow > 5 || newCol < 0 || newCol > 6 || $('tr').eq(newRow).children(0).eq(newCol).children(0).css('background-color') != curColor){
      break;
    }
    cnt ++;
  }
  for (let shift = 1; shift < 7; shift++){
    let newRow = row - shift;
    let newCol = col + shift;
    // console.log(newRow, newCol);
    if (newRow < 0 || newRow > 5 || newCol < 0 || newCol > 6 || $('tr').eq(newRow).children(0).eq(newCol).children(0).css('background-color') != curColor){
      break;
    }
    cnt ++;
  }

  if (cnt >= 4){
    return 1;
  }

  // diagonal top right
  cnt = 1;
  for (let shift = 1; shift < 7; shift++){
    let newRow = row + shift;
    let newCol = col + shift;
    if (newRow < 0 || newRow > 5 || newCol < 0 || newCol > 6 || $('tr').eq(newRow).children(0).eq(newCol).children(0).css('background-color') != curColor){
      break;
    }
    cnt ++;
  }
  for (let shift = 1; shift < 7; shift++){
    let newRow = row - shift;
    let newCol = col - shift;

    if (newRow < 0 || newRow > 5 || newCol < 0 || newCol > 6 || $('tr').eq(newRow).children(0).eq(newCol).children(0).css('background-color') != curColor){
      break;
    }
    cnt ++;
  }
  if (cnt >= 4){
    return 1;
  }





  return 0

}
