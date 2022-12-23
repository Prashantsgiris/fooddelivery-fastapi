from sqlalchemy.orm import Session
from food import models,schemas,oauth2
from fastapi import Depends




def get_all(db:Session):
    menu = db.query(models.Menu).all()
    return menu

def create(request: schemas.Menu, db: Session):
    new_menu = models.Menu( title = request.title, price = request.price, user_id = request.user_id)
    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)
    return new_menu



