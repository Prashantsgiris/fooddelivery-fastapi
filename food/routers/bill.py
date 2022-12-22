from fastapi import APIRouter, Depends
from food import database, models
from sqlalchemy.orm import Session




get_db = database.get_db

router = APIRouter(
    tags=["bill"]

)


@router.get('/receipt')
def receipt(db:Session = Depends(get_db)):
    orders = db.query(models.orders).all()
    bill = 0
    x=0
    for x in range(1, 10):
        take = db.query(models.orders).filter(models.orders.id == x).first()
        if take:
            bill += take.price

    remove = db.query(models.orders).filter(models.orders.id > 0)
    if not remove:
        return {'error'}
    remove.delete()
    db.commit()



    return {'orders':orders,'Bill':bill}



