from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# создаём экземпляры, но не подключаем сразу
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # инициализация
    db.init_app(app)
    migrate.init_app(app, db)
# импортируем и регистрируем blueprint
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)
    # импорт внутри функции — после инициализации
    from app import models

    return app

