from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException,status
from werkzeug.security import generate_password_hash,check_password_hash




def create_owner(db:Session, request:schemas.loginowner):
    check = db.query(models.loginowner).filter(models.loginowner.username == request.username or models.loginowner.email == request.email).first()
    if check is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail=f'Try unique username and email already '
        )
    new_owner = models.loginowner(username= request.username,email = request.email, password =generate_password_hash(request.password))
    db.add(new_owner)
    db.commit()
    db.refresh(new_owner)
    return new_owner



def create(request: schemas.Menu, db: Session):
    new_menu = models.Menu( title = request.title, price = request.price)
    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)
    return new_menu















def delete(id, db:Session):
    remove = db.query(models.Menu).filter(models.Menu.id == id)
    if not remove.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Item with id {id} not found'
        )
    remove.delete(synchronize_session=False)
    db.commit()
    return {'Item Removed'}

def update(db:Session,id,request: schemas.Menu):
    Item = db.query(models.Menu).filter(models.Menu.id == id)
    if not Item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Item with id {id} not found")
    Item.update({'title' : request.title, 'price' : request.price})
    db.commit()
    return {'Updated'}



def remove_owner(id,db:Session):
    owner = db.query(models.loginowner).filter(models.loginowner.id == id)
    if not owner.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Item with id {id} not found")
    owner.delete(synchronize_session = False)
    db.commit()
    return {'Owner Removed'}

def remove_customer(id,db:Session):
    customer = db.query(models.logincustomer).filter(models.logincustomer.id==id)
    if not customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with id {id} not found")
    customer.delete(synchronize_session=False)
    db.commit()
    return {'Customer Removed'}


def remove_delivery(id, db:Session):
    delivery = db.query(models.logindelivery).filter(models.logindelivery. id == id)
    if not delivery.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with id {id} not found")
    delivery.delete(synchronize_session=False)
    db.commit()
    return {'Delivery Removed'}








