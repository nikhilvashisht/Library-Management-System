# Library Management System

## A simple library management system built with python. Currently the system has the functionality to : 
- Add new books
- List all books
- Add new users
- Checkout books from system

## Installation and Usage
1. Clone the repo
   ```
   https://github.com/nikhilvashisht/Library-Management-System.git
   ```
2. Install the requirements
   ```
   pip install requirements.txt
   ```
3. Run main.py
   ```
   python main.py
   ```
4. Choose whatever action you wish to perform from the menu

## Project description
1. The system uses a csv based file storage for storing all books, users and checkouts. All utilities for reading and writing to the files
are present in `StorageManager` in `storage.py`, along with `Logger` class which handles all logging of the actions performed. 
2. Handling books, users and checkouts are done by independent manager classes, namely `BookManager`, `UserManager` and `CheckManager`. These classes
have the utility methods for reading and writing different data to the files. \

Valid error handling has been to handle various edge cases: 
- When file is empty
- When file is not present
- ISBN and other fields entered in the system should be valid

Additionaly, OOP concepts such as **Inheritance** and **Encapsulation** have been used to enhance code structure and support future extensions. Also, I've also tried to follow **DRY** principle to make use of methods previously written and use them again.
