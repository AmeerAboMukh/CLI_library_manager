class Book:
    def __init__(self, title, author, publication_year, genre):
        """
        Initialize a Book object with the provided attributes.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            publication_year (int): The publication year of the book.
            genre (str): The genre of the book.
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre

    def display_details(self):
        """
        Display the details of the book.
        """
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Genre: {self.genre}")
