import random

options = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
, '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
,'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

user = int(input("Choose rock(1), paper(2) or sciccors (3): ")) - 1
computer  = random.randint(0,2)
winner = "Draw"
if (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
	winner = "You won"
elif (user == 2 and computer == 0) or (user == 0 and computer == 1) or (user == 1 and computer == 2):
	winner = "Computer won"


print(f"You chose: {options[user]}")
print(f"Computer chose: {options[computer]}")
print(winner)
