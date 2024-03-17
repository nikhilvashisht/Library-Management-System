from storage import StorageManager, Logger

class UserManager(Logger, StorageManager):
    """
        Mananger class for adding and listing users
        to the library system. Functionality can be 
        extended to updating and deleting users with ease.
    """
    def add_user(self, name, userID):
        user = [name, userID]
        if len(user) > 0 and len(userID) > 0:
            super().add('users.csv', user)
            print("User Added.")
            super().log_message(f"User added. UserID - {userID}")
        else :
            print("Please enter valid username and userID!")

    def list_users(self):
        super().read('users.csv')