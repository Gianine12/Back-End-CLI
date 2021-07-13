from sqlalchemy import Column,String,Boolean,Integer
from . import db
from werkzeug.security import generate_password_hash

class Users(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    login = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    password_has = Column(String)


    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_has = generate_password_hash(password_to_hash)