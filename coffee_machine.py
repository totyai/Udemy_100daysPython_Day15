resourses = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0,
}
NEEDS = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "cost": 1.50
    },
    "latte": {
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "cost": 2.50
    },
    "cappuccino": {
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "cost": 3.00
    }
}

def report():
    """Returns a string with the resources available"""
    global resourses
    return f"Water: {resourses['water']}ml\nMilk: {resourses['milk']}ml\nCoffee: {resourses['coffee']}g\nMoney: ${resourses['money']}"

def resource_check(coffee_type):
    """Returns a booleen if the resourses are sufficient"""
    global NEEDS, resourses
    for key in resourses:
        if key == "money":
            continue
        elif NEEDS[coffee_type][key] <= resourses[key]:
            continue
        else:
            print(f"Sorry there is not enough {key}")
            return False
    return True

def money_check(coffee_type):
    print(f"Your coffee costs: ")
    quarters = input("How much quarters? ")
    dimes = input("How much dimes? ")
    nickels = input("How much nickles? ")
    pennies = input("How much pennies? ")

def make_coffee(coffee_type):
    if resource_check(coffee_type):
        if money_check(coffee_type):
            pass
        else:
            pass
    else:
        return

def main():
    cont = True
    while cont:
        action = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if action == "off":
            cont = False
            print("The machine turns off.")
        elif action == "report":
            print(report())
        elif action in NEEDS:
            make_coffee(action)
        else:
            print("Wrong input. Please try again.")

if __name__ == "__main__":
    main()