import random
from art import logo
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
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)

def deal_card(num):
	dealt = []
	for _ in range(num):
		dealt.append(random.choice(cards))
	return dealt


#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = [] + deal_card(2)
computer_cards = [] + deal_card(2)


#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.wq676q56767
def calculate_score(cards_in_hand):
	if len(cards_in_hand) == 2 and cards_in_hand[0] + cards_in_hand[1] == 21:
		return 0
	sum = 0
	for x in cards_in_hand:
		sum += x
	if 11 in cards_in_hand and sum > 21:
		cards_in_hand.remove(11)
		sum -= 11
		cards_in_hand.append(1)
		sum += 1
	return sum


game_ended = False
def compare():
	global game_ended
	if game_ended:
		if user_score == computer_score:
			print("Draw")
		elif user_score > computer_score:
			print("You won")
		else:
			print("Computer won")
	else:
		if user_score == 0:
			game_ended = True
			print("You won")
		elif computer_score == 0:
			game_ended = True
			print("Computer won")
		elif user_score > 21:
			game_ended = True
			print("Computer won")
			return -1
		elif computer_score > 21:
			game_ended = True
			print("You won")



user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f"Your cards: {user_cards}")
print(f"computer cards: [{computer_cards[0]}]")
compare()

user = None

while not game_ended:
	if input("Do you want to draw more card? [y/N]") == "y":
		user_cards += deal_card(1)
		user_score = calculate_score(user_cards)
		print(f"Your cards: {user_cards}")
		user = compare()
	else:
		game_ended = True

while computer_score < 17:
	computer_cards += deal_card(1)
	computer_score = calculate_score(computer_cards)

if user != -1:
	print(f"Your cards: {user_cards}")
	print(f"computer cards: {computer_cards}")
	compare()


#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
