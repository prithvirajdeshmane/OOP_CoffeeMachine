# Import classes needed
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# instantiate objects
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
menu_items = menu.get_items()

# set bool to track if machine is on or off
is_machine_on = True

while is_machine_on:
    # get user's choice of operation or drink
    choice = input(f"What would you like? {menu_items}: ").lower()

    # switch the machine off
    if choice == "off":
        is_machine_on = False
        print("Goodbye!")
        continue

    # get a report of resources available in the machine, as well as profit made
    if choice == "report":
        coffee_machine.report()
        money_machine.report()
        continue

    # confirm if drink entered by user exists on the menu
    drink = menu.find_drink(choice)
    if drink is None:
        continue

    # confirm whether the machine has enough resources to make user's drink
    if not coffee_machine.is_resource_sufficient(drink):
        continue

    # process payment, check if payment is sufficient or not, and how much change is due
    if not money_machine.make_payment(drink.cost):
        continue

    # dispense the user's drink
    coffee_machine.make_coffee(drink)
