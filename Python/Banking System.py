#   Banking System
print("Welcome to Secure Bank")

registered_user = "DevX"
registered_pass = "789"

user_name = input("Enter your username: ")
user_pass = input("Enter your password: ")

if user_name == registered_user and user_pass == registered_pass: 
    print("Login successful! Welcome to Secure Bank.")

    account_balance = 0
    print("Your account has been created. Initial balance: ₹0.")

    while True:
        print("\nChoose an action:")
        print("1. Deposit Funds")
        print("2. Withdraw Funds")
        print("3. View Balance")
        print("4. Transfer Funds")
        print("5. Logout")

        user_choice = input("Enter your choice (1-5): ")

        if user_choice == "1":
            deposit_amount = float(input("Enter deposit amount: "))
            account_balance += deposit_amount
            print(f"Deposit successful! New balance: ₹{account_balance}")

        elif user_choice == "2":
            withdraw_amount = float(input("Enter withdrawal amount: "))
            if withdraw_amount <= account_balance:
                account_balance -= withdraw_amount
                print(f"Withdrawal successful! New balance: ₹{account_balance}")
            else:
                print("Insufficient funds.")

        elif user_choice == "3":
            print(f"Your current balance is: ₹{account_balance}")

        elif user_choice == "4":
            recipient_account = input("Enter recipient account number: ")
            transfer_amount = float(input("Enter amount to transfer: "))
            if transfer_amount <= account_balance:
                account_balance -= transfer_amount
                print(f"Transfer successful! ₹{transfer_amount} sent to account {recipient_account}. New balance: ₹{account_balance}")
            else:
                print("Insufficient balance for transfer.")

        elif user_choice == "5":
            print("Thank you for banking with us. Have a great day!")
            break
else:
    print("Invalid credentials. Access denied.")
