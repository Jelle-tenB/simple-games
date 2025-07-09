from main import MENU, resources

MONEY = 0


def payment(choice):
    print("How many of each coin (quarter, dime, nickle, penny) are you paying with?")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    pay = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    pay = round(pay, 2)
    if pay < MENU[choice]["cost"]:
        print("Not enough payment. Your money has been refunded.")
        question()
    else:
        global MONEY
        change = pay - MENU[choice]["cost"]
        print(f"Your change is: $ {change}")
        MONEY += MENU[choice]["cost"]


def report():
    for key, value in resources.items():
        if key == "coffee":
            print(f"{key}: {value}g")
        else:
            print(f"{key}: {value}ml")
    print(f"money: ${MONEY}")


def question():
    costumer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if costumer == "espresso" or costumer == "latte" or costumer == "cappuccino":
        payment(costumer)
        return costumer
    elif costumer == "off":
        resources["water"] = 300
        resources["coffee"] = 100
        resources["milk"] = 200
        global MONEY
        MONEY = 0
        exit()
    elif costumer == "report":
        report()
        question()
    else:
        print("Please enter valid command")
        question()


costumer_choice = question()
if costumer_choice not in ["off", "report"]:
    coffee = MENU[costumer_choice]["ingredients"]
    if coffee["water"] > resources["water"]:
        print("not enough water")
    elif coffee["coffee"] > resources["coffee"]:
        print("not enough coffee")
    elif "milk" in coffee and coffee["milk"] > resources["milk"]:
        print("not enough milk")
    else:
        resources["water"] -= coffee["water"]
        resources["coffee"] -= coffee["coffee"]
        if "milk" in coffee:
            resources["milk"] -= coffee["milk"]
        print(f"Enjoy your {costumer_choice}")
        question()


# TODO ask users for espresso/latte/cappuccino
# TODO turn the machine "off"
# TODO print report
# TODO check resources
# TODO process coins
# TODO check if transaction successful
# TODO make coffee