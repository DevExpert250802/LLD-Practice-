# Online Movie Ticket Booking System

movies = [
    ("Inception", "6:00 PM"),
    ("Interstellar", "9:00 PM"),
    ("Avengers", "3:00 PM"),
    ("Joker", "8:00 PM")
]

bookings = {}
seats = set()

def view_movie():
    print("\nAvailable Movies:")
    for movie in movies:
        print(movie[0] + " - Show Time: " + movie[1])

def book_ticket():
    user = input("Enter your name: ").strip()
    view_movie()
    movie_name = input("Enter the movie name: ").strip()
    seat_number = input("Enter seat number: ").strip()

    if seat_number in seats:
        print("Seat " + seat_number + " is already booked.")
        return

    for movie in movies:
        if movie[0].lower() == movie_name.lower():
            if user not in bookings:
                bookings[user] = []
            bookings[user].append((movie[0], seat_number))
            seats.add(seat_number)
            print("Ticket booked for " + movie[0] + " - Seat No: " + seat_number)
            return

    print("Movie not found. Please try again.")

def cancel_ticket():
    user = input("Enter your name: ").strip()
    
    if user not in bookings or not bookings[user]:
        print("No bookings found for " + user + ".")
        return

    print("\nYour Bookings:")
    for booking in bookings[user]:
        print("- " + booking[0] + " - Seat No: " + booking[1])

    seat_number = input("Enter seat number to cancel: ").strip()

    for booking in bookings[user]:
        if booking[1] == seat_number:
            bookings[user].remove(booking)
            seats.remove(seat_number)
            print("Booking cancelled for " + booking[0] + " - Seat No: " + seat_number)
            return

    print("Seat number " + seat_number + " not found in your bookings.")

def view_booking_history():
    user = input("Enter your name: ").strip()
    
    if user not in bookings or not bookings[user]:
        print("No bookings found for " + user + ".")
        return

    print("\nYour Booking History:")
    for booking in bookings[user]:
        print("- " + booking[0] + " - Seat No: " + booking[1])

while True:
    print("\nOnline Movie Ticket Booking System")
    print("1. View available movies")
    print("2. Book tickets")
    print("3. Cancel tickets")
    print("4. Check booking history")
    print("5. Exit")
    
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        view_movie()
    elif choice == "2":
        book_ticket()
    elif choice == "3":
        cancel_ticket()
    elif choice == "4":
        view_booking_history()
    elif choice == "5":
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
