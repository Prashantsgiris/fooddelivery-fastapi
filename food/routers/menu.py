from fastapi import APIRouter, Depends
from food import schemas, database, models
from ..repository import menu
from typing import List
from sqlalchemy.orm import Session
from food import oauth2,schemas

router = APIRouter(
       tags=["MENU"]

)


get_db = database.get_db


@router.get('/menu',response_model=List[schemas.ShowMenu])
def get_all(db: Session = Depends(get_db)):
    menu = db.query(models.Menu).all()
    return menu


@router.post('/create_menu')
def create_menu(request:schemas.Menu, db:Session = Depends(get_db), current_user: schemas.loginowner = Depends(oauth2.get_current_user)):
    return menu.create(request, db)


