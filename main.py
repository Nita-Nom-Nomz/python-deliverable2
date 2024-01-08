print("Welcome to the GC Fruit Market!")
print("What is your name?")
name = input()

# List to track the quantity of each fruit bought
fruit_quantities = [0, 0, 0]

# Fruit prices
fruit_prices = [2, 1, 3]

# If the list changes or new fruits are added, list can be adjusted.
while True:
    # Display the fruit options and get user input for the chosen fruit.
    print(f"Welcome {name}. Which fruit would you like to buy? (Please make selection by number)")
    print("1. Apple $2")
    print("2. Grape $1")
    print("3. Orange $3")

    choice = int(input())

    # Update the quantity of the chosen fruit in the list
    if choice == 1:  # Apple
        fruit_quantities[0] += 1
        print("You bought 1 apple for $2")
        choice = input(f"Would you like to buy another piece of fruit? y/n ")
    elif choice == 2:  # Grape
        fruit_quantities[1] += 1
        print("You bought 1 grape for $1")
        choice = input(f"Would you like to buy another piece of fruit? y/n ")
    elif choice == 3:  # Orange
        fruit_quantities[2] += 1
        print("You bought 1 orange for $3")
        choice = input(f"Would you like to buy another piece of fruit? y/n ")

    if choice == "n":
        break

# Calculates subtotal
subtotal = sum(quantity * price for quantity, price in zip(fruit_quantities, fruit_prices))

# Calculates tax (5%)
tax_rate = 0.05
tax = subtotal * tax_rate

# Calculates the total cost
total = subtotal + tax

# Prints out the receipt/full order
print(f"Complete order for {name}:")
fruits = ['Apple(s)', 'Grape(s)', 'Orange(s)']
for i, quantity in enumerate(fruit_quantities):
    if quantity >= 0:
        print(f"{fruits[i]}: {quantity} at ${fruit_prices[i]} each")

print(f"Subtotal: ${subtotal}")
print(f"Tax (5%): ${tax}")
print(f"Total: ${total}")
