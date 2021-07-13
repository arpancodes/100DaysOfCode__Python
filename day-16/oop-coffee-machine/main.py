from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_machine = CoffeeMaker()
money_maker = MoneyMachine()

while True:
    order = input(f"What would you like to have {coffee_menu.get_items()}\b: ").lower()
    if order == "report":
        coffee_machine.report()
        money_maker.report()
    elif order == "off":
        break
    else:
        item = coffee_menu.find_drink(order)
        if item:
            if coffee_machine.is_resource_sufficient(item):
                if money_maker.make_payment(item.cost):
                    coffee_machine.make_coffee(item)
                else:
                    print("Insufficient amount, money returned.")



