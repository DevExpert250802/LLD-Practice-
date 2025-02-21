# Grocery Store Billing System

users = {}  
user_cart = {}  
logged_in_user = None  

item_price = {
    "Apple": 50, "Banana": 20, "Milk": 30, "Bread": 40, "Eggs": 60, "Rice": 80, "Sugar": 45
}

def signup():
    global users
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists. Try logging in.")
        return
    password = input("Enter a password: ")
    users[username] = password
    user_cart[username] = {}  
    print("Signup successful! You can now log in.")

def login():
    global logged_in_user
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in users and users[username] == password:
        logged_in_user = username
        print("Welcome, " + username + "! You are now logged in.")
    else:
        print("Invalid credentials. Try again.")

def logout():
    global logged_in_user
    if logged_in_user:
        print("Goodbye, " + logged_in_user + "! You have been logged out.")
        logged_in_user = None
    else:
        print("You are not logged in.")

def display_items():
    print("\nAvailable Items:")
    for item, price in item_price.items():
        print(item + " - ₹" + str(price))

def add_to_cart():
    if not logged_in_user:
        print("Please log in first.")
        return
    display_items()
    item = input("Enter item name: ").title()
    if item in item_price:
        try:
            quantity = int(input("Enter quantity of " + item + ": "))
            if quantity > 0:
                user_cart[logged_in_user][item] = user_cart[logged_in_user].get(item, 0) + quantity
                print(str(quantity) + " " + item + "(s) added to cart.")
            else:
                print("Quantity must be at least 1.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Item not available.")

def remove_from_cart():
    if not logged_in_user:
        print("Please log in first.")
        return
    item = input("Enter item name to remove: ").title()
    if item in user_cart[logged_in_user]:
        try:
            quantity = int(input("Enter quantity to remove from " + item + ": "))
            if 0 < quantity <= user_cart[logged_in_user][item]:
                user_cart[logged_in_user][item] -= quantity
                if user_cart[logged_in_user][item] == 0:
                    del user_cart[logged_in_user][item]
                print(str(quantity) + " " + item + "(s) removed from cart.")
            else:
                print("Invalid quantity.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Item not found in cart.")

def view_cart():
    if not logged_in_user:
        print("Please log in first.")
        return
    cart = user_cart[logged_in_user]
    if not cart:
        print("Your cart is empty.")
    else:
        print("\nYour Cart:")
        for item, quantity in cart.items():
            print(item + ": " + str(quantity) + " x ₹" + str(item_price[item]) + " = ₹" + str(quantity * item_price[item]))

def total_bill():
    if not logged_in_user:
        print("Please log in first.")
        return
    total = sum(item_price[item] * quantity for item, quantity in user_cart[logged_in_user].items())
    print("Total bill: ₹" + str(total))

def apply_discount():
    if not logged_in_user:
        print("Please log in first.")
        return
    total = sum(item_price[item] * quantity for item, quantity in user_cart[logged_in_user].items())
    discount_code = input("Enter discount code (SAVE10 for 10% off, FIRST50 for ₹50 off): ")

    discount = 0
    if discount_code == "SAVE10":
        discount = total * 0.10
    elif discount_code == "FIRST50" and total >= 200:
        discount = 50  

    final_amount = max(total - discount, 0)
    print("Discount applied: ₹" + str(discount))
    print("Final bill after discount: ₹" + str(final_amount))

while True:
    print("\n1. Signup")
    print("2. Login")
    print("3. Logout")
    print("4. View available items")
    print("5. Add item to cart")
    print("6. Remove item from cart")
    print("7. View cart")
    print("8. View total bill")
    print("9. Apply discount")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        logout()
    elif choice == "4":
        display_items()
    elif choice == "5":
        add_to_cart()
    elif choice == "6":
        remove_from_cart()
    elif choice == "7":
        view_cart()
    elif choice == "8":
        total_bill()
    elif choice == "9":
        apply_discount()
    elif choice == "10":
        print("Thank you for visiting! Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
