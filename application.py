from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)

@app.route("/")
def index():
from helpers import *

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # ensure username was submitted
        if not username or not password:
            return apology("must provide username")


        BackEndLogIN(username, password)

    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""
     # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # checks if all inputs satisfies the needs
        if not request.form.get("username"):
            return apology("must provide username")

        elif not request.form.get("password"):
            return apology("must provide both password")

        elif not request.form.get("password1"):
            return apology("must provide both passwords")

        elif request.form.get("password") != request.form.get("password1"):
             return apology("both passwords should be equal")

        # stores the encrypted password
        password = request.form.get("password")
        hash = pwd_context.hash(password)

        # checks if username is unique and stores it
        result = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", \
        username=request.form.get("username"), hash=hash)

        if not result:
            return apology("username already exists")

        # redirect to the home (index) page
        return redirect(url_for("index"))

    else:
        return render_template("register.html")
