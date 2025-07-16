import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(list_cards):
    random_card = random.choice(list_cards)
    return random_card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, opponent_score):
    if player_score == opponent_score:
        return 'Draw'
    elif opponent_score == 0:
        return "Lose, opponent has BlackJack"
    elif player_score == 0:
        return "Winner by a BlackJack"
    elif player_score > 21:
        return "You went over. You Lose"
    elif opponent_score > 21:
        return "Opponent went over. You win!"
    elif player_score > opponent_score:
        return "You Win!"
    else:
        return "You Lose"

def blackjack_game():
    print(logo)
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card(cards))
        computer_cards.append(deal_card(cards))

    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f'Your cards: {user_cards}, Current Score: {user_score}')
        print(f'Computer\'s first card: {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card(cards))
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card(cards))
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Main loop to play the game
while input('Do you want to play a game of BlackJack? Type \'y\' or \'n\': ').lower() == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')
    blackjack_game()
