from food import schemas,models, hashing,database
from sqlalchemy.orm import Session
from fastapi import HTTPException,status,Depends
from food.hashing import Hash
get_db = database.get_db


def create_delivery(db:Session, request:schemas.logindelivery):
    check = db.query(models.logindelivery).filter(models.logindelivery.username == request.username or models.logindelivery.email == request.email).first()
    if check is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f'Try unique username and email already')
    new_delivery= models.logindelivery(username = request.username, email = request.email, password = hashing.Hash.bcrypt(request.password))
    db.add(new_delivery)
    db.commit()
    db.refresh(new_delivery)
    return new_delivery

def login(request:schemas.login,db:Session=Depends(get_db)):
    user = db.query(models.logindelivery).filter(models.logindelivery.username == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Incorrect password")
    return user



def show_delivery(db:Session):
    show = db.query(models.logindelivery).all()
