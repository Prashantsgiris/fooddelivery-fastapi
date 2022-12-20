from fastapi import APIRouter, Depends
from food import database, models, schemas
from sqlalchemy.orm import Session
from typing import List
from ..repository import bill


get_db = database.get_db

router = APIRouter(
    tags=["bill"]

)

@router.get('/bills', response_model=List[schemas.showorders])
def show(request:schemas.orders,db:Session = Depends(get_db)):
    return bill.order(db, request)