# app/routes/__init__.py
from flask import Blueprint

bp = Blueprint("main", __name__)

# импортируем обработчики, чтобы они зарегистрировались на bp
from app.routes import books, authors, loans  # noqa: E402,F401
