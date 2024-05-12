import argparse
import json
from book import Book
from library import Library

def main():
    """
    Main function to manage the personal library.

    Parses command-line arguments, loads the library from a JSON file,
    performs actions based on the arguments provided, and saves the
    updated library to the JSON file.
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Personal Library Manager")
    parser.add_argument('-a', '--add', action='store_true', help="Add a new book")
    parser.add_argument('-l', '--list', action='store_true', help="List all books")
    parser.add_argument('-e', '--edit', type=int, metavar='INDEX', help="Edit the details of a book")
    parser.add_argument('-d', '--delete', type=int, metavar='INDEX', help="Delete a book by index")
    args = parser.parse_args()

    # Load library from JSON file
    library = Library.load_library("library.json")

    # Perform actions based on command-line arguments
    if args.add:
        title = input("Enter title: ")
        author = input("Enter author: ")
        publication_year = int(input("Enter publication year: "))
        genre = input("Enter genre: ")
        library.add_book(Book(title, author, publication_year, genre))
    elif args.list:
        library.list_books()
    elif args.edit:
        index = args.edit
        if 0 < index <= len(library.books):
            new_details = {}
            new_details['title'] = input("Enter new title: ")
            new_details['author'] = input("Enter new author: ")
            new_details['publication_year'] = int(input("Enter new publication year: "))
            new_details['genre'] = input("Enter new genre: ")
            library.edit_book(index, new_details)
        else:
            print("Invalid book index.")
    elif args.delete:
        index = args.delete
        if 0 < index <= len(library.books):
            library.delete_book(index)
        else:
            print("Invalid book index.")

    # Save library to file after making changes
    library.save_library("library.json")

if __name__ == "__main__":
    main()
