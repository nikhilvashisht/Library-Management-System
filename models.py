class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
    def __str__(self):
        return f"Title: {self.title} \n Author : {self.author} \n ISBN : {self.ISBN}"

class User:
    def __init__(self, username, userID):
        self.username: username
        self.userID = userID
    def __str__(self):
        return f"Username: {self.username} \n UserID : {self.userID}"


    