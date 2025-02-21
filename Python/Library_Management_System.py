# Library Management System
library_catalog = {}

def add_book():
    book_code = input("Enter Book ID: ")
    book_name = input("Enter Book Title: ")
    book_writer = input("Enter Author Name: ")
    publish_year = input("Enter Publication Year: ")

    if book_code in library_catalog:
        print("Book ID already exists! Try again.")
    else:
        library_catalog[book_code] = {
            "title": book_name,
            "author": book_writer,
            "year": publish_year
        }
        print("Book added successfully!")

def display_books():
    if not library_catalog:
        print("No books available in the catalog.")
    else:
        print("\nList of Available Books:")
        for book_code, book_info in library_catalog.items():
            print("ID: " + book_code + ", Title: " + book_info['title'] + 
                  ", Author: " + book_info['author'] + ", Year: " + str(book_info['year']))

def search_book():
    search_id = input("Enter Book ID to search: ")
    if search_id in library_catalog:
        print("ID: " + search_id + ", Title: " + library_catalog[search_id]['title'] + 
              ", Author: " + library_catalog[search_id]['author'] + ", Year: " + str(library_catalog[search_id]['year']))
    else:
        print("Book not found in the catalog.")

def delete_book():
    delete_id = input("Enter Book ID to delete: ")
    if delete_id in library_catalog:
        del library_catalog[delete_id]
        print("Book deleted successfully!")
    else:
        print("Book ID not found.")

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        print("Exiting Library System. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1-5.")
