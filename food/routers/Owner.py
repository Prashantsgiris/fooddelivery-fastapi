from fastapi import APIRouter, Depends,status
from food import schemas, database,oauth2
from ..repository import Owner
from sqlalchemy.orm import Session
from typing import List
from ..repository import Customer, Delivery





get_db = database.get_db
router = APIRouter(
    tags=["OWNER"]
)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def remove_menu_item(id, db:Session=Depends(get_db),current_user: schemas.loginowner = Depends(oauth2.get_current_user)):
    return Owner.delete(id,db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request:schemas.Menu, db:Session = Depends(get_db),current_user: schemas.loginowner = Depends(oauth2.get_current_user)):
    return Owner.update(db,id,request)



@router.get('/show_customer', response_model=List[schemas.showlogincustomer])
def show_costomer(db:Session = Depends(get_db),current_user: schemas.loginowner = Depends(oauth2.get_current_user)):
    return Customer.show_customer(db)

@router.get('/show_delivery', response_model=List[schemas.showlogindelivery])
def show_delivery(db:Session = Depends(get_db),current_user: schemas.loginowner = Depends(oauth2.get_current_user)):
    return Delivery.show_delivery(db)

@router.delete('/{id}/remove_owner',status_code=status.HTTP_204_NO_CONTENT)
def remove_owner(id,db:Session = Depends(get_db),current_user: schemas.loginowner = Depends(oauth2.get_current_user)):
    return Owner.remove_owner(id,db)

@router.delete('/{id}/remove_customer', status_code=status.HTTP_204_NO_CONTENT)
def remove_customer(id,db:Session = Depends(get_db),current_user: schemas.loginowner = Depends(oauth2.get_current_user)):
    return Owner.remove_customer(id,db)

@router.delete('/{id}/remove_delivery',status_code=status.HTTP_204_NO_CONTENT)
def remove_delivery(id,db:Session = Depends(get_db),current_user: schemas.loginowner = Depends(oauth2.get_current_user)):
    return Owner.remove_delivery(id,db)




