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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def show_status():
    print("water:", resources['water'])
    print("milk:", resources['milk'])
    print("coffee:", resources['coffee'])


def check_resources_latte():
    ok_resource_latte = False
    if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
        ok_resource_latte = True
    return ok_resource_latte


def check_resources_espresso():
    ok_resource_espresso = False
    if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
        ok_resource_espresso = True
    return ok_resource_espresso


def check_resources_cappuccino():
    ok_resource_cappuccino = False
    if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
        ok_resource_cappuccino = True
    return ok_resource_cappuccino


def dispense_latte(coins):
    # TODO: 3.Check resources sufficient?
    # TODO: 5.Check transaction successful?
    if coins == MENU["latte"]["cost"] and check_resources_latte():
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        print("Here is your latte ☕. Enjoy!")
    elif coins > MENU["latte"]["cost"]:
        extra = coins - MENU["latte"]["cost"]
        print(f"Here is ${extra} in change.")
    else:
        print("Sorry that's not enough money. Money refunded.")


def dispense_espresso(coins):
    if coins == MENU["espresso"]["cost"] and check_resources_espresso():
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        print("Here is your espresso ☕. Enjoy!")
    elif coins > MENU["espresso"]["cost"]:
        extra = coins - MENU["espresso"]["cost"]
        print(f"Here is ${extra} in change.")
    else:
        print("Sorry that's not enough money. Money refunded.")


def dispense_cappuccino(coins):
    if coins == MENU["cappuccino"]["cost"] and check_resources_cappuccino():
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        print("Here is your cappuccino ☕. Enjoy!")
    elif coins > MENU["cappuccino"]["cost"]:
        extra = coins - MENU["cappuccino"]["cost"]
        print(f"Here is ${extra} in change.")
    else:
        print("Sorry that's not enough money. Money refunded.")


# TODO: 4.Process coins
def take_coins():
    print('Please insert coins.')
    quarters = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickles = int(input("how many nickles?:"))
    pennies = int(input("how many pennies?:"))
    cost = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    print(f'cost is = {round(cost, 2)}')
    return round(cost, 2)


# TODO: 1.Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

while True:
    ask = input("What would you like? (espresso/latte/cappuccino):")

    # TODO: 2.Print report
    if ask.lower() == 'report':
        show_status()
        # TODO: 6.Make Coffee.
    elif ask.lower() == 'latte':
        coin = take_coins()
        dispense_latte(coin)
    elif ask.lower() == 'espresso':
        coin = take_coins()
        dispense_espresso(coin)
    elif ask.lower() == 'cappuccino':
        coin = take_coins()
        dispense_cappuccino(coin)
    else:
        print('Please enter a choice shown above !')

