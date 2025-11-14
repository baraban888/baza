# app/services/loans.py
from datetime import datetime
from app.models import db, Book, Loan

def issue_loan(book_id: int, borrower: str) -> Loan:
    book = Book.query.get_or_404(book_id)
    if book.available_copies <= 0:
        raise ValueError("Немає доступних примірників")
    loan = Loan(book_id=book.id, borrower=borrower)
    db.session.add(loan)
    db.session.commit()
    return loan

def return_loan(loan_id: int) -> Loan:
    loan = Loan.query.get_or_404(loan_id)
    if loan.returned_at:
        return loan
    loan.returned_at = datetime.utcnow()
    db.session.commit()
    return loan
