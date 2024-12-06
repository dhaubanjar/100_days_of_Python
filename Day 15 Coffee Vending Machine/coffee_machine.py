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
    "water": 600,
    "milk": 700,
    "coffee": 100,
}

def calculate_coins():
    """ Returns the total amount of money inserted."""
    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    pennie = 0.01

    quarters, dimes, nickels, pennies = 0, 0, 0, 0
    try:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
    except ValueError:
        print("Please enter a valid number only.")
        return calculate_coins()            # calls same function to re-prompt for input

    total_money = ((quarter * quarters) + (dime * dimes) + (nickel * nickels) + (pennie * pennies))
    return round(total_money, 2)


def make_coffee(drink_name, order_ingredients):
    """ Deduct the required ingredients from the resources after making a coffee"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


def check_resources(order_ingredients):
    global profit                                           # sets profit variable as global inside the function
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:      # checks if values in resources are enough or not.
            print(f"Sorry there is not enough {item} for {choice}")
            return False                                    # if not enough, end the loop.

        print("Please insert the coins.")
        total_money = calculate_coins()                 # calls calculate_coins() function and return total money.
        coffee_cost = drink["cost"]                     # retrieves cost of a coffee from dictionary.

        if total_money >= coffee_cost:
            profit += coffee_cost                       # stores profit after serving a coffee.
            refund = round((total_money - coffee_cost), 2)      # calculates change to return

            print(f"You gave us ${total_money} for your {choice}")
            print(f"The cost of your {choice} is ${coffee_cost}")
            if refund > 0:
                print(f"Here is your ${refund} dollars in change.")
            make_coffee(choice, order_ingredients)            # calls make_coffee() function to deduct resources.
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False



is_turn = True
while is_turn:
    """ while loop used to break the loop when choice = off """
    try:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            is_turn = False
        elif choice == "report":
            a = resources.get("water")
            b = resources.get("milk")
            c = resources.get("coffee")
            d = profit
            print(f"Water: {a}\nMilk: {b}\nCoffee: {c}\nProfit: {d}")
        elif choice in MENU:
            drink = MENU[choice]  # selects element from the dictionary equals to the input
            check_resources(drink["ingredients"])  # calls check_resources() function
        else:
            print("Invalid option. Please choose 'espresso/latte/cappuccino'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("\n" * 10)






























