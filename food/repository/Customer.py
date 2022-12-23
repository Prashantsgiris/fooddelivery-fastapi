from sqlalchemy.orm import Session
from food import models, schemas, hashing, database
from fastapi import HTTPException,status, Depends
from food.hashing import Hash

get_db = database.get_db


def show_customer(db:Session):
    show_customer = db.query(models.logincustomer).all()
    return show_customer

def placeorder(db:Session, request: schemas.orders):
    def price():
        check = db.query(models.Menu).filter(models.Menu.title == request.title).first()
        if check:
            bill = request.quantity * check.price
            return bill
    order = models.orders(title=request.title,quantity= request.quantity,price=price())
    db.add(order)
    db.commit()
    return {'title':request.title,'quantity':request.quantity,'price':price()}

