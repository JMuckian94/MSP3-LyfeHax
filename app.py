import os
from flask import (Flask, render_template, redirect, request, url_for, session,
                   flash)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    """
    Returns user to the landing page
    """
    return render_template("pages/index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    Allows user to register for an account
    Checks if a username is already in use
    Forwards user onto their new member dashboard
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already in use")
            return redirect(url_for("signup"))

        username = request.form.get("username").lower()
        password = generate_password_hash(request.form.get("password"))

        mongo.db.users.insert_one({
            'username': username,
            'password': password})

        if mongo.db.users.find_one({'username': username}) is not None:
            user = mongo.db.users.find_one({'username': username})
            user_id = user['_id']
            session['user_id'] = str(user_id)
            return redirect(url_for("dashboard", user_id=user_id))

    return render_template("pages/signup.html", register="True")


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
                user_id = str(user['_id'])
                session['user_id'] = str(user_id)

            else:
                flash("Incorrect Username and/or password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("pages/login.html")


@app.route('/logout')
def logout():
    """
    Allows the user to log out
    Takes them back to the home page
    """
    session.clear()
    return render_template("pages/index.html")


@app.route('/hax')
def hax():
    """
    Takes user to the lifehacks page
    """
    return render_template("pages/hax.html")


@app.route('/dashboard/<user_id>')
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
    return render_template('pages/error.html',
                           error_message=error_message), 404


@app.errorhandler(500)
def server_error(error):
    """
    Renders error.html with 500 message.
    """
    error_message = str(error)
    return render_template('pages/error.html',
                           error_message=error_message), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
