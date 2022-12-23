from food import schemas,models, hashing,database
from sqlalchemy.orm import Session
from fastapi import HTTPException,status,Depends
from food.hashing import Hash
get_db = database.get_db


def show_delivery(db:Session):
    show = db.query(models.logindelivery).all()
    return show
