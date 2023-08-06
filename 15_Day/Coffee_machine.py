from machine_data import MENU, resources

profit = 0
is_on = True


def is_resource_sufficient(order_ingredients):
    """Returns True When order can be made and Fals when ingredients is unsefficent"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns the total calculated from coin insurted"""
    print("Please insert coins.")
    total = int(input("How many Quarters?: ")) * 0.25
    total += int(input("How many Dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns true when the payment is acceptred, or false if thge money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from resource"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("Thanks for coming.")
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):    
            payment = process_coins()
            is_transaction_successful(payment, drink["cost"])
            make_coffee(choice, drink["ingredients"])
