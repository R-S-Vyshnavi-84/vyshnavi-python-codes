class Library:
    def __init__(self):
        self.books = {}  # book_id: {title, author, available_copies}
        self.users = {}  # user_id: user_name
        self.issued_books = {}  # user_id: list of book_ids issued

    def add_book(self, book_id, title, author, copies):
        if book_id in self.books:
            print(f"Book ID {book_id} already exists. Updating copies.")
            self.books[book_id]['available_copies'] += copies
        else:
            self.books[book_id] = {
                'title': title,
                'author': author,
                'available_copies': copies
            }
        print(f"Book '{title}' added/updated successfully.")

    def register_user(self, user_id, user_name):
        if user_id in self.users:
            print(f"User ID {user_id} already registered.")
        else:
            self.users[user_id] = user_name
            print(f"User '{user_name}' registered successfully.")

    def issue_book(self, user_id, book_id):
        if user_id not in self.users:
            print("User not registered.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return
        if self.books[book_id]['available_copies'] <= 0:
            print("No copies available.")
            return

        self.books[book_id]['available_copies'] -= 1
        self.issued_books.setdefault(user_id, []).append(book_id)
        print(f"Book '{self.books[book_id]['title']}' issued to {self.users[user_id]}.")

    def return_book(self, user_id, book_id):
        if user_id not in self.users:
            print("User not registered.")
            return
        if user_id not in self.issued_books or book_id not in self.issued_books[user_id]:
            print("This book was not issued to the user.")
            return

        self.books[book_id]['available_copies'] += 1
        self.issued_books[user_id].remove(book_id)
        print(f"Book '{self.books[book_id]['title']}' returned by {self.users[user_id]}.")

    def display_books(self):
        print("\nAvailable Books:")
        for book_id, info in self.books.items():
            print(f"ID: {book_id}, Title: {info['title']}, Author: {info['author']}, Copies: {info['available_copies']}")

    def display_users(self):
        print("\nRegistered Users:")
        for user_id, name in self.users.items():
            print(f"User ID: {user_id}, Name: {name}")

    def display_issued_books(self):
        print("\nIssued Books:")
        for user_id, books in self.issued_books.items():
            user_name = self.users[user_id]
            book_titles = [self.books[bid]['title'] for bid in books]
            print(f"{user_name} ({user_id}): {', '.join(book_titles)}")
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Register User")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Display Users")
        print("7. Display Issued Books")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            copies = int(input("Enter Number of Copies: "))
            library.add_book(book_id, title, author, copies)

        elif choice == '2':
            user_id = input("Enter User ID: ")
            user_name = input("Enter User Name: ")
            library.register_user(user_id, user_name)

        elif choice == '3':
            user_id = input("Enter User ID: ")
            book_id = input("Enter Book ID: ")
            library.issue_book(user_id, book_id)

        elif choice == '4':
            user_id = input("Enter User ID: ")
            book_id = input("Enter Book ID: ")
            library.return_book(user_id, book_id)

        elif choice == '5':
            library.display_books()

        elif choice == '6':
            library.display_users()

        elif choice == '7':
            library.display_issued_books()

        elif choice == '8':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()
