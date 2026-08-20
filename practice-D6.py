# Food menu
print("---  welcome to our restaurant  ---")
print("        *** FOOD MENU ***")

print("* FAST FOOD")
print("1. Sandwich      : 2.5$")
print("2. Burger        : 3$")
print("3. French Fries  : 2$")

print("* Salads")
print("1. Chicken Salad : 4$")
print("2. Shrimp Salad  : 5$")
print("3. Tuna Salad    : 5.5$")

print("* DRINKS")
print("1. Water         : 1$")
print("2. Coca Cola     : 1.5$")
print("3. Coffee        : 2$")

print("-"*35)

while True:
    order_food = input("Choose Menu: ")
    match order_food:
        case ("fast food"):
            print("1. Sandwich      : 2.5$")
            print("2. Burger        : 3$")
            print("3. French Fries  : 2$")
            fast_food = input("Order fast food: ")
    
        case ("salad"):
            print("1. Chicken Salad : 4$")
            print("2. Shrimp Salad  : 5$")
            print("3. Tuna Salad    : 5.5$")

        case ("drinks"):
            print("1. Water         : 1$")
            print("2. Coca Cola     : 1.5$")
            print("3. Coffee        : 2$")
            drinks = input("Order drink: ")
        case _:
            print("item isn't available")
