from database import add_user, get_user

class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password

    def register(self):
        # Store user data in the database
        add_user(self.user_id, {"username": self.username, "password": self.password})

    @staticmethod
    def login(username, password):
        for user_id, user_data in users_db.items():
            if user_data["username"] == username and user_data["password"] == password:
                return User(user_id, username, password)
        return None
