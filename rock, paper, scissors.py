print("ROCK PAPER SCISSORS")
print()
print("Select your move Rock,Paper or Scrissors")
print()

player1_score = 0
player2_score = 0

while True:   

  
  player1Move = input("Player 1 > ")
  print()
  player2Move = input("Player 2 > ")
  print()
  
  if player1Move == "Rock" or player1Move == "rock":
    if player2Move == "Rock" or player2Move == "rock":
      print("You both picked Rock, draw!")
    elif player2Move == "Scissors" or player2Move == "scissors":
      print("Player1 smashed Player2's Scissors into dust with their Rock!")
      player1_score += 1
    elif player2Move == "Paper" or player2Move == "paper":
      print("Player1's Rock is smothered by Player2's Paper!")
      player2_score += 1
    else:
      print("Invalid Move Player 2!")
  elif player1Move == "Paper" or player1Move == "paper":
    if player2Move == "Rock" or player2Move == "rock":
      print("Player2's Rock is smothered by Player1's Paper!")
      player1_score += 1
    elif player2Move == "Scissors" or player2Move == "scissors":
      print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
      player2_score += 1
    elif player2Move == "Paper" or player2Move == "paper":
      print("Two bits of paper flap at each other. Dissapointing. Draw.")
    else:
      print("Invalid Move Player 2!")
  elif player1Move == "Scissors" or player1Move == "scissors":
    if player2Move == "Rock" or player2Move == "rock":
      print("Player 2's Rock makes metal-dust out of Player1's Scissors")
      player2_score += 1
    elif player2Move == "Scissors" or player2Move == "scissors":
      print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
    elif player2Move == "Paper" or player2Move == "paper":
      print("Player1's Scissors make confetti out of Player2's paper!")
      player1_score += 1
    else:
      print("Invalid Move Player 2!")
  else:
    print("Invalid Move Player 1!")

  
  print("Player 1 has", player1_score, "wins.")
  print("Player 2 has", player2_score, "wins.")

  if player1_score==3 or player2_score==3:
    print("Thanks for playing!")
    exit()
  else:

    continue
