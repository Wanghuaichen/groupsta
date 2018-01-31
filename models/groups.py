from cs50 import SQL
from passlib.apps import custom_app_context as pwd_context

# configure CS50 Library to use SQlite database
db = SQL("sqlite:///groupsta.db")

class Group():

    def __init__(self, user_id):
        self.user_id = user_id


    def create(self, title, description):

        # check if title already exist
        result = db.execute("SELECT * FROM groups WHERE group_name = :title", title=title)
        if len(result) != 0:
            return None

        # insert into database
        group = db.execute("INSERT INTO groups (group_name, bio) VALUES (:group_name, :bio)", group_name = title, bio = description)

        # select group id from the database
        group_id = db.execute("SELECT group_id FROM groups WHERE group_name=:title", title=title)
        group_id = int(group_id[0]['group_id'])
        result = db.execute("INSERT INTO follow (user_id, group_id, groupname, admin) VALUES (:user_id, :group_id, :groupname, :admin)", user_id = self.user_id, group_id = group_id, groupname = title, admin = int(1))
        return group_id

    def follow(self, group_id):
        result = db.execute("SELECT * FROM follow WHERE group_id=:group_id AND user_id=:user_id", group_id = group_id, user_id = self.user_id)
        if len(result) != 0:
            return None

        # collects groupname for the group_id
        groupname = db.execute("SELECT group_name FROM groups WHERE group_id=:group_id", group_id=group_id)
        groupname = str(groupname[0]['group_name'])

        # insert into new following request in the follow database
        result = db.execute("INSERT INTO follow (user_id, group_id, groupname, admin) VALUES (:user_id, :group_id, :groupname, :admin)", \
        user_id = self.user_id, group_id = group_id, groupname = groupname, admin = int(0))

        # returns follow_id to application.py
        follow_id = db.execute("SELECT follow_id from follow WHERE group_id = :group_id AND user_id = :user_id", group_id = group_id, user_id = self.user_id)
        follow_id = int(follow_id[0]['follow_id'])

        return follow_id

    def exploregroups(self):

        # loads random group's name, description and every other kind of information about the groups
        result = db.execute("SELECT * FROM groups ORDER BY RANDOM() LIMIT 5")
        return result

    def loadgroups(self):

        # loads every group's name, description and every other kind of information about the groups
        result = db.execute("SELECT * FROM groups")
        return result

    def loadfeed(self, group_id):

        # loads all posts of a group
        count = db.execute("SELECT count(*) FROM posts;")
        if len(count) != 0:
            count = int(count[0]['count(*)'])
            feed = db.execute("SELECT * FROM posts WHERE group_id = :group_id ORDER BY time DESC Limit :count;", group_id = group_id, count = count)
            return feed
        else:
            return None

    def groupinfo(self, group_id):

        # loads basic information of the group
        info = db.execute("SELECT * FROM groups WHERE group_id = :group_id", group_id = group_id)
        if len(info) != 0:
            name = info[0]["group_name"]
            return name
        else:
            return None

    def nametoid(self, groupname):
        # looks for the right user_id by the given username
        group_id = db.execute("SELECT group_id FROM groups WHERE group_name = :group_name", group_name = groupname)
        group_id = int(group_id[0]['group_id'])
        if len(group_id) != 0:
            return group_id
        else:
            return None

    def followed(self):
        # select groupnames that apply to current user-login
        return db.execute("SELECT groupname FROM follow WHERE user_id = :id",id = self.user_id)


    def mainfeed(self):
        # loads all posts of groups you follow
        count = db.execute("SELECT count(*) FROM posts;")
        count = int(count[0]['count(*)'])

        if len(count) != 0:
            posts = db.execute("SELECT * FROM posts WHERE group_id IN (SELECT group_id FROM follow WHERE user_id = :user_id) ORDER BY time DESC Limit :count;", user_id = self.user_id, count = count)
            return posts
        return None
