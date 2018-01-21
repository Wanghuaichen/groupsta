from cs50 import SQL
from passlib.apps import custom_app_context as pwd_context

# configure CS50 Library to use SQlite database
db = SQL("sqlite:///groupsta.db")

class Group():

    def __init__(self, user_id, title, group_id, description):
        self.user_id = user_id
        self.title = title
        self.group_id = group_id
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
        group_id = int(group_id[0]['group_id'])
        result = db.execute("INSERT INTO follow (user_id, group_id, groupname, admin) VALUES (:user_id, :group_id, :groupname, :admin)", user_id = self.user_id, group_id = group_id, groupname = self.title, admin = int(1))
        return group_id

    def follow(self):
        group_ids = db.execute("SELECT group_id FROM groups")
        group_ids = int(group_id[0]['group_id'])
        for i in group_ids:
            if self.group_id == group_ids:
                groupname = db.execute("SELECT groupname FROM groups WHERE group_id=:group_id", group_id=self.group_id)

                result = de.execute("INSERT INTO follow (user_id, group_id, groupname, admin) VALUES (:user_id, :group_id, :groupname, :admin)", \
                user_id = self.user_id, group_id = group_id, groupname = groupname, admin = 0)

                follow_id = db.execute("SELECT follow_id from follow WHERE group_id = :group_id AND user_id = :user_id", group_id = self.group_id, user_id = self.user_id)
                follow_id = int(follow_id[0]['follow_id'])
                return follow_id
        return None

    def loadgroups(self):
        result = db.execute("SELECT * FROM groups")
        return result


