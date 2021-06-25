print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? Rs. "))
total_people = int(input("How many people to split the bill? "))
tip_percent = int(input("What percent til would you like to give? 10, 12 or 15? "))
each_amount = (total_bill + (total_bill * (tip_percent/100))) / total_people
print(f"Each person should pay: {each_amount}")
