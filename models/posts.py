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
                db.execute("INSERT INTO posts (user_id, post_path, username, group_id, description, likes) \
                        VALUES (:user_id, :post_path, :username, :group_id, :description, :likes)",
                            user_id = self.user_id,
                            post_path = img_path,
                            username = name[0]["username"],
                            group_id = group,
                            description = description,
                            likes = 0)

        def loadgroups(self):
                # loads all groups that are followed by the user
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

                # import gif comment into databse
                db.execute("INSERT INTO comment (post_id, user_id, username, comment, comment_gif) \
                           VALUES (:post_id, :user_id, :username, :comment, :comment_gif)",
                           post_id = post_id,
                           user_id = self.user_id,
                           username = name[0]["username"],
                           comment = "empty",
                           comment_gif = comment_gif)
                return True

        def loadcomments(self):
                # loads all comments and returns it
                return db.execute("SELECT * FROM comment")


        def like(self, post_id):
                # check if the post is already liked
                check = db.execute("SELECT * FROM likes WHERE post_id = :post_id AND user_id = :user_id", post_id = post_id, user_id = self.user_id)

                # if the post is already liked the like will be removed
                if len(check) != 0:
                        update = db.execute("UPDATE posts SET likes = likes - :new_like WHERE post_id = :post_id", new_like = 1, post_id=post_id)
                        result = db.execute("DELETE FROM likes WHERE user_id = :user_id AND post_id = :post_id", user_id = self.user_id, post_id = post_id)
                        return result

                # otherwise the post will be liked
                update = db.execute("UPDATE posts SET likes = likes + :new_like WHERE post_id = :post_id", new_like = 1, post_id=post_id)
                result = db.execute("INSERT INTO likes (user_id, post_id) VALUES (:user_id, :post_id)", user_id = self.user_id, post_id = post_id,)
                return result


