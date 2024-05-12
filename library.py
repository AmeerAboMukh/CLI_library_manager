import json
from book import Book

class Library:
    def __init__(self):
        """
        Initialize a Library object with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Add a book to the library.

        Args:
            book (Book): The book object to be added to the library.
        """
        # Check if a book with the same title already exists
        if any(existing_book.title == book.title for existing_book in self.books):
            print(f"A book with the title '{book.title}' already exists.")
            return
        # If not, add the new book to the library
        self.books.append(book)

    def list_books(self):
        """
        List all books in the library.
        """
        for index, book in enumerate(self.books, start=1):
            print(f"{index}.")
            book.display_details()

    def edit_book(self, index, new_details):
        """
        Edit the details of a book in the library.

        Args:
            index (int): The index of the book to be edited.
            new_details (dict): A dictionary containing the new details of the book.
        """
        if 0 < index <= len(self.books):
            self.books[index - 1].__dict__.update(new_details)

    def delete_book(self, index):
        """
        Delete a book from the library.

        Args:
            index (int): The index of the book to be deleted.
        """
        if 0 < index <= len(self.books):
            del self.books[index - 1]

    def save_library(self, filename):
        """
        Save the library to a JSON file.

        Args:
            filename (str): The name of the JSON file to save the library to.
        """
        with open(filename, 'w') as file:
            json.dump([vars(book) for book in self.books], file)

    @classmethod
    def load_library(cls, filename):
        """
        Load a library from a JSON file.

        Args:
            filename (str): The name of the JSON file to load the library from.

        Returns:
            Library: The loaded library object.
        """
        library = cls()
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for book_data in data:
                    # Ensure that only valid attributes are passed to Book constructor
                    book_data.pop('rating', None)  # Remove 'rating' if present
                    library.add_book(Book(**book_data))
        except (FileNotFoundError, json.JSONDecodeError):
            pass  # Handle file not found or invalid JSON gracefully
        return library
