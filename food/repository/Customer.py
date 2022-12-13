from sqlalchemy.orm import Session
from food import models, schemas, hashing
from fastapi import HTTPException,status
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List

def create_customer(db:Session, request: schemas.logincustomer):
    check = db.query(models.logincustomer).filter(models.logincustomer.username == request.username or models.logincustomer.email == request.email).first()
    if check is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Try unique username and email already ')
    new_customer= models.logincustomer(username = request.username,email = request.email, password = generate_password_hash(request.password))
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

def show_customer(db:Session):
    show_customer = db.query(models.logincustomer).all()
    return show_customer

def placeorder(db:Session, request: schemas.orders):
    order = models.orders(title=request.title,quantity= request.quantity)
    db.add(order)
    db.commit()
    check = db.query(models.Menu).filter(models.Menu.title == request.title).first()
    if check:
        if request.title == "Veg Momo":
            bill = request.quantity * 160
            return {'order': request.title, 'quantity': request.quantity, 'Bill': bill}
        elif request.title == "Chicken Momo":
            bill = request.quantity * 200
            return {'order': request.title, 'quantity': request.quantity, 'Bill': bill}
        elif request.title == "Mutton Momo":
            bill = request.quantity * 300
            return {'order': request.title, 'quantity': request.quantity, 'Bill': bill}


    db.commit()
    return order



