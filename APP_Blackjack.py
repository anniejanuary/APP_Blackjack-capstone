############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def new_game ():

  clear()
  from art import logo
  print(logo)

  #USER ROUND 1: 2 cards
  for _ in range (2): #it just runs the number in range, twice (doesnt matter whats after "for")
    user_cards.append(random.choice(cards))
    print(f"    Your cards: {user_cards}, current score: {sum(user_cards)}")

  #COMPUTER ROUND 1: 1 card
  computer_cards.append(random.choice(cards))
  print(f"    Computer's cards: {computer_cards}, current score: {sum(computer_cards)}")

  check_result (sum(user_cards), sum(computer_cards))
  another_card ('y', 'n')
  

# CHECK SCORES == & > 21 ?
def check_result (sum_user, sum_computer):
  global cards
  global user_cards
  global computer_cards
  
  #DOES USER OR COMPUTER HAVE A BLACKJACK == 21 ?
  if sum_user == 21 and len(user_cards) == 2: # checking if 10 and 11 in cards
    print("You have a Blackjack, you win! 🤩")
    play_again('y', 'n')
  elif sum_computer == 21 and len(computer_cards) == 2:
    print("Computer has a Blackjack, you lose! ☠️")
    play_again('y', 'n')

  #DOES USER SCORE >21?
  if sum_user > 21:
    if 11 in user_cards:
      
      replace_ace(sum(user_cards))
      
      print(f"    Your cards after replacing 11 with 1: {user_cards}, current score: {sum(user_cards)}")
      check_result (sum(user_cards), sum(computer_cards))
      
    else:
      print("You lose! ☠️")
      play_again('y', 'n')

  #DOES COMPUTR SCORE >21?
  if sum_computer > 21:
    print("You win! 😄")
    play_again('y', 'n')

# REPLACING ACE's VALUE using For Loop
def replace_ace (sum_user):
    for i in range(len(user_cards)):
      if user_cards[i] == 11:
        user_cards[i] = 1
  
    # why doesnt this work?:
    #REPLACING ACE's VALUE from 11 to 1 using LIST COMPREHENSION
    #user_cards = [1 if card == 11 else cards for card in user_cards]
  
    return user_cards   # got to return user_cards to change a parameter's value inside a function
  
# ANOTHER CARD
def another_card (yes, no):
  if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
    user_cards.append(random.choice(cards))
    print(f"    Your cards: {user_cards}, current score: {sum(user_cards)}")
    check_result (sum(user_cards), sum(computer_cards))
    
    user_took_another_card (sum(user_cards), sum(computer_cards))
  else:
    user_didnt_take_another_card (sum(user_cards), sum(computer_cards))

    
#COMPUTER NEXT ROUNDS after if another_card_choice == 'y':
def user_took_another_card (sum_user, sum_computer):
  if sum_computer < 17:  
    computer_cards.append(random.choice(cards))
    sum_computer
    print(f"    Computer's cards: {computer_cards}, current score: {sum_computer}")
    check_result (sum(user_cards), sum(computer_cards))
    another_card ('y', 'n')
  else:
      check_result (sum(user_cards), sum(computer_cards))
      another_card ('y', 'n')
      
  check_result (sum(user_cards), sum(computer_cards))

  
#COMPUTER NEXT ROUNDS after if another_card_choice == 'n':
def user_didnt_take_another_card (sum_user, sum_computer):
  while sum_computer < 17:  
    next_computer_card = random.choice(cards)
    computer_cards.append(next_computer_card)
    sum_computer += next_computer_card
    print(f"    Computer's cards: {computer_cards}, current score: {sum_computer}")
  if sum_computer >= 17:
      check_result (sum(user_cards), sum(computer_cards))
      final_count (sum(user_cards), sum(computer_cards))

  
# FINAL COUNT 
def final_count (sum_user, sum_computer):
  if sum_computer > sum_user:
      print("You lose! ☠️")
      play_again('y', 'n')
  elif sum_computer == sum_user:
      print("It's a draw 😐")
      play_again('y', 'n')
  elif sum_computer < sum_user:
      print("You win! 😄")
      play_again('y', 'n')
    
    
# RESTART THE GAME ?
def play_again (yes, no):
  again = input("Would you like to play again? 🤨 y or n: ")
  if again == yes:
    user_cards.clear()
    computer_cards.clear()
    new_game()
  else:
    print("Goodbye then! 👋")
    keep_playing = False
    exit() ### break is not working if i place it in the while Keep_playing loop below


keep_playing = True    

##### INITIATING THE GAME
while keep_playing:
  new_game()

