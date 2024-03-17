# utility methods for storing and retrieving data from files
import csv
from datetime import datetime
import os

class StorageManager:
    """
        Base class for file storage. Contains methods
        for adding and reading data from files, can
        be extended to updating and deleting data from 
        files with ease. The class can be extended by 
        any manager inside the application which requires
        dealing with file data.
    """

    def add(self, filename, new_data):
        """
            Utility method for adding new_data to file

            Args: filename, data
            Returns: None
        """
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_data)

    def read(self, filename):
        """
            Utility method for reading the contents of a file.
            Checks if a file exists, or not. If the file does
            not exists, creates the file. Otherwise, reads the file
            contents.

            Args: filename
            Returns : None
        """
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                #try catch statement for checking if the file is empty or not
                if os.stat(filename).st_size == 0:  # Check if any rows exist
                    print("### No Entries Yet! ###")
                else:
                # Iterate over rows if the file is not empty
                    for row in reader:
                        print(row)
        except (OSError, FileNotFoundError):
            with open(filename, 'w') as file:
                print("### No Entries Yet! ###")

class Logger:
    """
        Base class for logging actions in the application. 
        Can be extended by any manager to log messages in the system.
        Permanently stores all messages inside disk.
    """

    def log_message(self, message):
        """
            Utility method for logging messages. 

            Args: message to be logged
            Returns: None
        """
        with open('logs.txt', 'a') as file:
            log = f'[ {datetime.now()} ] : {message}'
            file.write(log)
            file.write('\n')
            file.flush()

    
