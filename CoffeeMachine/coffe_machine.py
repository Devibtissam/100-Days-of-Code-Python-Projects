
from data import MENU
from data import resources


def is_resources_sufficients(ingredients):
  """Returns True when order can be made, False if ingredients are insufficient."""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print("Sorry there is not enough water.")
            return False
    return True


def process_coins():
  """Returns the total calculated from coins inserted."""
    print("insert how many coins.")
    total_price = int(input("how many quarters? :"))*0.25
    total_price += int(input("how many dimes? :"))*0.1
    total_price += int(input("how many nickels?: "))*0.05
    total_price += int(input("how many pennies?: "))*0.01
    return total_price


def is_transaction_succesful(price, drink_price):
  """Return True when the payment is accepted, or False if money is insufficient."""
    if price > drink_price:
        print(f"Here {round(price - drink_price,2)}$ in change")
        global profit
        profit = drink_price
        return True
    else:
        print("sorry that's not enough money. money refunded")
        return False


profit = 0
is_on = True
while is_on:

    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffe: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficients(drink['ingredients']):
            payment = process_coins()
            if is_transaction_succesful(payment, drink['cost']):
                for item in drink['ingredients']:
                    resources[item] -= drink['ingredients'][item]
                print(f"Here is your {choice} ☕. Enjoy !!")
