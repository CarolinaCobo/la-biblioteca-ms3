import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
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
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/get_books")
def get_books():
    books = mongo.db.books.find()
    return render_template("books.html", books=books)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books = mongo.db.books.find({"$text": {"$search": query}})
    return render_template("books.html", books=books)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "name": request.form.get("username").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Look for the username name on the DB
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    try:
        # grab the session user's username from db
        user = mongo.db.users.find_one(
            {"username": session["user"]})

        user_books = list(mongo.db.books.find(
            {"created_by": session["user"]}))

        return render_template("profile.html",
                               user=user,
                               user_books=user_books)

    except Exception:
        flash("Please log in first!")
        return redirect(url_for("login"))


# Logout
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Add book
@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    try:
        if session["user"]:
            if request.method == "POST":
                book = {
                    "genre_name": request.form.get("genre_name"),
                    "book_name": request.form.get("book_name"),
                    "book_description": request.form.get("book_description"),
                    "book_author": request.form.get("book_author"),
                    "book_image": request.form.get("book_image"),
                    "number_pages": request.form.get("number_pages"),
                    "isbn": request.form.get("isbn"),
                    "created_by": session["user"]
                }
                mongo.db.books.insert_one(book)
                flash("Book Successfully Added")
                return redirect(url_for("get_books"))

            genres = mongo.db.genres.find().sort("genre_name", 1)
            return render_template("add_book.html", genres=genres)

    except Exception:
        flash(
            "Please log in first")
        return redirect(url_for("login"))


# Update book details (only for the ones added by the user)
@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    try:
        if session["user"]:
            if request.method == "POST":
                submit = {
                    "genre_name": request.form.get("genre_name"),
                    "book_name": request.form.get("book_name"),
                    "book_description": request.form.get("book_description"),
                    "book_author": request.form.get("book_author"),
                    "book_image": request.form.get("book_image"),
                    "number_pages": request.form.get("number_pages"),
                    "isbn": request.form.get("isbn"),
                    "created_by": session["user"]
                }
                mongo.db.books.update({"_id": ObjectId(book_id)}, submit)
                flash("Book Successfully Updated")
                return redirect(url_for("get_books"))


            book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
            genres = mongo.db.genres.find().sort("genre_name", 1)
            return render_template("edit_book.html", book=book, genres=genres)

    except Exception:
        flash(
            "Please log in first")
        return redirect(url_for("login"))


# Delete book (only the ones added by the user)
@app.route("/delete_book/<book_id>")
def delete_book(book_id):
     try:
        if session["user"]:
            mongo.db.books.remove({"_id": ObjectId(book_id)})
            flash("Book Successfully Deleted")
            return redirect(url_for("get_books"))
     except Exception:
        flash(
            "Please log in first")
        return redirect(url_for("login"))

# Get genres
@app.route("/get_genres")
def get_genres():
    try:
        if session["user"]:
            genres = list(mongo.db.genres.find().sort("genre_name", 1))
            print(genres)
            return render_template("genres.html", genres=genres)

    except Exception:
        flash(
            "Please log in first")
        return redirect(url_for("login"))

# Add genre (only admin)
@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    if request.method == "POST":
        genre = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.insert_one(genre)
        flash("New Genre Added")
        return redirect(url_for("get_genres"))

    return render_template("add_genre.html")


# Edit Genre (only admin)
@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.update({"_id": ObjectId(genre_id)}, submit)
        flash("Genre Successfully Updated")
        return redirect(url_for("get_genres"))

    genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
    return render_template("edit_genre.html", genre=genre)


# Delete Genre (only admin)
@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    mongo.db.genres.remove({"_id": ObjectId(genre_id)})
    flash("Genre Successfully Deleted")
    return redirect(url_for("get_genres"))


# Open book page
@app.route("/book_page/<book_id>", methods=["GET", "POST"])
def book_page(book_id):
    # Get the book details for the selected book and render
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("book_page.html", book=book)


# Add Favorite
@app.route("/add_favorite/<favorites_id>")
def add_favorite(favorites_id):
    # Allows the user to add a book review for their favorite section
    if "user" in session:
        print("here")
        # grab the session user's details from db
        username = mongo.db.users.find_one(
            {"username": session["user"]})

        # grab the book details
        book = mongo.db.books.find_one(
            {"_id": ObjectId(favorites_id)})

        # Collect the favorite object data
        favorite = {
            "book_id": book["_id"],
            "book_name": book["book_name"],
            "book_author": book["book_author"],
            "genre_name": book["genre_name"]
        }

        # update the user document favorites array
        mongo.db.users.update_one(
            {"_id": ObjectId(username["_id"])},
            {"$push": {"favorite": favorite}})

        flash(
            "Favorite book added to your profile")
        return redirect(url_for("book_page", book_id=book["_id"]))

    # Display for users that are not logged in.
    else:
        book = mongo.db.books.find_one(
            {"_id": ObjectId(favorites_id)})
        flash("To add favorites, please register")
        return redirect(url_for("book_page", book_id=book["_id"]))


# Add comment
@app.route("/add_comment/<book_id>", methods=["GET", "POST"])
def add_comment(book_id):
    if request.method == "POST":
        # collect the add-comment form data and write to the DB
        new_comment = {
            "_id": ObjectId(),
            "comment": request.form.get("comment"),
            "created_by": session["user"]
        }
        mongo.db.books.update_one(
            {"_id": ObjectId(book_id)},
            {"$push": {"comments": new_comment}})

        flash("New Comment Added")
        return redirect(url_for("book_page", book_id=book_id))
    return render_template("add_comment.html", book_id=book_id)

# Delete comment


@app.route("/delete_comment/<book_id>/<comment_id>")
def delete_comment(book_id, comment_id):
    try:
        if session["user"]:
            mongo.db.books.update_one(
                {"_id": ObjectId(book_id)},
                {"$pull": {"comments": {"_id": ObjectId(comment_id)}}})

            flash("Comment Successfully Removed")
            return redirect(url_for("book_page", book_id=book_id))
    
    except Exception:
        flash(
            "Please log in first")
        return redirect(url_for("login"))


# Error handling
@app.errorhandler(404)
def not_found(error):
   
    return render_template("error-404.html", error=error)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
