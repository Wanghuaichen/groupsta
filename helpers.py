from flask import redirect, render_template, request, session
from passlib.apps import custom_app_context as pwd_context

def BackEndLogIN(username, password)
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=username)

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(password, rows[0]["hash"]):
            return null

        # remember which user has logged in
        return [0]["id"]