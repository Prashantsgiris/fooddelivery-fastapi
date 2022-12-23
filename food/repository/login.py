from food import schemas,models, database,token
from sqlalchemy.orm import Session
from fastapi import HTTPException,status,Depends
from food import hashing
from fastapi.security import OAuth2PasswordRequestForm

get_db = database.get_db



def create_owner(db:Session, request:schemas.loginowner):
    check = db.query(models.loginowner).filter(models.loginowner.username == request.username or models.loginowner.email == request.email).first()
    if check is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail=f'Try unique username and email already '
        )
    new_owner = models.loginowner(username= request.username,email = request.email, password =hashing.Hash.bcrypt(request.password))
    db.add(new_owner)
    db.commit()
    db.refresh(new_owner)
    return new_owner


def create_customer(db: Session, request: schemas.logincustomer):
    check = db.query(models.logincustomer).filter(models.logincustomer.username == request.username or models.logincustomer.email == request.email).first()
    if check is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Try unique username and email already ')
    new_customer = models.logincustomer(username = request.username,email = request.email, password = hashing.Hash.bcrypt(request.password))
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer


def create_delivery(db:Session, request:schemas.logindelivery):
    check = db.query(models.logindelivery).filter(models.logindelivery.username == request.username or models.logindelivery.email == request.email).first()
    if check is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f'Try unique username and email already')
    new_delivery= models.logindelivery(username = request.username, email = request.email, password = hashing.Hash.bcrypt(request.password))
    db.add(new_delivery)
    db.commit()
    db.refresh(new_delivery)
    return new_delivery











