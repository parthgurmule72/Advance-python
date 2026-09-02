class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self):
        book = input("Enter Book Name: ")
        self.books[book] = "Available"
        print("Book added successfully!")

    def register_patron(self):
        patron = input("Enter Patron Name: ")
        self.patrons[patron] = []
        print("Patron registered successfully!")

    def view(self):
        print("\n----- Books -----")
        if len(self.books) == 0:
            print("No books available.")
        else:
            for book, status in self.books.items():
                print(book, "-", status)

        print("\n----- Patrons -----")
        if len(self.patrons) == 0:
            print("No patrons registered.")
        else:
            for patron in self.patrons:
                print(patron)

    def borrow_book(self):
        patron = input("Enter Patron Name: ")

        if patron not in self.patrons:
            print("Patron not found!")
            return

        book = input("Enter Book Name: ")

        if book in self.books and self.books[book] == "Available":
            self.books[book] = patron
            self.patrons[patron].append(book)
            print("Book issued successfully!")
        else:
            print("Book Not Available!")

    def return_book(self):
        patron = input("Enter Patron Name: ")
        book = input("Enter Book Name: ")

        if patron in self.patrons and book in self.patrons[patron]:
            self.books[book] = "Available"
            self.patrons[patron].remove(book)
            print("Book returned successfully!")
        else:
            print("Book not borrowed by this patron!")

library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. View Books & Patrons")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.register_patron()

    elif choice == "3":
        library.view()

    elif choice == "4":
        library.borrow_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")