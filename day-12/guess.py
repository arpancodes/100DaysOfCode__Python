import random
from art import logo
print(logo)
print("Welcome to the best number guessing game, you need to guess a number between 1 to 100: ")

level = input('Please choose a level between "easy" and "hard": ')

if level == "easy":
	guesses = 10
else:
	guesses = 5

randomNumber = random.randint(1, 100)


print(f"You have {guesses} guesses to guess the number!")

won = False

while guesses > 0 and not won:
	guess = int(input(f"Make a guess ({guesses} remaining): "))
	if guess < randomNumber:
		print("Too LOW")
	elif guess > randomNumber:
		print("Too HIGH")
	else:
		print("You won!")
		won = True
	guesses -= 1

if not won:
	print(f"You lost!, the number was {randomNumber}")
