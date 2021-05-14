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

# 

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


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
    if request.method == "POST":
        book = {
            "genre_name": request.form.get("genre_name"),
            "book_name": request.form.get("book_name"),
            "book_description": request.form.get("book_description"),
            "book_author": request.form.get("book_author"),
            "book_image": request.form.get("book_image"),
            "number_pages": request.form.get("number_pages"),
            "isbn": request.form.get("isbn"),
            "rating": request.form.get("rating"),
            "created_by": session["user"]
        }
        mongo.db.books.insert_one(book)
        flash("Book Successfully Added")
        return redirect(url_for("get_books"))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("add_book.html", genres=genres)

# Edit book (only for the ones added by the user)

@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name"),
            "book_name": request.form.get("book_name"),
            "book_description": request.form.get("book_description"),
            "book_author": request.form.get("book_author"),
            "book_image": request.form.get("book_image"),
            "number_pages": request.form.get("number_pages"),
            "isbn": request.form.get("isbn"),
            "rating": request.form.get("rating"),
            "created_by": session["user"]
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, submit)
        flash("Book Successfully Updated")

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("edit_book.html", book=book, genres=genres)

# Delete book (only the ones added by the user) 

@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash("Book Successfully Deleted")
    return redirect(url_for("get_books"))

# Get genres

@app.route("/get_genres")
def get_genres():
    genres = list(mongo.db.genres.find().sort("genre_name", 1))
    return render_template("genres.html", genres=genres)

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

# Delete Genre (only adming)

@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    mongo.db.genres.remove({"_id": ObjectId(genre_id)})
    flash("Genre Successfully Deleted")
    return redirect(url_for("get_genres"))


# Open book page.

@app.route("/book_page/<book_id>", methods=["GET", "POST"])
def book_page(book_id):
    """
    Get the book details for the selected book and
    render the the Book Page template.
    """
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("book_page.html", book=book)


# Add Favorite 

@app.route("/add_favorite/<favorite_id>")
def add_favorite(favorite_id):
    # Allows the user to add a book review for their favorite section
    if session["user"]:
        # grab the session user's details from db
        username = mongo.db.users.find_one(
            {"username": session["user"]})

        # grab the book review details
        book = mongo.db.book_review.find_one(
            {"_id": ObjectId(favorite_id)})

        # Collect the favorites object data
        favorites = {
            "book_review_id": book["_id"],
            "book_name": book["book_name"],
            "book_author": book["book_author"],
            "genre": book["genre_name"]
        }

        # update the user document favorites array
        mongo.db.users.update_one(
            {"_id": ObjectId(username["_id"])},
            {"$push": {"favorites": favorites}})

        flash(
            "Favorite book added to your profile",
            "teal-text text-darken-2 teal lighten-5")
        return redirect(url_for("book_page", book_id=book["_id"]))

    # Display for users that are not logged in.
    else:
        flash(
            "To add favorites, please register",
            "red-text text-darken-2 red lighten-4")
        return redirect(url_for("book_page", book_id=book["_id"]))



@app.route("/add_comment/<comment_id>", methods=["GET", "POST"])
def add_comment(comment_id):
    """
    Allows the user to add comments to a book review page.
    Writes the comment to the specific book_review document.
    """
    if request.method == "POST":
        # collect the add-comment form data and write to MongoDB
        new_comment = {
            "text": request.form.get("comment"),
            "created_by": session["user"],
        }

        mongo.db.book_review.update_one(
                    {"_id": ObjectId(comment_id)},
                    {"$push": {"comments": new_comment}})

        flash(
            "New Comment Added",
            "teal-text text-darken-2 teal lighten-5")
        return redirect(url_for("book_page", book_id=comment_id))

    comments = mongo.db.book_review.find_one({"_id": ObjectId(comment_id)})
    return render_template("add-comment.html", comments=comments)





if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)