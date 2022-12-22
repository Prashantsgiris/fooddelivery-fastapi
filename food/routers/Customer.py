from fastapi import APIRouter, Depends
from food import schemas, database
from ..repository import Customer
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT





get_db = database.get_db

router = APIRouter(
    tags = ['Customer']
)



@router.post('/create_customer')
def create_customer(request:schemas.logincustomer, db:Session=Depends(get_db)):
    return Customer.create_customer(db,request)




@router.put('/PlaceOrder')
def placeorder(request:schemas.orders, db: Session = Depends(get_db)):
    return Customer.placeorder(db,request)


#order route













