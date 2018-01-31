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

            # check if new_password and password_check match and encrypyts the new password
            if new_password == check_password:
                hash_password = pwd_context.hash(new_password)

                # update password
                db.execute("UPDATE users SET hash = :new_password WHERE user_id = :user_id",
                            new_password=hash_password, user_id=self.user_id)
                return True

            else:
                return False

        else:
            return False

    def change_username(self, current_username, new_username, current_password):

        # check if new username already exists
        result = db.execute("SELECT * FROM users WHERE username = :username", username=new_username)
        if len(result) != 0:
            return None

        # retrieve user
        user = db.execute("SELECT * FROM users WHERE user_id = :user_id", user_id=self.user_id)

        # check if current password is correct and username is correct
        if pwd_context.verify(current_password, user[0]["hash"]):
            if user[0]["username"] == current_username:
                db.execute("UPDATE users SET username = :new_username WHERE user_id = :user_id",
                            new_username = new_username, user_id=self.user_id)
                return True

            else:
                return False

    def profilefeed(self):

        # loads the amount of posts
        count = db.execute("SELECT count(*) FROM posts;")

        # all the user's posts will be collected and will be returned in the feed
        if len(count) != 0:
            count = int(count[0]['count(*)'])
            return db.execute("SELECT * FROM posts WHERE user_id = :user_id ORDER BY time DESC Limit :count;", user_id = self.user_id, count = count)
        else:
            return None