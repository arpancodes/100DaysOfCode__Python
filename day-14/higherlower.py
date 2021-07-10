from game_data import data
from art import logo, vs
import random


print(logo)
score = 0

while True:
	x = random.randint(0, len(data) - 1)
	first = data[x]
	second = data[x+1]
	print(first["name"])
	print(f"A. {first['name']}, {first['description']}, {first['country']}")
	print(vs)
	print(f"B. {second['name']}, {second['description']}, {second['country']}")
	choice = input("Who do you think has the higher followers? A or B: ").lower()

	if choice == "a":
		if first["follower_count"] > second["follower_count"]:
			score += 1
			print("====================================================")
			print("Correct!")
			print("====================================================")
		else:
			print("Wrong Answer!")
			break
	else:
		if first["follower_count"] < second["follower_count"]:
			score += 1
			print("====================================================")
			print("Correct!")
			print("====================================================")
		else:
			print("Wrong Answer!")
			break

print(f"Game over! your score was: {score}")
