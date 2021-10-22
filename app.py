""" Imports operating system """
import os
from flask import (Flask, render_template, redirect, request, url_for, session,
                   flash)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# App config

app = Flask(__name__)

# MongoDB config

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Collections

category_collection = mongo.db.categories
hax_collection = mongo.db.hax
user_collection = mongo.db.users


@app.route("/")
@app.route("/index")
def index():
    """
    Returns user to the landing page
    """
    return render_template("pages/index.html")


@app.route("/get_hax")
def get_hax():
    """
    Takes user to the lifehacks page
    Gets stored hax from the database
    """
    hax = mongo.db.hax.find()
    return render_template("pages/hax.html", hax=hax)

# User authentication


# Sign Up
@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    Allows user to register for an account
    Checks if a username is already in use
    Forwards user onto their new member profile
    """
    if "user" in session:
        flash('You are already signed up!')
        return redirect(url_for("index"))

    if request.method == "POST":
        form = request.form.to_dict()

        # Checks if password and password1 match
        if form["user_password"] == form["user_password1"]:
            # If they do it will try to find user in db
            user = user_collection.find_one({"username": form["username"]})
            if user:
                flash(f"{form['username']} already exists!")
                return redirect(url_for("signup"))
            # If user doesn't exist register the new user
            # Hash password
            hash_pass = generate_password_hash(form['user_password'])
            # Create new user with hashed password
            user_collection.insert_one(
                {
                    "username": form['username'],
                    "password": hash_pass
                }
            )
            # Check if the user has been saved to db
            existing_user = user_collection.find_one(
                {"username": form["username"]})
            if existing_user:
                # Add user to session (Log in)
                session["user"] = existing_user["username"]
                return redirect(url_for(
                    "profile", user=existing_user["username"]))

            flash("There was a problem. Please try again.")
            return redirect(url_for("signup"))

        flash("Passwords must match!")
        return redirect(url_for("signup"))

    return render_template("pages/signup.html")


# Login
@app.route("/login", methods=["GET"])
def login():
    """
    Check if user is not logged in already
    """
    if "user" in session:
        existing_user = user_collection.find_one({"username": session["user"]})
        if existing_user:
            # If they are, redirect to user profile
            flash("You are already logged in!")
            return redirect(url_for("profile", user=existing_user["username"]))

    # Load the login page for the user
    return render_template("pages/login.html")


@app.route("/user_auth", methods=["POST"])
def user_auth():
    """
    Authenticates the user for log in
    """
    form = request.form.to_dict()
    existing_user = user_collection.find_one({"username": form["username"]})
    # Checks if the user is in db
    if existing_user:
        # If passwords match (hashed / real)
        if check_password_hash(
            (existing_user["password"]),
                form["user_password"]):
            # Log in the user
            session["user"] = form["username"]
            # If user is admin redirect to admin page
            if session["user"] == "admin":
                return redirect(url_for("admin"))

            flash("You are now logged in!")
            return redirect(url_for(
                "profile", user=existing_user["username"]))

        flash("Wrong username and/or password")
        return redirect(url_for("login"))

    flash("You must be registered first before you can log in.")
    return redirect(url_for("pages/signup"))


@app.route("/logout")
def logout():
    """
    Allows the user to log out
    Takes them back to the home page
    """
    session.clear()
    flash("You are now logged out!")
    return render_template("pages/index.html")


@app.route("/profile/<user>", methods=["GET", "POST"])
def profile(user):
    """
    User Profile
    """
    if "user" in session:
        # If so get user and pass to template
        existing_user = user_collection.find_one({"username": user})
        return render_template("pages/profile.html", user=existing_user)

    flash("You must be logged in first!")
    return redirect(url_for("index"))


@app.route("/add_task")
def add_task():
    return render_template("pages/add_task.html")


@app.errorhandler(404)
def page_not_found(error):
    """
    Renders error.html with 404 message
    """
    error_message = str(error)
    return render_template("pages/error.html",
                           error_message=error_message), 404


@app.errorhandler(500)
def server_error(error):
    """
    Renders error.html with 500 message.
    """
    error_message = str(error)
    return render_template("pages/error.html",
                           error_message=error_message), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
