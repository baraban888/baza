 # app/models.py
from datetime import datetime
from . import db

# --- связь многие-ко-многим между книгами и авторами ---
book_author = db.Table(
    "book_author",
    db.Column("author_id", db.Integer, db.ForeignKey("author.id"), primary_key=True),
    db.Column("book_id", db.Integer, db.ForeignKey("book.id"), primary_key=True),
)

# --- Автор ---
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)

    books = db.relationship(
        "Book",
        secondary=book_author,
        back_populates="authors",
        lazy="selectin"
    )

    def __repr__(self):
        return f"<Author {self.name!r}>"

# --- Книга ---
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, index=True)
    isbn = db.Column(db.String(32), unique=True, index=True)
    on_shelf = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    authors = db.relationship(
        "Author",
        secondary=book_author,
        back_populates="books",
        lazy="selectin"
    )

    loans = db.relationship(
        "Loan",
        back_populates="book",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Book {self.title!r}>"

# --- Выдача книги ---
class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    borrower = db.Column(db.String(128), nullable=False)  # кто взял
    borrowed_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    due_at = db.Column(db.DateTime, nullable=True)        # срок возврата
    returned_at = db.Column(db.DateTime, nullable=True)   # когда вернули

    book = db.relationship("Book", back_populates="loans")

    @property
    def is_active(self) -> bool:
        return self.returned_at is None

    def __repr__(self):
        status = "active" if self.is_active else "returned"
        return f"<Loan book_id={self.book_id} borrower={self.borrower!r} {status}>"
