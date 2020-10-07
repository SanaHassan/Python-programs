pizza_toppings=["cheese","Peperoni","Chicken Chunks"]


def format_topping(topping):
        if topping == "cheese":
            return f"{topping.title()} (Free)"
        elif topping == "Chicken Chunks":
            return f"{topping.title()} ($2.00)"
        else:
            return f"{topping.title()} ($1.00)"


def pizza_menu(toppings):
    print("------------------------Welcome t our Pizzeria-------------------------------")
    print("HERE IS OUR AVAILABLE TOPPINGS:")
    for topping in toppings:
        print(format_topping(topping))

pizza_menu(pizza_toppings)
