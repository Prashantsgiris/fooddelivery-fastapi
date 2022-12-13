from sqlalchemy.orm import Session
from food import models

def orders(db:Session):
    orders = db.query(models.orders).all()
    return orders