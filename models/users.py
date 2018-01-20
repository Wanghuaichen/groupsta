from cs50 import SQL
from passlib.apps import custom_app_context as pwd_context

# configure CS50 Library to use SQlite database
db = SQL("sqlite:///groupsta.db")

class User():

    def __init__(self, user_id):
        self.user_id = user_id


    def register(username, password, first_name, last_name):

        # encrypt password
        hash_password = pwd_context.hash(password)

        # check if username already exists
        result = db.execute("SELECT * FROM users WHERE username = :username", username=username)
        if len(result) != 0:
            return None

        else:
            # insert new user into users
            db.execute("INSERT INTO users (username, hash, first_name, last_name) VALUES (:username, :hash, :first_name, :last_name)",
                        username=username,
                        hash=hash_password,
                        first_name=first_name,
                        last_name=last_name)

            # retrieve user
            user = db.execute("SELECT * FROM users WHERE username = :username", username=username)

            # return User
            return user[0]

    def login(username, password):

        # query database for username
        user = db.execute("SELECT * FROM users WHERE username = :username", username=username)

        # ensure username exists and password is correct
        if len(user) != 1 or not pwd_context.verify(password, user[0]["hash"]):
            return None

        else:
            return user[0]

    def change_password(self, current_password, new_password, check_password):

        # retrieve user
        user = db.execute("SELECT * FROM users WHERE user_id = :user_id", user_id=self.user_id)

        # check if current password is correct
        if pwd_context.verify(current_password, user[0]["hash"]):

            # check if new_password and password_check match
            if new_password == check_password:

                # encrypt new password
                hash_password = pwd_context.hash(new_password)

                # update password
                db.execute("UPDATE users SET hash = :new_password WHERE user_id = :user_id",
                            new_password=hash_password, user_id=self.user_id)
                return True

            else:
                return False

        else:
            return False


    # MOET NOG GETEST WORDEN MAAR DAARVOOR MOETEN WE EVEN DE HTML VAN SETTINGS BESPREKEN
    def change_username(self, current_username, new_username, current_password):

        # retrieve user
        user = db.execute("SELECT * FROM users WHERE user_id = :user_id", user_id=self.user_id)

        # check if current password is correct
        if pwd_context.verify(current_password, user[0]["hash"]):

            # check if current_username is correct
            if user[0]["username"] == current_username:

                # update username
                db.execute("UPDATE users SET username = :new_username WHERE user_id = :user_id",
                            new_username = new_username, user_id=self.user_id)
                return True

            else:
                return False