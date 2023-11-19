from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

coffee_machine_on = True
while coffee_machine_on:
    customer_input = input(f"What would you like? {menu.get_items()}: ")
    if customer_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif customer_input == "off":
        coffee_machine_on = False
    else:
        drink = menu.find_drink(customer_input)
        if drink:
            enough_resource = coffee_maker.is_resource_sufficient(drink)
            if enough_resource:
                enough_payment = money_machine.make_payment(drink.cost)
                if enough_payment:
                    coffee_maker.make_coffee(drink)