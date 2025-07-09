from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
coffeemaker = CoffeeMaker()
money = MoneyMachine()


def start():
    costumer_choice = input(f"What would you like? ({my_menu.get_items()}): ").lower()
    if costumer_choice != "off" and costumer_choice != "report":
        if my_menu.find_drink(costumer_choice) is None:
            start()
        else:
            chosen_item = my_menu.find_drink(costumer_choice)
            if coffeemaker.is_resource_sufficient(chosen_item) is True:
                if money.make_payment(chosen_item.cost) is True:
                    coffeemaker.make_coffee(chosen_item)
                    start()
                else:
                    start()
            else:
                start()
    elif costumer_choice == "off":
        exit
    elif costumer_choice == "report":
        coffeemaker.report()
        money.report()
        start()


start()
