from application import app, db
from application.models import Book, Users
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db.create_all()
@app.route('/user', methods=["GET","POST"])
def user_home():
    if request.form:
        user_db = Users(user_name=request.form.get("user_name"), user_email=request.form.get("user_email"), start_date = request.form.get("start_date"), book_id=request.form.get("book_id"))
        db.session.add(user_db)
        db.session.commit()
    user_data = Users.query.all()
    return render_template("user.html", user_data=user_data)

@app.route("/update_user", methods=["POST"])
def update_user():
    user_db = Users.query.filter_by(id=request.form.get("id")).first()
    user_db.user_name = request.form.get("new_user_name")
    user_db.user_email = request.form.get("new_user_email")
    user_db.start_date = request.form.get("new_start_date")
    db.session.commit()
    return redirect("/user")

@app.route("/delete_user", methods=["POST"])
def delete_user():
    user_db = Users.query.filter_by(id=request.form.get("id")).first()
    db.session.delete(user_db)
    db.session.commit()
    return redirect("/user")

###########################################################################################

@app.route('/', methods=["GET","POST"])
def home():
    if request.form:
        book_db = Book(book_title=request.form.get("book_title"), author=request.form.get("author"))
        db.session.add(book_db)
        db.session.commit()
    book_lists = Book.query.all()
    return render_template("index.html", book_lists=book_lists)

###########################################################################################

@app.route("/book_update", methods=["GET", "POST"])
def book_update():
    if request.form:
        book_db = Book(book_title=request.form.get("book_title"), author=request.form.get("author"))
        db.session.add(book_db)
        db.session.commit()
    book_lists = Book.query.all()
    return render_template("book_update.html", book_lists=book_lists)

@app.route("/update", methods=["POST"])
def update():
    book_db = Book.query.filter_by(book_title=request.form.get("current_book_title")).first()
    book_db.book_title = request.form.get("newbook_title")
    book_db.author = request.form.get("new_author")
    
    db.session.commit()
    return redirect("/book_update")

@app.route("/delete", methods=["POST"])
def delete():
    book_db = Book.query.filter_by(book_title=request.form.get("book_title")).first()
    db.session.delete(book_db)
    db.session.commit()
    return redirect("/book_update")