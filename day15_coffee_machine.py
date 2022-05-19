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
    "money": 0,
}


def format_resources():
    """returns the formatted message of current resources status"""
    message = f'''
Water: {resources["water"]} ml
Milk: {resources["milk"]} ml
Coffee: {resources["coffee"]} g
Money: ${resources["money"]} 
'''
    return message


def check_resources(drink_name):
    for item in resources:
        if item in MENU[drink_name]["ingredients"]:
            if MENU[drink_name]["ingredients"][item] > resources[item]:
                print(f"There's not enough {item}. Sorry!")
                global transaction_on
                transaction_on = False


def money_collect():
    """ Asks the user for number of inserted coins, returns a dictionary with number of coins """
    print("Please insert coins.")
    quarters_amount = int(input("How many quarters?: "))
    dimes_amount = int(input("How many dimes?: "))
    nickles_amount = int(input("How many nickles?: "))
    pennies_amount = int(input("How many pennies?: "))
    amount_of_each_coin = {
        "quarters": quarters_amount,
        "dimes": dimes_amount,
        "nickles": nickles_amount,
        "pennies": pennies_amount,
    }
    return amount_of_each_coin


def total_coins_value(dict_with_number_of_coins):
    """ Counts the total sum of inserted money (and returns it as output).
    Requires a dictionary with information of how many coins of each type were inserted."""
    coins_value = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01,
     }
    total_sum = 0
    for coin_type in coins_value:
        total_sum += coins_value[coin_type] * dict_with_number_of_coins[f"{coin_type}"]
    return total_sum


def check_the_money(drink_name, total_sum):
    """ checks if the amount of money that user entered is OK. If it's not enough,
    it cancels transaction (returns False), if it's too much, it counts the change for the user. """
    drink_cost = MENU[drink_name]["cost"]
    if drink_cost > total_sum:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif drink_cost == total_sum:
        resources["money"] += total_sum
        return True
    elif drink_cost < total_sum:
        change = round(total_sum - drink_cost, 2)
        print(f"Here is ${change} in change")
        return True


def update_resources(drink_name):
    """ Updates the amount of resources left in coffee machine, after making a coffee"""
    for item in resources:
        if item in MENU[drink_name]["ingredients"]:
            resources[item] -= MENU[drink_name]["ingredients"][item]
        if item == "money":
            resources[item] += MENU[drink_name]["cost"]


coffee_machine_on = True

while coffee_machine_on:
    transaction_on = True
    users_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if users_choice == "off":
        coffee_machine_on = False
    elif users_choice == "report":
        print(format_resources())
        transaction_on = False
    elif users_choice == "espresso" or users_choice == "latte" or users_choice == "cappuccino":
        check_resources(users_choice)
    else:
        transaction_on = False
        print("Invalid input. Try again.")
    if transaction_on and coffee_machine_on:
        total_money = total_coins_value(money_collect())
        if check_the_money(users_choice, total_money):
            update_resources(users_choice)
            print(f"Here is your {users_choice}. Enjoy!")
