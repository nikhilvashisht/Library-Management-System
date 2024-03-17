from storage import StorageManager, Logger
import isbnlib

class CheckoutManager(Logger, StorageManager):
    """
        Class for managing book checkouts. Functionality 
        can be extended to checking books in with ease.
    """
    
    def checkout_book(self, userID, ISBN):
        #validating if the isbn number is valid or not
        is_valid_isbn = isbnlib.is_isbn13(ISBN) or isbnlib.is_isbn10(ISBN)
        if is_valid_isbn and len(userID) > 0:
            book = [userID, ISBN]
            super().add('checkouts.csv', book)
            print("Book checked out.")
            super().log_message(f"Book checked out. ISBN - {ISBN}")
        elif is_valid_isbn == False:
            print("Please enter a valid ISBN!")
        else:
            print("Please enter a valid userID!")
            
