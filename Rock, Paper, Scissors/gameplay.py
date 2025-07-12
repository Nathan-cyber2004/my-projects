import random
from ascii_art import rock, paper, scissors

def opponent_choice():
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  return computer_choice

def user_choice():
  while True:
    user_choice = input("Choose either rock, paper, or scissors: ").lower()
    if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
      break
    else:
      print("Invalid choice, please choose either rock, paper, or scissors...")
  
  return user_choice
  
def display_art(choice):
  if choice == "rock":
    print(rock)
  elif choice == "paper":
    print(paper)
  elif choice == "scissors":
    print(scissors)
  else:
    print("Unrecognized choice...")

def determine_winner(player_choice, opponent_choice):
  if player_choice == "rock" and opponent_choice == "scissors":
    return "You win!"
  elif player_choice == "paper" and opponent_choice == "rock":
    return "You win!"
  elif player_choice == "scissors" and opponent_choice == "paper":
    return "You win!"
  elif player_choice == opponent_choice:
    return "Tie game"
  else:
    return "You lose!"

def game_logic():
  playing = True
  player_score = 0
  computer_score = 0
  counter = 0

  while True:
    try:
      num_rounds = int(input("How many rounds would you like to play? "))
      break
    except:
      print("Invalid input, please enter again")
  

  while playing:
    computer_choice = opponent_choice()
    player_choice = user_choice()

    print("You chose...")
    display_art(player_choice)
    print("") # Newline for better readability
    print("Computer chose...")
    display_art(computer_choice)
    print("")

    winner = determine_winner(player_choice, computer_choice)
    if winner == "You win!":
      print(winner)
      counter += 1
      player_score += 1
    elif winner == "Tie game":
      print(winner)
      counter += 1
    elif winner == "You lose!":
      print(winner)
      counter += 1
      computer_score += 1

    if counter == num_rounds:
      playing = False
  
  if player_score > computer_score:
    print("You win the game!")
    print("You won " + str(player_score) + " out of " + str(num_rounds))
  elif player_score == computer_score:
    print("It's a tie...")
    print("You won " + str(player_score) + " out of " + str(num_rounds))
  else:
    print("Sorry, the computer has won")
    print("You won " + str(player_score) + " out of " + str(num_rounds))
  
  while True:
    user_quit = input("Would you like to play again? (Type 'y' or 'n'): ").lower()
    if user_quit == "n":
      print("Thanks for playing!")
      break
    else:
      game_logic()
