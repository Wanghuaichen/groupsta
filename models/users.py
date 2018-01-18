from cs50 import SQL
from passlib.apps import custom_app_context as pwd_context

# configure CS50 Library to use SQlite database
db = SQL("sqlite:///finance.db")

class User():

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):

        # encrypt password
        hash_password = pwd_context.hash(self.password)

        # check if username already exists
        result = db.execute("SELECT * FROM users WHERE username = :username", username=self.username)
        if len(result) != 0:
            return None

        else:

            # insert new user into users
            db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
            username=self.username, hash=hash_password)

            # retrieve user
            user = db.execute("SELECT * FROM users WHERE username = :username", username=self.username)

            # return User
            return user[0]

    def login(self):

        # query database for username
        user = db.execute("SELECT * FROM users WHERE username = :username", username=self.username)

        # ensure username exists and password is correct
        if len(user) != 1 or not pwd_context.verify(self.password, user[0]["hash"]):
            return None

        else:
            return user[0]

