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
                        VALUES (:user_id, :post_path, :username, :group_id, :description)",
                            user_id = self.user_id,
                            post_path = img_path,
                            username = name[0]["username"],
                            group_id = group,
                            description = description)

        def loadgroups(self):
                result = db.execute("SELECT * FROM follow where user_id = :user_id", user_id = self.user_id)
                return result

        def comment(self, post_id, comment):

                # look up username using user_id
                name = db.execute("SELECT username FROM users WHERE user_id = :user_id", user_id = self.user_id)

                # import comment into databse
                db.execute("INSERT INTO comment (post_id, user_id, username, comment, comment_gif) \
                           VALUES (:post_id, :user_id, :username, :comment, :comment_gif)",
                           post_id = post_id,
                           user_id = self.user_id,
                           username = name[0]["username"],
                           comment = comment,
                           comment_gif = "empty")

                return True

        def comment_gif(self, post_id, comment_gif):

                # look up username using user_id
                name = db.execute("SELECT username FROM users WHERE user_id = :user_id", user_id = self.user_id)

                # import comment into databse
                db.execute("INSERT INTO comment (post_id, user_id, username, comment, comment_gif) \
                           VALUES (:post_id, :user_id, :username, :comment, :comment_gif)",
                           post_id = post_id,
                           user_id = self.user_id,
                           username = name[0]["username"],
                           comment = "empty",
                           comment_gif = comment_gif)

                return True

        def loadcomments(self):
                comments = db.execute("SELECT * FROM comment")
                return comments
