import schemas,models, hashing
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash,check_password_hash
from fastapi import HTTPException,status

def create_delivery(db:Session, request:schemas.logindelivery):
    check = db.query(models.logindelivery).filter(models.logindelivery.username == request.username or models.logindelivery.email == request.email).first()
    if check is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f'Try unique username and email already')
    new_delivery= models.logindelivery(username = request.username, email = request.email, password = generate_password_hash(request.password))
    db.add(new_delivery)
    db.commit()
    db.refresh(new_delivery)
    return new_delivery

def show_delivery(db:Session):
    show = db.query(models.logindelivery).all()
