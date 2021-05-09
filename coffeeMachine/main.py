
"""     Coffee Machine
    Take user input of what they like to have and give them the required coffee.
    If there are enough ingredients available to make that coffee
"""

# Coffee Menu
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
# Machine resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Initial machine profit
profit = 0


# Check if machine has enough resources
def isResourceSufficient(order_ingredients):
    """Returns True if there are enough resources to process order"""
    for item in order_ingredients:
        # If any ingredient is not available to make the product then return False
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True


def processCoins():
    """Returns the total calculated coins that are inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def isTransactionSuccessful(money_received, drink_cost):
    """Return True if the payment is accepted."""
    if money_received >= drink_cost:
        # Hold the change amount to give user back
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        # Call the global variable profit inside function
        global profit
        # Increase profit by cost of the drink
        profit += drink_cost
        return True
    else:
        print(f"Sorry! Insufficient money inserted. Money refunded...")
        return False


def makeCoffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        # Decrease resources amount by ordered item ingredients
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True

# Machine will run until turn off
while is_on:
    # Ask user to choose between the coffee menu
    choice = input("What would you like??? \n\n\tExpresso\n\n\tLatte\n\n\tCappuccino\n\t>>> ").lower()
    # Turn off the machine if user input off
    if choice == "off":
        is_on = False
    # Provide with report if user input report
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        # drink holds user desired item from menu
        drink = MENU[choice]
        # Call the function to check if machine have enough resources to make user
        # desired item
        if isResourceSufficient(drink["ingredients"]):
            # Calls the function processCoins() to process the inserted coins
            # and returns the total amount and store it in payment
            payment = processCoins()
            # call the function to check if the payment is successful and
            # then machine will start making coffee
            if isTransactionSuccessful(payment, drink["cost"]):
                makeCoffee(choice, drink["ingredients"])

