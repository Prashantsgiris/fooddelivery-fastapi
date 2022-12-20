from sqlalchemy.orm import Session
from food import models
from ..models import orders

def order(db:Session):
    orders = db.query(models.orders).all()
    remove = db.query(models.orders).filter(models.orders.id > 0)
    if not remove:
        return {'error'}
    remove.delete()
    db.commit()

    return orders

