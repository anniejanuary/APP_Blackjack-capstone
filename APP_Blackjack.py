############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []



def check_result (sum_user, sum_computer):
  '''check if scores == & > 21 ?'''
  
  #DOES USER OR COMPUTER HAVE A BLACKJACK == 21 ?
  if sum_user == 21 and len(user_cards) == 2: # checking if 10 and 11 in cards
    print("\nYou have a Blackjack, you win! 🤩")
    final_score()
  elif sum_computer == 21 and len(computer_cards) == 2:
    print("\nComputer has a Blackjack, you lose! ☠️")
    final_score()

  #DOES USER SCORE >21?
  if sum_user > 21:
    if 11 in user_cards:
      
      replace_ace(sum(user_cards))
      
      print(f"    Your cards after replacing 11 with 1: {user_cards}, current score: {sum(user_cards)}")
      check_result (sum(user_cards), sum(computer_cards))
      
    else:
      print("\nYou lose! ☠️")
      final_score()

  #DOES COMPUTR SCORE >21?
  if sum_computer > 21:
    print("\nYou win! 😄")
    final_score()


def replace_ace (sum_user):
      '''REPLACING ACE's VALUE using For Loop'''
      for i in range(len(user_cards)):
        if user_cards[i] == 11:
          user_cards[i] = 1

      return user_cards   # got to return user_cards to change a parameter's value inside a function
      


def another_card (yes, no):
  '''Deal a new card'''
  if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
    user_cards.append(random.choice(cards))
    print(f"    Your cards: {user_cards}, current score: {sum(user_cards)}")

  else:
    user_didnt_take_another_card (sum(user_cards), sum(computer_cards))


  
def user_didnt_take_another_card (sum_user, sum_computer):
  '''Computer taking cards after user has stopped taking cards'''
  while sum_computer < 17:  
    next_computer_card = random.choice(cards)
    computer_cards.append(next_computer_card)
    sum_computer += next_computer_card
  if sum_computer >= 17:
      print(f"    Computer's cards: {computer_cards}, current score: {sum_computer}")
      check_result (sum(user_cards), sum(computer_cards))
      final_count (sum(user_cards), sum(computer_cards))

  
def final_count (sum_user, sum_computer):
    '''Final score count'''
    if sum_computer > sum_user:
      print("\nYou lose! ☠️")
      final_score()
    elif sum_computer == sum_user:
      print("\nIt's a draw 😐")
      final_score()
    elif sum_computer < sum_user:
      print("\nYou win! 😄")
      final_score()
  
  
def final_score ():
  '''Show the final scores and ask if user wants to play again'''
  print(f"Your final cards: {user_cards}, final score: {sum(user_cards)}")
  print(f"Computer's final cards: {computer_cards}, final score: {sum(computer_cards)}")
  
  play_again = input("Would you like to play again? 🤨 y or n: ")    
  while play_again == 'y':
    is_game_over = False
    user_cards.clear()
    computer_cards.clear()
    new_game()
  else:
    print("Goodbye then! 👋")
    exit() #my issue w switching the is_game_over flag to True not working: 
           #https://stackoverflow.com/questions/73662743/pythonafter-i-choose-not-to-play-again-why-does-it-ask-me-again-if-i-want-anot


def new_game ():
  clear()
  from art import logo
  print(logo)
    
  global cards
  global user_cards
  global computer_cards
  global is_game_over

  is_game_over = False
  
  #USER ROUND 1: 2 cards
  for _ in range (2): #it just runs the number in range, twice (doesnt matter whats after "for")
    user_cards.append(random.choice(cards))
    
  computer_cards.append(random.choice(cards))
  print(f"    Your cards: {user_cards}, current score: {sum(user_cards)}")
  print(f"    Computer's first card: {computer_cards}")
  
  while is_game_over == False:
    check_result (sum(user_cards), sum(computer_cards))
    another_card ('y', 'n')


##### INITIATING THE GAME
new_game()





