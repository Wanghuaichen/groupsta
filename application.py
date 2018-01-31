from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for, jsonify
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
from flask_uploads import UploadSet, IMAGES, configure_uploads
import json

from helpers import *
import time
from models import users, groups, posts
import safygiphy

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure flask_upload API
photos = UploadSet("photos", IMAGES)
app.config["UPLOADED_PHOTOS_DEST"] = "static/img/"
configure_uploads(app, photos)


@app.route("/", methods=["GET", "POST"])
@login_required
def index():

    # instantiate giphy, post and Group
    giphy = safygiphy.Sticky(token="aYiNwV98zSwp2eeIQ1ucWNpAtEaTt51r")
    post = posts.Post(session["user_id"])
    group = groups.Group(session["user_id"])

    # retrieve data
    groupfollow = group.followed()
    feed = group.mainfeed()
    trending = giphy.trending(limit=25)
    trending_list = [trending["data"][i]["images"]["fixed_width_small"]["url"] for i in range(25)]
    comments = post.loadcomments()

    if request.method == "POST":

        # requesting all data
        likes = request.form.get("likes")
        gif_link = request.form.get("gif")
        post_id = request.form.get("post_id")
        comment = request.form.get("comment")

        # if like is requested
        if likes:
            post.like(likes)
            return redirect(url_for("index"))

        # if text comment
        elif comment:
            post.comment(post_id, comment)
            comments = post.loadcomments()
            return render_template("index.html", groupnames = groupfollow, feed = feed, gif_list = trending_list, comments=comments)

        # if a giphy is requested
        elif gif_link:
            post.comment_gif(post_id, gif_link)
            comments = post.loadcomments()
            return render_template("index.html", groupnames = groupfollow, feed = feed, gif_list = trending_list, comments=comments)

    else:
        return render_template("index.html", groupnames = groupfollow, feed = feed, gif_list = trending_list, comments=comments)


@app.route("/<group_name>")
@login_required
def group(group_name):

    # instantiate giphy, post and Group
    giphy = safygiphy.Sticky(token="aYiNwV98zSwp2eeIQ1ucWNpAtEaTt51r")
    post = posts.Post(session["user_id"])
    group = groups.Group(session["user_id"])
    group_id = group.nametoid(group_name)

    # retrieve data
    group_id = group.nametoid(group_name)
    info = group.groupinfo(group_id)
    feed = group.loadfeed(group_id)
    groupfollow = group.followed()
    trending = giphy.trending(limit=25)
    trending_list = [trending["data"][i]["images"]["fixed_width_small"]["url"] for i in range(25)]
    comments = post.loadcomments()

    return render_template("index.html", groupnames = groupfollow, info = info, feed = feed, gif_list = trending_list, comments=comments)

@app.route("/livesearch")
def livesearch():

    search_results = None

    # retrieve all the groups from the database
    user_id = session["user_id"]
    group = groups.Group(user_id)
    data = group.loadgroups()

    # request the input text from the form
    text = request.args['searchText']

    # check if input text is in database data
    if len(text) >= 2:
        result = {"results":[], "group_id":[], "bio":[]
        }
        for element in data:
            for i in element:
                if i == 'group_name':
                    searchable = element[i]
                    if str(text).lower() in str(searchable).lower():
                        result["results"].append(searchable)
                        result["group_id"].append(element["group_id"])
                        result["bio"].append(element["bio"])
                else:
                    pass
        session["search_results"]  = result
        print (result)
        return json.dumps(result)

    else:
        return None

@app.route("/search", methods=["GET", "POST"])
@login_required
def search():

    # # instantiate functions
    group = groups.Group(session["user_id"])

    # make variables
    results = session["search_results"]
    user_id = session["user_id"]

    if not results:
        results = ["No groups found"]

    # convert group names to group id's

    group_id_result = [group.nametoid(result) for result in results]
    print(group_id_result)
    # load info per group
    group_info = []
    for id in group_id_result:
        group = groups.Group(user_id)

        # aan groupinfo moet hier nog een group_id meegegeven worden
        group_info.append(group.groupinfo(id))

    group_info = [element for sublist in group_info for element in sublist]

    return render_template("search.html", group_info = group_info)

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""

    if request.method == "POST":

        # ensure username input not blank
        if not request.form.get("username"):
            return render_template("register.html", error="Please choose a username.")

        # ensure password not blank
        elif not request.form.get("password"):
            return render_template("register.html", error="Please choose a password")

        # ensure same password filled in again
        if request.form.get("password") != request.form.get("passwordcheck"):
            return render_template("register.html", error="Passwords do not match.")

        # ensure first name not blank
        if not request.form.get("first_name"):
            return render_template("register.html", error="Please enter your first name.")

        # ensure last name not blank
        elif not request.form.get("last_name"):
            return render_template("register.html", error="Please enter your last name.")


        # retrieve user after register
        register = users.User.register(request.form.get("username"),
                                       request.form.get("password"),
                                       request.form.get("first_name"),
                                       request.form.get("last_name"))

        # if username already exists
        if register is None:
            return render_template("register.html", error="Username already exists.")

        # if register successful
        else:

            # log user in
            session["user_id"] = register["user_id"]

            # redirect user to homepage
            return redirect(url_for("index"))

    else:
        return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in. """

    # forget any user_id
    session.clear()

    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return render_template("login.html", missing_name = "Username missing")

        # ensure password was submitted
        elif not request.form.get("password"):
            return render_template("login.html", missing_pass = "Password missing")

        # retrieve user after login
        login = users.User.login(request.form.get("username"), request.form.get("password"))

        # if login unsuccessful
        if login is None:
            return render_template("login.html", failure = "Login unsuccessful!")

        # if login successful
        else:

            # log user in
            session["user_id"] = login["user_id"]
            return redirect(url_for("index"))

    # user reached page via GET
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()
    return redirect(url_for("login"))


@app.route("/followgroup", methods=["GET", "POST"])
@login_required
def followgroup():

    # instantiate functions
    group = groups.Group(session["user_id"])
    followable = group.exploregroups()

    # load grouplist in sidebar
    groupfollow = group.followed()

    if request.method == "POST":

        # controls if a button is pressed and which button is pressed
        if request.form["action"]:
            group_id = request.form["action"]
            session["group_id"] = group_id

            # the group_id of the pressed button will be transported to the follow function and returns the follow_id
            result = group.follow(group_id)

            # follow unsuccessful
            if result == None:
                return render_template("followgroup.html", followable = followable, error = "You're already member of this group", groupnames = groupfollow)
            else:
                return redirect(url_for("index"))

    else:
        return render_template("followgroup.html", followable = followable, groupnames = groupfollow)

@app.route("/post", methods=["GET", "POST"])
@login_required
def post():

    # instantiate functions
    post = posts.Post(session["user_id"])
    following = post.loadgroups()

    # load grouplist in sidebar
    group = groups.Group(session["user_id"])
    groupfollow = group.followed()

    if request.method == "POST" and 'photo' in request.files:

        # request photo
        photo = request.files["photo"]

        # check for correct user input
        if not photo:
            return render_template("post.html", groups = following, error = "no photo uploaded, pick one!", groupnames = groupfollow)

        # check for allowed extensions
        filename = str(photo.filename)
        if filename.endswith(('.jpg','.png','.jpeg','.gif','.JPG','.PNG','.JPEG','.GIF')):

            # if allowed, save photo in folder
            file = photos.save(photo)

            # check in which group to post
            choice = request.form["group"]
            if not choice:
                return render_template("post.html", groups=following, error = "no group chosen", groupnames = groupfollow)
            session["group_id"] = choice

            # pull description of photo
            description = request.form["description"]

            # insert into database
            path = file
            post.upload(path, choice, description)

            return redirect(url_for("index"))

        # if extension is not allowed
        else:
            return render_template("post.html", groups = following, error = "extension not allowed", groupnames = groupfollow)

    else:
        return render_template("post.html", groups = following, groupnames = groupfollow)

@app.route("/settings", methods=["GET", "POST"])
@login_required
def settings():

    # load grouplist in sidebar
    group = groups.Group(session["user_id"])
    groupfollow = group.followed()

    if request.method == "POST":

        # instantiate user
        user = users.User(session["user_id"])

        # checks if password button is pressed
        if request.form["action"] == "Change password":

            # checks if any form blank
            if not request.form.get("current_password"):
                return render_template("settings.html", missingcurrent = "Current password missing", groupnames = groupfollow)

            if not request.form.get("new_password"):
                return render_template("settings.html", missingnew = "New password missing", groupnames = groupfollow)

            if not request.form.get("check_password"):
                return render_template("settings.html", missingcheck = "Password check missing", groupnames = groupfollow)

            # check if new password and password match
            if request.form.get("new_password") != request.form.get("check_password"):
                return render_template("settings.html", nomatch = "Passwords do not match", groupnames = groupfollow)

            # change password in the database
            change_password = user.change_password(request.form.get("current_password"),
                                          request.form.get("new_password"),
                                          request.form.get("check_password"))

            # if change successful
            if change_password == True:
                return render_template("settings.html", success= "Password changed!", groupnames = groupfollow)

            else:
                return render_template("settings.html", failure = "Current password is incorrect!", groupnames = groupfollow)


        # checks if username button is pressed
        elif request.form["action"] == "Change username":

            # checks if any form blank
            if not request.form.get("current_username"):
                return render_template("settings.html", missingcurrent = "Current username missing", groupnames = groupfollow)

            if not request.form.get("new_username"):
                return render_template("settings.html", missingnew2 = "New username missing", groupnames = groupfollow)

            if not request.form.get("current_password"):
                return render_template("settings.html", missingcheck2 = "Password is missing", groupnames = groupfollow)

            # change username in databases
            change_username = user.change_username(request.form.get("current_username"),
                                                   request.form.get("new_username"),
                                                   request.form.get("current_password"))

            if change_username is True:
                return render_template("settings.html", success = "Username changed!", groupnames = groupfollow)

            if change_username is False:
                return render_template("settings.html", failure2 = "Password is incorrect!", groupnames = groupfollow)

            if change_username is None:
                return render_template("settings.html", failure2 = "Username already exists!", groupnames = groupfollow)

    else:
        return render_template("settings.html", groupnames = groupfollow)


@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():

    # instantiate giphy, post, group and user
    giphy = safygiphy.Sticky(token="aYiNwV98zSwp2eeIQ1ucWNpAtEaTt51r")
    post = posts.Post(session["user_id"])
    group = groups.Group(session["user_id"])
    user = users.User(session["user_id"])

    # retrieve data
    groupfollow = group.followed()
    feed = user.profilefeed()
    trending = giphy.trending(limit=25)
    trending_list = [trending["data"][i]["images"]["fixed_width_small"]["url"] for i in range(25)]
    comments = post.loadcomments()

    if request.method == "POST":

        # retrieve data
        gif_link = request.form.get("gif")
        post_id = request.form.get("post_id")
        comment = request.form.get("comment")

        # if text comment
        if not gif_link:
            post.comment(post_id, comment)
            comments = post.loadcomments()
            return render_template("profile.html", groupnames = groupfollow, feed = feed, gif_list = trending_list, comments=comments)

        else:
            post.comment_gif(post_id, gif_link)
            comments = post.loadcomments()
            return render_template("profile.html", groupnames = groupfollow, feed = feed, gif_list = trending_list, comments=comments)

    else:
        return render_template("profile.html", groupnames = groupfollow, feed = feed, gif_list = trending_list, comments=comments)

@app.route("/create", methods=["GET", "POST"])
@login_required
def create():

    # load grouplist in sidebar
    group = groups.Group(session["user_id"])
    groupfollow = group.followed()

    if request.method == "POST":
        # checks if inputs are correct
        if not request.form.get("title"):
            return render_template("create.html", missingtitle = "The title is missing", groupnames = groupfollow)

        elif not request.form.get("description"):
            return render_template("create.html", missingdesc = "The description is missing", groupnames = groupfollow)

        # create function is being called and generates output
        group = groups.Group(session["user_id"])
        create = group.create(request.form.get("title"), request.form.get("description"))

        # if the title already exists
        if create == None:
            return render_template("create.html", missingtitle = "The title already exists", groupnames = groupfollow)
        session["group_id"] = create

        return redirect(url_for("index"))
    else:
        return render_template("create.html",groupnames = groupfollow)

