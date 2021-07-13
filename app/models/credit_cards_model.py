from sqlalchemy import Column,String,Boolean,Integer
from sqlalchemy.sql.schema import ForeignKey
from . import db
from sqlalchemy.orm import relationship, backref


class CreditCard(db.Model):
    __tablename__= "credit_cards"

    id = Column(Integer, primary_key=True)

    expire_date = Column(String, nullable=False)
    number = Column(String, nullable=False, unique=True)
    provider = Column(String(50), nullable=False)
    security_code = Column(String(3), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))

    usuarios = relationship("Users", backref=backref("credit_card"))
