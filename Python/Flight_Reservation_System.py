# Flight Reservation System

users = {}  # Stores registered users (username -> password)
flights = [
    {"Flight No": "AI101", "Destination": "New York", "Price": 500},
    {"Flight No": "BA202", "Destination": "London", "Price": 450},
    {"Flight No": "QR303", "Destination": "Doha", "Price": 400},
    {"Flight No": "EK404", "Destination": "Dubai", "Price": 350}
]
bookings = {}  # Stores user bookings
logged_in_user = None  # Tracks logged-in user


def signup():
    global users
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists! Try a different one.")
        return
    password = input("Enter a password: ")
    users[username] = password
    bookings[username] = []
    print("Signup successful! Please log in.")


def signin():
    global logged_in_user
    if logged_in_user:
        print("You are already logged in as " + logged_in_user)
        return

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        logged_in_user = username
        print("Login successful! Welcome, " + username)
    else:
        print("Invalid username or password.")


def signout():
    global logged_in_user
    if logged_in_user:
        print("Logged out successfully!")
        logged_in_user = None
    else:
        print("You are not logged in.")


def search_flights():
    print("\nAvailable Flights:")
    for flight in flights:
        print(flight["Flight No"] + " - Destination: " + flight["Destination"] + " - Price: ₹" + str(flight["Price"]))


def book_ticket():
    if not logged_in_user:
        print("Please sign in first!")
        return

    search_flights()
    flight_no = input("Enter Flight No to book: ")

    for flight in flights:
        if flight["Flight No"] == flight_no:
            bookings[logged_in_user].append(flight)
            print("Ticket booked for " + flight["Destination"] + ", Flight No: " + flight_no)
            return

    print("Invalid Flight No")


def cancel_booking():
    if not logged_in_user:
        print("Please sign in first!")
        return

    if not bookings[logged_in_user]:
        print("No bookings found")
        return

    print("\nYour Bookings:")
    for flight in bookings[logged_in_user]:
        print("- " + flight["Flight No"] + " Destination: " + flight["Destination"])

    flight_no = input("Enter Flight No to cancel: ")

    for flight in bookings[logged_in_user]:
        if flight["Flight No"] == flight_no:
            bookings[logged_in_user].remove(flight)
            print("Booking cancelled for Flight No: " + flight_no)
            return

    print("Flight No not found in your bookings")


def filter_flights_by_price():
    max_price = int(input("Enter maximum price: "))
    filtered_flights = [flight for flight in flights if flight["Price"] <= max_price]

    if not filtered_flights:
        print("No flights available within the specified price range")
    else:
        print("\nFlights within price range:")
        for flight in filtered_flights:
            print(flight["Flight No"] + " - Destination: " + flight["Destination"] + " - Price: ₹" + str(flight["Price"]))


while True:
    print("\nFlight Reservation System")
    print("1. Signup")
    print("2. Signin")
    print("3. Signout")
    print("4. Search available flights")
    print("5. Book a flight ticket")
    print("6. Cancel a booking")
    print("7. Filter flights by price")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        signup()
    elif choice == "2":
        signin()
    elif choice == "3":
        signout()
    elif choice == "4":
        search_flights()
    elif choice == "5":
        book_ticket()
    elif choice == "6":
        cancel_booking()
    elif choice == "7":
        filter_flights_by_price()
    elif choice == "8":
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice")
