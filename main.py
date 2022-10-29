from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:

    print(f"Options: {menu.get_items()}")
    entry = input("Enter your choice:")

    if entry.lower() == "report":
        coffee_maker.report()
    elif entry.lower() == "shutdown":
        break
    elif entry.lower() == "profit":
        money_machine.report()
    elif not menu.find_drink(entry) is None:
        drink = menu.find_drink(entry)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


