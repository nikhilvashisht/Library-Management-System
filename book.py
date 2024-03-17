from storage import StorageManager, Logger
import isbnlib

class BookManager(StorageManager, Logger):
    """
        Manager class for adding and reading books 
        from the file system. Functionality can be extended
        to updating and deleting files with ease.
    """

    def add_book(self, title, author, ISBN):
        """
            Method for adding books to system.

            Args: title, author and ISBN
            Returns: None
        """
        #validating if the isbn number is valid or not
        is_valid_isbn = isbnlib.is_isbn13(ISBN) or isbnlib.is_isbn10(ISBN)
        if is_valid_isbn and len(title) > 0 and len(author) > 0:
            book = [title, author, ISBN]
            super().add('books.csv', book)
            print("Book Added.")
            super().log_message(f"Book added. ISBN - {ISBN}")
        else :
            print("Please enter a valid ISBN!")

    def list_books(self):
        """
            Method for listing books present in the system.
        """
        super().read('books.csv')   
        super().log_message("List books.")   
