from fastapi import APIRouter, Depends
from food import database, models
from sqlalchemy.orm import Session




get_db = database.get_db

router = APIRouter(
    tags=["bill"]

)






