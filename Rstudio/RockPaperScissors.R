actions <- c("rock", "scissors", "paper", "exit")

win <- 0
loss <- 0
tie <- 0

while(TRUE) {
  player_move <- as.numeric(readline("Choose your move: rock[1], scissors[2], paper[3], exit[0]: "))
  if (player_move == 0) {
    message("Goodbye:D")
    break
  }
  
  player_move <- actions[player_move]
  computer_move <- actions[sample(1:3, 1)]
  
  if (player_move == computer_move) {
    message("TIE ")
    tie <- tie + 1
  } else if (player_move == "rock" & computer_move == "scissors") {
    message("you win ")
    win <- win + 1
  } else if (player_move == "scissors" & computer_move == "paper") {
    message("you win ")
    win <- win + 1
  } else if (player_move == "paper" & computer_move == "rock") {
    message("you win ")
    win <- win + 1
  } else {
    message("you lose ")
    loss <- loss + 1
  }
  
  
  message("Player Move:", player_move, "\n")
  message("Computer Move:", computer_move, "\n")
  message("WIN ", win)
  message("LOSS ", loss)
  message("TIE ", tie)
  
}
