from flask import Flask
from .models import db
from .routes.books_route import books_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Inicializar a extensão SQLAlchemy
    db.init_app(app)

    # Registrar o Blueprint
    app.register_blueprint(books_bp, url_prefix='/books')

    return app
