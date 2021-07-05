from os import system, name
from art import logo
# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


print(logo)
print("Welcome to the silent auction for 'The best painting'")
all_bids = []

def init():
	name = input("What is your name? ")
	bid = int(input("What is your bid? Rs."))
	all_bids.append({
		"name": name,
		"bid": bid
	})

def calculate_highest_bid():
	max_bid = {"name": "", "bid": 0}
	for	x in all_bids:
		if x["bid"] > max_bid["bid"]:
			max_bid = x
	print(f'The maximum bid was Rs.{(max_bid["bid"])} by {max_bid["name"]}')

while True:
	init()
	should_continue = input("Are there more bidders? Type \"yes\" or \"no\": ")
	if should_continue == "yes":
		clear()
	elif should_continue == "no":
		clear()
		calculate_highest_bid()
		break
