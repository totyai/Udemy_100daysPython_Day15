resourses = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
},

def report():
    pass

def espresso():
    pass

def latte():
    pass

def cappuccino():
    pass

def main():
    cont = True
    while cont:
        action = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if action == "off":
            cont = False
            print("The machine turns off.")
        elif action == "report":
            print(report())
        elif action == "espresso":
            print(espresso())
        elif action == "latte":
            print(latte())
        elif action == "cappuccino":
            print(cappuccino())
        else:
            print("Wrong input. Please try again.")

if __name__ == "__main__":
    main()