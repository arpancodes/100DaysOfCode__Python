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

def add(n1, n2):
	return n1 + n2

def subtract(n1, n2):
	return n1 - n2

def multiply(n1, n2):
	return n1 * n2

def divide(n1, n2):
	return n1 / n2

operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide
}

def calculator():
	clear()
	print(logo)
	num1 = float(input("Enter the first number: "))
	should_continue = True

	while should_continue:
		for operator in operations:
			print(operator)
		operation_chosen = input("Select an operation from above: ")
		num2 = float(input("Pick the next number: "))
		answer = operations[operation_chosen](num1, num2)
		print(f"{num1} {operation_chosen} {num2} = {answer}")
		if input(f"Enter 'y' to continue with {answer}, or enter 'n' to start a new calculation: ") == "y":
			num1 = answer
		else:
			should_continue = False
			calculator()

calculator()
