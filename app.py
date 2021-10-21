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


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    Allows user to register for an account
    Checks if a username is already in use
    Forwards user onto their new member dashboard
    """
    if "user" in session:
        flash('You are already signed in')
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
            else:
                # Hash password
                hash_pass = generate_password_hash(form['user_password'])
                # Create new user with hashed password
                user_collection.insert_one(
                    {
                        "username": form['username'],
                        "email": form["email"],
                        "password": hash_pass
                    }
                )
                # Check if the user has been saved to db
                user_in_db = user_collection.find_one(
                    {"username": form["username"]})
                if user_in_db:
                    # Add user to session (Log in)
                    session["user"] = user_in_db["username"]
                    return redirect(url_for(
                        "dashboard", user=user_in_db["username"]))
                else:
                    flash("There was a problem. Please try again.")
                    return redirect(url_for("signup"))
        else:
            flash("Passwords must match!")
            return redirect(url_for("signup"))

    return render_template("signup")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Allows the user to login if they have an account
    Redirects to member dashboard
    """
    if request.method == "POST":
        user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user:
            if check_password_hash(user["password"],
               request.form.get("password")):
                user_id = str(user["_id"])
                session["user_id"] = str(user_id)

            else:
                flash("Incorrect Username and/or password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("pages/login.html")


@app.route("/logout")
def logout():
    """
    Allows the user to log out
    Takes them back to the home page
    """
    session.clear()
    return render_template("pages/index.html")


@app.route("/dashboard/<user_id>")
def blank_dashboard():
    """
    When the user has a new account or has not posted anything yet
    It will display a blank user profile dashboard
    """
    return render_template("pages/dashboard.html")


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
            debug=True)
