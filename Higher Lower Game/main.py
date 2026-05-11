# Project 12: Higher or Lower Game

import random
from game_data import data
from art import logo, vs

# Defining functions

def get_name():
  position = random.randint(0, len(data))
  for _ in range(len(data)):
    name = data[position]['name']
  return name

def get_follower_count(person):
  for num in range(len(data)):
    if data[num]['name'] == person:
      follower_count = data[num]['follower_count']
  return follower_count

def get_description(person):
  for num in range(len(data)):
    if data[num]['name'] == person:
      description = data[num]['description']
  return description

def get_country(person):
  for num in range(len(data)):
    if data[num]['name'] == person:
      country = data[num]['country']
  return country

# Game logic
playing = True

# Assigning variables
person_a = get_name()
person_b = get_name()
score = 0

while playing:

  a_follower_count = get_follower_count(person_a)
  b_follower_count = get_follower_count(person_b)

  a_description = get_description(person_a)
  b_description = get_description(person_b)

  a_country = get_country(person_a)
  b_country = get_country(person_b)

  print(logo)
  print(f'Compare A: {person_a}, {a_description}, from {a_country}')
  print(vs)
  print(f'Against B: {person_b}, {b_description}, from {b_country}')

  user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  if a_follower_count == b_follower_count:
    print('Equal Follower Count...')

  if user_guess == 'a' and a_follower_count > b_follower_count:
    print('Correct!')
    score += 1
    print(f'Current Score: {score}')
  elif user_guess == 'a' and a_follower_count < b_follower_count:
    print('Incorrect')
    print(f'Current Score: {score}')
    playing = False
  elif user_guess == 'b' and b_follower_count > a_follower_count:
    print('Correct!')
    score += 1
    print(f'Current Score: {score}')
  elif user_guess == 'b' and b_follower_count < a_follower_count:
    print('Incorrect')
    print(f'Current Score: {score}')
    playing = False
  
  person_a = person_b
  person_b = get_name()

  while person_a == person_b:
    person_b = get_name()