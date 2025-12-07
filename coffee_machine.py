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
        "milk": 0,
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
logo = """
                                    
   (         (     (                
   )\\        )\\ )  )\\ )    (    (   
 (((_)   (  (()/( (()/(   ))\\  ))\\  
 )\\___   )\\  /(_)) /(_)) /((_)/((_) 
((/ __| ((_)(_) _|(_) _|(_)) (_))   
 | (__ / _ \\ |  _| |  _|/ -_)/ -_)  
  \\___|\\___/ |_|   |_|  \\___|\\___|  
                                    
"""

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
    global resourses, NEEDS
    """Asks the user for money for the coffee. Adds profit. Returns if transaction is successfull"""
    print(f"Your coffee costs: ${NEEDS[coffee_type]['cost']}")
    try:
        quarters = int(input("How much quarters? "))
        dimes = int(input("How much dimes? "))
        nickels = int(input("How much nickles? "))
        pennies = int(input("How much pennies? "))
    except:
        print("Wrong input. Try again.")
    
    sum = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    print(f"Your Total: ${sum}.")
    if sum == NEEDS[coffee_type]["cost"]:
        resourses["money"] += sum
        return True
    elif sum > NEEDS[coffee_type]["cost"]:
        change = sum - NEEDS[coffee_type]["cost"]
        resourses["money"] += NEEDS[coffee_type]["cost"]
        print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(coffee_type):
    """Deduces resources and calls in additional checks: money, resource need"""
    global resourses, NEEDS
    if resource_check(coffee_type):
        if money_check(coffee_type):
            for key in resourses:
                if key == "money":
                    continue
                else:
                    resourses[key] -= NEEDS[coffee_type][key]
            print(f"Here is your {coffee_type}.")
        else:
            return
    else:
        return

def main():
    global logo
    cont = True
    while cont:
        print(logo)
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