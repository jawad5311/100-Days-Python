
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# # Print Report
# coffee_object = CoffeeMaker()
# coffee_object.report()
#
# # Create coffee object and check if the resources available
# drink = Menu()
# items = drink.get_items()
# print(items)
# item = drink.find_drink('latte')
#
# check_resource = coffee_object.is_resource_sufficient(item)
# print(check_resource)
#
# # Process coins
# payment = MoneyMachine()
# payment.make_payment(.25)
#
#
# make_latte = CoffeeMaker()
# make_latte.make_coffee(item)


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like: ({options}): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)




