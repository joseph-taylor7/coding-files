
import sqlite3
from flask import Flask, render_template, request, redirect, flash, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash





app = Flask(__name__)
app.secret_key = "super-secret-key"

def get_database():
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
@app.route("/home")
@app.route("/")
def home():
    if "user_id" in session:

        return render_template("home.html",logged_in=True,name=session["user_name"],lname=session["user_lname"],id=session["user_id"],letter = session["user_name"][0].upper(), email=session["user_email"])

    return render_template("home.html", logged_in=False)

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password)


        conn = get_database()
        cursor = conn.cursor()

        cursor.execute("Select 1 from users where email = ?", (email,))

        exist_email = cursor.fetchone()
        if exist_email:
            flash("Email already exists", "error")
            return redirect(url_for("signup"))

        cursor.execute("Insert into users(fname, lname, email, password) values(?,?,?,?);", (fname, lname,email,hashed_password))
        conn.commit()
        conn.close()
        flash("Account Created Successfully", "success")
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = get_database()
        cursor = conn.cursor()

        cursor.execute("select * from users where email = ?", (email,))
        user = cursor.fetchone()

        
        if user is None:
            flash("User doesn't exist", "error")
            return redirect(url_for("login"))

        stored_hash = user["password"]
        if not check_password_hash(stored_hash, password):
            flash("Password incorrect", "error")
            return redirect(url_for("login"))

        session["user_id"] = user["id"]
        session["user_name"] = user["fname"]
        session["user_lname"] = user["lname"]
        session["user_email"] = user["email"]

        flash("Logged in succefully", "success")
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("home")

if __name__ == "__main__":
    app.run(debug=True)

