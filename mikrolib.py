from app import create_app
from app.models import db, Book, Author, Loan

app = create_app()

@app.shell_context_processor
def make_ctx():
    return {"db": db, "Book": Book, "Author": Author, "Loan": Loan}
