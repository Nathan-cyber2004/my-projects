import random

def get_opponent():
  '''
  This function will get user input and return either True or False
  True - User is playing against the computer
  False - User is playing against a friend
  '''
  desired_opponent = input("Would you like to play against a computer or with your friend? (Type 'computer' or 'friend'): ").lower()
  if desired_opponent == "computer":
    return True
  else:
    return False

def assign_player_symbol(computer_opponent):
   '''
   This function assigns both players either 'X' or 'O'
   '''
   options = ["X", "O"]
   choosing_symbol = True
   player_one = "X" # Place holder
   player_two = player_one

   if computer_opponent == True:
    
    while choosing_symbol:
      player_one = input("What symbol would you like? (Type 'X' or 'O'): ").upper()
      if player_one != "X" and player_one != "O":
         print("Please choose a valid symbol...")
      else:
         choosing_symbol = False

    while player_two == player_one:
        player_two = random.choice(options)
   else:
    player_one = random.choice(options)

    while player_two == player_one:
       player_two = random.choice(options)

   return player_one, player_two

def initialize_board():
  return [["_", "_", "_"] for _ in range(3)]

def display_board(board):
  for row in board:
    print(" | ".join(row))

def user_input(board, symbol, player_name):
    print(f"{player_name}'s turn:")
    while True:
        row_input = input("Choose a row number (1-3) or Q to quit: ").strip() # .strip() for better error handling
        if row_input.lower() == "q":
            return "Q"
        col_input = input("Choose a col number (1-3) or Q to quit: ").strip()
        if col_input.lower() == "q":
            return "Q"
        try:
            row_num = int(row_input) - 1
            col_num = int(col_input) - 1
            if row_num not in range(3) or col_num not in range(3):
                print("Invalid position. Please choose numbers between 1 and 3.")
                continue
            if board[row_num][col_num] != "_":
                print("That spot is already taken. Please choose another.")
                continue
            board[row_num][col_num] = symbol
            break
        except ValueError:
            print("Please enter valid numbers.")

def computer_input(board, computer_symbol):
  print("The computer's turn: ")
  choices = [0, 1, 2]
  is_choosing = True

  while is_choosing:
    computer_row = random.choice(choices)
    computer_col = random.choice(choices)
    chosen_spot = board[computer_row][computer_col]
    if chosen_spot == "_":
      board[computer_row][computer_col] = computer_symbol
      is_choosing = False

def determine_winner(board, symbol):
    '''
    Checks for winner by looping through the list of lists
    '''
  # Check rows
    for row in board:
        if all(elem == symbol for elem in row): 
           return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == symbol for i in range(3)): # Top left to bottom right
        return True
    if all(board[i][2 - i] == symbol for i in range(3)): # Top right to bottom left
        return True

    return False

def determine_tie(board):
   return all(cell != "_" for row in board for cell in row)

def end_game(board, user, opponent, winner_player = "sample"):
  playing = True
  if determine_winner(board, user):
    print(f"Congratulations! {winner_player} wins!")
    playing = False
  elif determine_winner(board, opponent): # Opponent is the computer
      print("Sorry, you lose...\nThe Computer has won.")
      playing = False
  elif determine_tie(board):
    print("It's a tie...")
    playing = False
  return playing

def game_logic():
  print("Welcome to this simple Tic Tac Toe game!")
  playing = True
  desired_opponent = get_opponent()

  if desired_opponent == True:
     print("You will play against the computer!")
     player, computer = assign_player_symbol(True)
  else:
     print("You will play with a friend!")
     player_one, player_two = assign_player_symbol(False)
  
  board = initialize_board()
  display_board(board)
  print("")

  try: # If the variable 'computer' doesn't exist, an Unbound Local Error will occur which calls the two player logic
    if computer:
      print("You will go first!")
      while playing:
        if user_input(board, player, "Player One") == "Q":
           playing = False
        display_board(board)
        playing = end_game(board, player, computer, winner_player = "Player")
        if not playing:
          break
        computer_input(board, computer)
        display_board(board)
        playing = end_game(board, player, computer)
      
  except UnboundLocalError:
     print(f"Player one will go first! You are using {player_one}'s")
     while playing:
      if user_input(board, player_one, "Player One") == "Q":
         playing = False
      display_board(board)
      playing = end_game(board, player_one, player_two, winner_player = "Player One")
      if not playing:
        break
      if user_input(board, player_two, "Player Two") == "Q":
         playing = False
      display_board(board)
      playing = end_game(board, player_one, player_two, winner_player = "Player Two")
  
  finally:
     play_again = input("Would you like to play again? (Type 'y' or 'n'): ")
     if play_again == "y":
        game_logic()
     else:
        print("Thanks for playing!")