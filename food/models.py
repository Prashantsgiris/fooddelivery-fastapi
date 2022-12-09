from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship

class Menu(Base):
    __tablename__ = "MENU"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Integer)

class loginowner(Base):
    __tablename__ = "Owner"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String,unique=True)
    email = Column(String)
    password = Column(String)


class orders(Base):
    __tablename__ = "Orders"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    quantity = Column(Integer,nullable=False)


class logincustomer(Base):
    __tablename__ = "Customer"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

class logindelivery(Base):
    __tablename__ = "Delivery"
    id = Column(Integer, primary_key= True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)








