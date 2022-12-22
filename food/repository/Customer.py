from sqlalchemy.orm import Session
from food import models, schemas, hashing, database
from fastapi import HTTPException,status, Depends
from food.hashing import Hash

get_db = database.get_db

def create_customer(db: Session, request: schemas.logincustomer):
    check = db.query(models.logincustomer).filter(models.logincustomer.username == request.username or models.logincustomer.email == request.email).first()
    if check is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Try unique username and email already ')
    new_customer = models.logincustomer(username = request.username,email = request.email, password = hashing.Hash.bcrypt(request.password))
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

def login_as_Customer(request: schemas.login, db:Session = Depends(get_db)):
    user = db.query(models.logincustomer).filter(models.logincustomer.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Incorrect Password")
    return user

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

