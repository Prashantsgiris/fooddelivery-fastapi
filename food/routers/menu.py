from fastapi import APIRouter, Depends
from food import schemas, database
from ..repository import menu
from typing import List
from sqlalchemy.orm import Session
from food import oauth2,schemas

router = APIRouter(
       tags=["MENU"]

)


get_db = database.get_db


@router.get('/menu',response_model=List[schemas.ShowMenu])
def show_menu(db:Session = Depends(get_db)):
    return menu.get_all(db)

@router.post('/create_menu')
def create_menu(request:schemas.Menu, db:Session = Depends(get_db)):
    return menu.create(request, db)


