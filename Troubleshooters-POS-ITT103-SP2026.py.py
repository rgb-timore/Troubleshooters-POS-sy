#Troubleshooter POS system

# Product categories and prices
categories = {
    "Clothing": {
        "Adidas shoes": 10.00,
        "Polo shirt": 6.50,
        "Polo Jeans": 7.50,
        "Hanes shirt": 8.50,
        "Hanes Jeans": 9.50
    },
    "Electronics": {
        "PlayStation 4": 100.00,
        "PlayStation 5": 200.00,
        "Xbox 1": 300.00,
        "Asus Gaming PC": 500.00
    },
    "Beauty": {
        "Avon deodorant": 1.00,
        "Arm & Hammer": 2.00,
        "Avon lotion": 2.00
    }
}

# Inventory (stock levels)
inventory = {
    "Adidas shoes": 10,
    "Polo shirt": 0,
    "Polo Jeans": 12,
    "Hanes shirt": 40,
    "Hanes Jeans": 0,
    "PlayStation 4": 13,
    "PlayStation 5": 10,
    "Xbox 1": 9,
    "Asus Gaming PC": 2,
    "Avon deodorant": 19,
    "Arm & Hammer": 20,
    "Avon lotion": 15
}

# Menu list (used to map numbers to items)
menu = []

# Cart dictionary (item -> quantity)
cart = {}

#  display the item selected as the user inputs them and is used for the final reciept
def display_cart(cart, menu):
    print()
    print("====== CART ======")

    subtotal = 0
    total_items = 0

    # Loop through cart items
    for item_name, qty in cart.items():

        # Find price from menu
        price = next(price for item, price in menu if item == item_name)

        line_total = price * qty
        subtotal += line_total
        total_items += qty

        print(f"{item_name:20} x{qty} = ${line_total:.2f}")


    # Discount application
    # Every 3 items = 5% discount
    discount_blocks = total_items // 3
    discount_rate = discount_blocks * 0.05
    discount_amount = subtotal * discount_rate

    #
    discount_total = subtotal - discount_amount

    #total before tax is applied
    tax = 0.10
    tax_amount = discount_total * tax

    #final calculation
    final_total = discount_total + tax_amount

    print("--------------------------------------")
    print(f"Items: {total_items}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount_amount:.2f} ({discount_rate*100:.0f}%)")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${final_total:.2f}")
    print("=============================================")

    return final_total

def print_receipt(cart, menu, final_total, amount_receive):
    print("=============================================")
    print("---------------WALMART RECEIPT---------------")
    print("=============================================")

    subtotal = 0
    total_items = 0

    # Print items
    for item_name, qty in cart.items():
        price = next(price for item, price in menu if item == item_name)
        line_total = price * qty

        subtotal += line_total
        total_items += qty

        print(f"{item_name:20} x{qty}  ${line_total:.2f}")

    # Discount
    discount_blocks = total_items // 3
    discount_rate = discount_blocks * 0.05
    discount_amount = subtotal * discount_rate

    discounted_total = subtotal - discount_amount

    # Tax
    tax = 0.10
    tax_amount = discounted_total * tax

    change = amount_receive - final_total

    print("=============================================")
    print(f"Items: {total_items}")
    print(f"Subtotal:        ${subtotal:.2f}")
    print(f"Discount:       -${discount_amount:.2f}")
    print(f"Tax (10%):      +${tax_amount:.2f}")
    print("=============================================")
    print(f"TOTAL:           ${final_total:.2f}")
    print(f"Cash:            ${amount_receive:.2f}")
    print(f"Change:          ${change:.2f}")
    print("=============================================")
    print("   Thank you for shopping!")
    print("=============================================")

print("-----------------------------------------")
print("Welcome to Walmart POS system")
print("-----------------------------------------")

item_number = 1

# Build menu and display items
for category, items in categories.items():
    print()
    print(f"************ {category} ************")

    for item, price in items.items():
        menu.append((item, price))  # store item + price
        print(f"{item_number}\t{item:20}: ${price:.2f}")
        item_number += 1

print("-----------------------------------------")

while True:

    # Ask user what they want to do
    action = input("Select product number, (r) remove item, (q) checkout: ").lower()

    # checkout items
    if action == "q":
        break
    # removes items
    if action == "r":
        num = input("Enter item number to remove: ")

        if num.isdigit():
            index = int(num) - 1

            # Check if valid index
            if 0 <= index < len(menu):
                item_name, price = menu[index]

                # Check if item is in cart
                if item_name in cart:
                    cart[item_name] -= 1          # reduce quantity
                    inventory[item_name] += 1     # return to stock

                    # Remove item completely if quantity is 0
                    if cart[item_name] == 0:
                        del cart[item_name]

                    print(f"Removed one {item_name}")
                    display_cart(cart, menu)
                else:
                    print("Item not in cart")
            else:
                print("Invalid number")
        else:
            print("Enter a valid number")

        continue

#add item to cart
    if action.isdigit():
        index = int(action) - 1

        # Check valid selection
        if 0 <= index < len(menu):
            item_name, price = menu[index]

            # Check stock availability
            if inventory[item_name] > 0:

                # Add to cart or increase quantity
                if item_name in cart:
                    cart[item_name] += 1
                else:
                    cart[item_name] = 1

                inventory[item_name] -= 1  # reduce stock

                print(f"Added {item_name} (${price:.2f}) | Remaining: {inventory[item_name]}")

                # Show updated cart
                display_cart(cart, menu)

            else:
                print(f"{item_name}'s are out of stock")
        else:
            print("Invalid selection")

    else:
        print("Please enter a valid option")
print()
print("Your Receipt:") # by using the function we can print the final output
final_total = display_cart(cart, menu)

#accepts payments and calculate change
while True:
    try:
        amount_receive = float(input("Amount received: "))
        if amount_receive < final_total:
            print("Insufficient funds")
        else:
            change = amount_receive - final_total

            print(f"Amount received: ${amount_receive:.2f}")
            print(f"Your change: ${change:.2f}")
            print("Thank you for you business")
            print("Transaction complete.")

            # Print receipt function
            print_receipt(cart, menu, final_total, amount_receive)
            break

    except ValueError:
        print("Invalid input")

