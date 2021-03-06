from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.user_model import Users
    from app.models.credit_cards_model import CreditCard

