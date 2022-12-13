from fastapi import APIRouter, Depends
from food import database, models, schemas
from sqlalchemy.orm import Session
from typing import List
from ..repository import bill


get_db = database.get_db

router = APIRouter(

)

@router.get('/', response_model=List[schemas.orders])
def show(db:Session = Depends(get_db)):
    return bill.orders(db)