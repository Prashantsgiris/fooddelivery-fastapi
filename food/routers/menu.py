from fastapi import APIRouter, Depends,status
from food import schemas, database
from ..repository import menu
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(
   tags=["MENU"]
)


get_db = database.get_db


@router.get('/',response_model=List[schemas.ShowMenu])
def all(db:Session = Depends(get_db)):
    return menu.get_all(db)


