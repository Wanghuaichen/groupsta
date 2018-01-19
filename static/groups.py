from cs50 import SQL
from passlib.apps import custom_app_context as pwd_context

# configure CS50 Library to use SQlite database
db = SQL("sqlite:///groupsta.db")

class Group():

    def __init__(self, user_id, title, description):
        self.user_id = user_id
        self.title = title
        self.description = description


    def create(self):
        # check if title already exist
        result = db.execute("SELECT * FROM groups WHERE group_name = :title", title=self.title)
        if len(result) != 0:
            return None

        # insert into database
        group = db.execute("INSERT INTO groups (group_name, bio) VALUES (:group_name, :bio)", group_name = self.title, bio = self.description)

        # select group id from the database
        group_id = db.execute("SELECT group_id FROM groups WHERE group_name=:title", title=self.title)
        return group_id[0]
