# app/routes/loans.py
from datetime import datetime

from flask import render_template, request, redirect, url_for

from app.routes import bp           # наш blueprint "main"
from app.models import Loan, Book   # модели
from app import db                  # объект БД


@bp.route("/loans")
def list_loans():
    """
    Список выдач.
    Активные (не возвращённые) — сверху,
    затем уже возвращённые, по дате выдачи.
    """
    loans = (
        Loan.query
        .order_by(
            Loan.returned_at.is_(None).desc(),  # True > False → активные сверху
            Loan.borrowed_at.desc()
        )
        .all()
    )
    return render_template("loans/list.html", loans=loans)


@bp.route("/loans/add", methods=["GET", "POST"])
def add_loan():
    """
    Создание новой выдачи книги.
    GET  → показать форму
    POST → сохранить выдачу, если всё ок
    """
    if request.method == "POST":
        book_id = request.form.get("book_id")
        borrower = request.form.get("borrower", "").strip()
        due_at_str = request.form.get("due_at")

        if book_id and borrower:
            # ID книги → int
            book_id = int(book_id)

            # Проверяем, не выдана ли книга уже
            active_loan = Loan.query.filter_by(book_id=book_id, returned_at=None).first()
            if active_loan:
                books = (
                    Book.query
                    .filter_by(on_shelf=True)
                    .order_by(Book.title)
                    .all()
                )
                error = "Ta książka jest już wypożyczona!"
                return render_template("loans/add.html", books=books, error=error)

            # Срок возврата (если указан)
            due_at = None
            if due_at_str:
                try:
                    # input type="date" → формат YYYY-MM-DD
                    due_at = datetime.fromisoformat(due_at_str)
                except ValueError:
                    pass

            # Создаём выдачу
            loan = Loan(book_id=book_id, borrower=borrower, due_at=due_at)
            db.session.add(loan)
            db.session.commit()

            return redirect(url_for("main.list_loans"))

    # --- GET: показываем форму выдачи ---
    books = (
        Book.query
        .filter_by(on_shelf=True)
        .order_by(Book.title)
        .all()
    )
    return render_template("loans/add.html", books=books, error=None)
