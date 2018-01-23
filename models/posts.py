from cs50 import SQL
from passlib.apps import custom_app_context as pwd_context

# configure CS50 Library to use SQlite database
db = SQL("sqlite:///groupsta.db")

class Post():
        def __init__(self, user_id):
                self.user_id = user_id

        def upload(self, img_path, group, description):
                # retrieve username of user
                name = db.execute("SELECT username FROM users WHERE user_id = :user_id", user_id = self.user_id)

                # import post in database of user
                db.execute("INSERT INTO posts (user_id, post_path, username, group_id, description) \
                        VALUES (:user_id, :post_path, :username, :group_id, :description)", \
                            user_id = self.user_id, \
                            post_path = img_path, \
                            username = name[0]["username"], \
                            group_id = group, \
                            description = description)

        def loadgroups(self):
                result = db.execute("SELECT * FROM follow where user_id = :user_id", user_id = self.user_id)
                return result