from fastapi import APIRouter,Depends
from food import schemas, database
from sqlalchemy.orm import Session
from ..repository import Delivery



get_db = database.get_db


router = APIRouter(
    tags=['DELIVERY']
)

@router.post('/signup_for_delivery')
def create_delivery(request:schemas.logindelivery, db:Session = Depends(get_db)):
    return Delivery.create_delivery(db,request)

@router.post('/login_as_delivery')
def login(request:schemas.login,db:Session =Depends(get_db)):
    return Delivery.login(request,db)