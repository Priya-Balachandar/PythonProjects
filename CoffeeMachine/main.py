MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def process_coins():
    """Prompts user to insert coins and calculates total money inserted."""
    print('Please insert coins.')
    quarter = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    # Calculate total from coins
    total = 0.25 * quarter + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    return total


def check_transaction_successful(money_received, drink_cost):
    """Checks if the user has inserted enough money and processes the transaction."""
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here's your change: ${change}")
    global profit
    profit += drink_cost
    return True


def check_resources(drink):
    """Checks if there are enough resources to make the drink."""
    for ingredient, required in MENU[drink]["ingredients"].items():
        if resources.get(ingredient, 0) < required:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def make_coffee(drink_name):
    """Deducts required ingredients from the resources and serves the drink."""
    for ingredient, required in MENU[drink_name]["ingredients"].items():
        resources[ingredient] -= required
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif user_choice in MENU:
        drink = MENU[user_choice]
        if check_resources(user_choice):
            payment = process_coins()
            if check_transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice)
    else:
        print("Invalid input. Please choose from espresso, latte, or cappuccino.")

