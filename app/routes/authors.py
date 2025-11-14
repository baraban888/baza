# app/routes/authors.py
from flask import render_template, request, redirect, url_for
from app import db
from app.models import Author
from . import bp


@bp.route("/authors")
def list_authors():
    """Список авторов"""
    authors = Author.query.order_by(Author.name).all()
    return render_template("authors/list.html", authors=authors)


@bp.route("/authors/add", methods=["GET", "POST"])
def add_author():
    """Добавление автора"""
    if request.method == "POST":
        name = request.form.get("name", "").strip()

        if not name:
            error = "Imię autora jest wymagane."
            return render_template("authors/add.html", error=error)

        # Проверяем, нет ли автора с таким именем
        existing = Author.query.filter_by(name=name).first()
        if existing:
            error = "Autor o takim imieniu już istnieje."
            return render_template("authors/add.html", error=error)

        author = Author(name=name)
        db.session.add(author)
        db.session.commit()
        return redirect(url_for("main.list_authors"))

    # GET-запрос — просто показываем форму
    return render_template("authors/add.html")
