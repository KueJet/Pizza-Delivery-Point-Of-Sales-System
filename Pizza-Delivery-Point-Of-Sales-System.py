from datetime import date

#Creating dictionary to store ingredients
ingredientList = {
    "flour": 0,
    "mozzarella cheese": 0,
    "pineapple": 0,
    "mushroom": 0,
    "chicken pepperoni": 0
}

#Initializing the sales record
sales_record = [
    {"pizza": "Chicken supreme", "regular": 0, "large": 0},
    {"pizza": "Haiwaiian chicken", "regular": 0, "large": 0},
    {"pizza": "Super supreme", "regular": 0, "large": 0},
    {"pizza": "Chicken pepperoni", "regular": 0, "large": 0},
    {"pizza": "Veggie lover", "regular": 0, "large": 0}
]

#Defining the ingredient usage for each pizza and pizza size.
ingredient_usage = [
    [  #Chicken supreme [regular][large]
        {"flour": 150, "mozzarella cheese": 70, "pineapple": 0, "mushroom": 40, "chicken pepperoni": 80},
        {"flour": 200, "mozzarella cheese": 100, "pineapple": 0, "mushroom": 60, "chicken pepperoni": 120}
    ],
    [  #Haiwaiian chicken [regular][large]
        {"flour": 150, "mozzarella cheese": 70, "pineapple": 50, "mushroom": 0, "chicken pepperoni": 80},
        {"flour": 200, "mozzarella cheese": 100, "pineapple": 80, "mushroom": 0, "chicken pepperoni": 120}
    ],
    [  #Super supreme [regular][large]
        {"flour": 150, "mozzarella cheese": 70, "pineapple": 50, "mushroom": 40, "chicken pepperoni": 80},
        {"flour": 200, "mozzarella cheese": 100, "pineapple": 80, "mushroom": 60, "chicken pepperoni": 120}
    ],
    [  #Chicken pepperoni [regular][large]
        {"flour": 150, "mozzarella cheese": 70, "pineapple": 0, "mushroom": 0, "chicken pepperoni": 80},
        {"flour": 200, "mozzarella cheese": 100, "pineapple": 0, "mushroom": 0, "chicken pepperoni": 120}
    ],
    [  #Veggie lover [regular][large]
        {"flour": 150, "mozzarella cheese": 70, "pineapple": 50, "mushroom": 40, "chicken pepperoni": 0},
        {"flour": 200, "mozzarella cheese": 100, "pineapple": 80, "mushroom": 60, "chicken pepperoni": 0}
    ]
]

#Function to calculate subtotal
def calculate_subtotal(pizza, size, quantity):
    price = {
        "Chicken supreme": [39.3, 52.3],  #Regular and Large prices
        "Haiwaiian chicken": [39.3, 52.3],
        "Super supreme": [42.3, 56.3],
        "Chicken pepperoni": [36.0, 47.9],
        "Veggie lover": [32.0, 45.9]
    }
    price = price[pizza][0] if size == "regular" else price[pizza][1]
    return price * quantity

#Function to display sales
def sales():
    print("Sales: ")
    print("-" * 60)
    print("{:<20} {:<10} {:<15} {:>10}".format("Pizza", "Size", "Quantity sold", "Subtotal"))
    print("-" * 60)
    total_sales = 0
    for pizza in sales_record:
        for size, quantity in pizza.items():
            if size != "pizza" and quantity > 0:
                subtotal = calculate_subtotal(pizza["pizza"], size, quantity)
                total_sales += subtotal
                print("{:<20} {:<10} {:>13} {:>10.2f}".format(pizza["pizza"], size, quantity, subtotal))
    print("-" * 60)
    print("Total: RM {:.2f}".format(total_sales))
    print("=" * 60)

#Function to display ingredient stock
def stock():
    print("Ingredients left:")
    print("-" * 40)
    for ingredient, stock in ingredientList.items():
        print(f"{ingredient.capitalize()}: {stock} grams")
    print("-"*40)

# Function for ordering 
def order():
    # Loop the ordering menu as long as the user wants
    while True:
        # Showing Pizza Menu options to customers
        print("\nPizza Menu")
        print("1. Chicken Supreme")
        print("2. Haiwaiian Chicken")
        print("3. Super Supreme")
        print("4. Chicken Pepperoni")
        print("5. Veggie Lover")
        print("6. Cancel")
        # Taking the order
        try:
            ordering = int(input("Enter your pizza option:"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        match ordering:
            case 1 | 2 | 3 | 4 | 5:
                # Taking the size of the pizza
                print("\nSize of Pizza")
                print("1. Regular")
                print("2. Large")
                print("3. Cancel")
                # Taking the size of the pizza
                try:
                    pizza_size = int(input("What size of pizza do you want? (1 or 2): "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                if pizza_size == 3:
                    break 
                elif pizza_size not in [1, 2]:
                    print("Invalid size choice.")
                    continue 
                try:
                    quantity = int(input("Enter the quantity of pizza: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                if quantity > 0:
                    # Calculate total ingredient usage for the selected pizza size and quantity
                    total_usage = {}
                    for ingredient, usage in ingredient_usage[ordering - 1][pizza_size - 1].items():
                        total_usage[ingredient] = usage * quantity

                    # Check if the available ingredient stock is sufficient
                    ingredients_sufficient = True
                    for ingredient, usage in total_usage.items():
                        if ingredientList[ingredient] < usage:
                            print(f"Insufficient stock for {ingredient.capitalize()}!")
                            ingredients_sufficient = False
                            break

                    if ingredients_sufficient:
                        # Deduct the used ingredients from the stock
                        for ingredient, usage in total_usage.items():
                            ingredientList[ingredient] -= usage

                        pizza = sales_record[ordering - 1]
                        size = "regular" if pizza_size == 1 else "large"
                        pizza[size] += quantity
                        print("Order added successfully!")
                        continueOrder = input("Do you want to continue ordering? (Enter 'no' to stop): ").lower()
                        if continueOrder == "no":
                            totalPrice = sum(calculate_subtotal(pizza["pizza"], size, quantity) for pizza in sales_record for size, quantity in pizza.items() if size != "pizza" and quantity > 0)
                            print("Total is RM {:.2f}".format(totalPrice))
                            break
                    else:
                        print("Order cannot be processed due to insufficient ingredients.")
                else:
                    print("Invalid quantity.")
            case 6:
                break
            case _:
                print("Invalid pizza option.")

#Getting the ingredients for the day
print(f"Day Begins! Enter the amount of stocks for today ({date.today()})")
for ingredient in ingredientList:
    while True:
        stock_input = input(f"Enter stock for {ingredient.capitalize()} in grams: ")
        if stock_input.isdigit() or (stock_input[0] == '-' and stock_input[1:].isdigit()):
            ingredient_stock = float(stock_input)
            if ingredient_stock >= 0:
                ingredientList[ingredient] = ingredient_stock
                break  # Exit the loop if input is valid
            else:
                print("Invalid quantity. Please enter a non-negative number.")
        else:
            print("Invalid input. Please enter a number.")
            
while True:
    print("\nMain Menu:")
    print("1. Order")
    print("2. Check Sales")
    print("3. Check Stock")
    print("4. Closing")
    try:
        action = int(input("Choose your action (1 to 4): "))
        match action:
            case 1:
                order()
            case 2:
                sales()
            case 3:
                stock()
            case 4:
                print("Closing")
                break
            case _:
                print("Invalid selection. Enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")

print("Program ended")