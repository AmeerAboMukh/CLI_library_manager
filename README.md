# Personal Library Manager

This Python program allows users to manage their personal library by adding, listing, editing, and deleting books.

## Getting Started

To use the library manager, follow these steps:

1. Clone the repository to your local machine.
```bash
   git clone <repository_url>
```
2. Install the required dependencies.
```
pip install -r requirements.txt
```

3. Run the program using Python.

## Usage

### Adding a Book
To add a new book to your library, use the `-a` or `--add` flag. You will be prompted to enter the details of the book, including title, author, publication year, and genre.

```
python main.py -a
```

### Listing Books

To list all books in your library, use the -l or --list flag.
```
python main.py -l
```
### Editing a Book

To edit the details of a book, specify the index of the book you want to edit using the -e or --edit flag. You will be prompted to enter the new details for the book.

```
python main.py -e INDEX
```

### Deleting a Book

To delete a book from your library, specify the index of the book you want to delete using the -d or --delete flag.
```
python main.py -d INDEX
```

## File Management

The program automatically saves your library to a JSON file named library.json after each operation.

## Examples

### Adding a Book
```

Enter title: Harry Potter and the Philosopher's Stone
Enter author: J.K. Rowling
Enter publication year: 1997
Enter genre: Fantasy
```

### Listing Books
```
Title: Harry Potter and the Philosopher's Stone
Author: J.K. Rowling
Publication Year: 1997
Genre: Fantasy
```

### Editing a Book
```
Enter new title: Harry Potter and the Sorcerer's Stone
Enter new author: J.K. Rowling
Enter new publication year: 1998
Enter new genre: Fantasy
```

### Deleting a Book
```
Deleted book at index 1.
```
