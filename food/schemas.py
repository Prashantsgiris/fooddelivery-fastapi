from pydantic import BaseModel
from typing import Optional




class orders(BaseModel):
    title : str
    quantity : int


class Menu(BaseModel):
    title: str
    price: int


class ShowMenu(BaseModel):
    title: str
    price: int

    class Config():
        orm_mode = True


class loginowner(BaseModel):
    username: str
    email: str
    password: str


class logincustomer(BaseModel):
    username: str
    email: str
    password: str


class logindelivery(BaseModel):
    username: str
    email: str
    password: str


class showlogincustomer(BaseModel):
    username: str
    password: str

    class Config():
        orm_mode = True




class showlogindelivery(BaseModel):
    username: str
    password: str

    class Config():
        orm_mode = True



