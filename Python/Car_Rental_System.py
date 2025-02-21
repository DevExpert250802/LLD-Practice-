# Car Rental Management System
# Dictionary to hold available cars (Car ID: (Car Model, Daily Rent))

car_inventory = {
    201: ("Toyota Camry", 1600),
    202: ("Honda Accord", 2100),
    203: ("Ford Explorer", 3200),
    204: ("BMW X3", 4200),
    205: ("Nissan Altima", 5200),
    206: ("Suzuki Vitara", 7200),
    207: ("Hyundai i20", 8200),
    208: ("Lamborghini Huracan", 9200),
    209: ("Mercedes-Benz E-Class", 10200),
    210: ("Maserati Levante", 11200)
}

rented_vehicles = []
rental_log = {}
user_accounts = {}

def register_user():
    username = input("Enter a username: ").strip().lower()
    if username in user_accounts:
        print("Username already exists! Choose a different one.")
        return False
    password = input("Enter a password: ").strip()
    user_accounts[username] = password
    print("Registration successful! You may now log in.")
    return True

def login_user():
    username = input("Enter your username: ").strip().lower()
    password = input("Enter your password: ").strip()
    if user_accounts.get(username) == password:
        print("Login successful! Welcome, " + username + "!")
        return True
    print("Incorrect username or password. Please try again.")
    return False

def display_available_cars():
    print("\nAvailable Cars:")
    if not car_inventory:
        print("No cars currently available.")
    else:
        for car_id, (model, rent) in car_inventory.items():
            print("Car ID: " + str(car_id) + ", Model: " + model + ", Rent per day: ₹" + str(rent) + "/day")

def rent_vehicle():
    if not car_inventory:
        print("No cars available for rent.")
        return

    car_id_input = input("Enter the Car ID you wish to rent: ").strip()
    if not car_id_input.isdigit():
        print("Invalid input! Enter a valid Car ID.")
        return

    car_id = int(car_id_input)
    if car_id not in car_inventory:
        print("Invalid Car ID! Choose from available options.")
        return

    client_name = input("Enter your name: ").strip().lower()
    rental_days_input = input("Enter rental period (in days): ").strip()
    if not rental_days_input.isdigit():
        print("Invalid input! Enter a valid number of days.")
        return

    rental_days = int(rental_days_input)
    if rental_days <= 0:
        print("Rental period must be at least 1 day.")
        return

    car_details = car_inventory.pop(car_id)
    total_cost = car_details[1] * rental_days
    rented_vehicles.append((client_name, car_id, car_details[0], rental_days, total_cost))
    rental_log.setdefault(client_name, []).append((car_id, rental_days, total_cost))
    print("Car rented successfully! Total cost: ₹" + str(total_cost))

def display_rented_vehicles():
    print("\nRented Cars:")
    if not rented_vehicles:
        print("No cars are currently rented.")
    else:
        for record in rented_vehicles:
            print("Client Name: " + record[0] + ", Car ID: " + str(record[1]) + ", Model: " + record[2] + ", Days: " + str(record[3]) + ", Total Price: ₹" + str(record[4]))

def return_vehicle():
    if not rented_vehicles:
        print("No cars are currently rented.")
        return

    client_name = input("Enter your name: ").strip().lower()
    car_id_input = input("Enter the Car ID to return: ").strip()
    if not car_id_input.isdigit():
        print("Invalid input! Enter a valid Car ID.")
        return

    car_id = int(car_id_input)
    rental_entry = None

    for record in rented_vehicles:
        if record[0] == client_name and record[1] == car_id:
            rental_entry = record
            break

    if rental_entry:
        rented_vehicles.remove(rental_entry)
        car_inventory[car_id] = (rental_entry[2], rental_entry[4] // rental_entry[3])
        print("Car ID " + str(car_id) + " returned successfully!")
    else:
        print("No matching rental record found.")

def display_rental_log():
    print("\nRental History:")
    if not rental_log:
        print("No rental history found.")
    else:
        for client, records in rental_log.items():
            print("\nClient: " + client.capitalize())
            for record in records:
                print("Car ID: " + str(record[0]) + ", Days: " + str(record[1]) + ", Cost: ₹" + str(record[2]))

def main():
    while True:
        print("\nWelcome to Car Rental Management System!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            if login_user():
                while True:
                    print("\nCar Rental Menu:")
                    print("1. View Available Cars")
                    print("2. Rent a Car")
                    print("3. View Rented Cars")
                    print("4. Return a Car")
                    print("5. View Rental History")
                    print("6. Logout")

                    menu_choice = input("Enter your choice (1-6): ").strip()

                    if menu_choice == "1":
                        display_available_cars()
                    elif menu_choice == "2":
                        rent_vehicle()
                    elif menu_choice == "3":
                        display_rented_vehicles()
                    elif menu_choice == "4":
                        return_vehicle()
                    elif menu_choice == "5":
                        display_rental_log()
                    elif menu_choice == "6":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice! Enter a number between 1 and 6.")
        elif choice == "3":
            print("Thank you for using the Car Rental Management System!")
            break
        else:
            print("Invalid choice! Enter a number between 1 and 3.")

main()
