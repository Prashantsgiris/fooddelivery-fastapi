from sqlalchemy.orm import Session
from food import models, schemas,hashing,database
from fastapi import HTTPException,status,Depends
from food.hashing import Hash

get_db = database.get_db


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








