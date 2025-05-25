class Book:                                              #Used "class" as per the ques given in discord
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_checked_out = False
    
    def __str__(self):
        return f"{self.title} by {self.author} (Book ID: {self.book_id})"

class LibraryManager:                                    #Used "class" as per the ques given in discord      
    def __init__(self):                                  #Used "func" as per the ques given in discord     
        self.books = []
        self.next_book_id = 1
    
    def add_book(self, title, author):
        book = Book(title, author, self.next_book_id)
        self.books.append(book)
        self.next_book_id += 1
        return book
    
    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                return True
        return False
    
    def check_out_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and not book.is_checked_out:
                book.is_checked_out = True
                return True
        return False
    
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and book.is_checked_out:
                book.is_checked_out = False
                return True
        return False
    
    def list_books(self):
        return [str(book) + (" [Checked Out]" if book.is_checked_out else "") for book in self.books]

library = LibraryManager()

while True:
    print("\nLibrary Operations:")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Check Out Book")
    print("4. Return Book")
    print("5. List Books")
    print("6. Exit")
    user_input = input("Choose operation (1-6): ")
    
    if user_input == "1":
        title = input("\nEnter title: ")
        author = input("Enter author: ")
        library.add_book(title, author)
        print(f"Book added successfully with Book ID: {library.next_book_id - 1}")
    
    elif user_input == "2":
        book_id = int(input("\nEnter Book ID: "))
        if library.remove_book(book_id):
            print("Book removed successfully!")
        else:
            print("Book not found!!")
    
    elif user_input == "3":
        book_id = int(input("\nEnter Book ID: "))
        if library.check_out_book(book_id):
            print("Book checked out successfully!")
        else:
            print("Book not available or already checked out!")
    
    elif user_input == "4":
        book_id = int(input("\nEnter Book ID: "))
        if library.return_book(book_id):
            print("Book returned successfully!")
        else:
            print("Book not found or not checked out!!")
    
    elif user_input == "5":
        books = library.list_books()
        if books:
            for book in books:
                print(f"\n{book}")
        else:
            print("\nNo books in library!!")
    
    elif user_input == "6":
        print("\nExiting...\n")
        break
    
    else:
        print("Invalid operation!!!")