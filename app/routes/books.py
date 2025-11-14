# app/routes/books.py
from flask import render_template, request, redirect, url_for
from app.routes import bp
from app.models import Book
from app import db
from app.models import Author
from sqlalchemy.exc import IntegrityError

@bp.route("/")
def index():
    # просто перенаправляем на список книг
    return redirect(url_for("main.list_books"))


@bp.route("/books")
def list_books():
    books = Book.query.order_by(Book.title).all()
    return render_template("books/list.html", books=books)

@bp.route("/books/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form.get("title")
        isbn = request.form.get("isbn", "")
        on_shelf = "on_shelf" in request.form

        book = Book(title=title, isbn=isbn, on_shelf=on_shelf)

        try:
            db.session.add(book)
            db.session.commit()
            return redirect(url_for('main.list_books'))
        except IntegrityError:
            db.session.rollback()
            error = "Książka z takim numerem ISBN już istnieje!"
            return render_template("books/add.html", error=error)

    return render_template("books/add.html")


    
