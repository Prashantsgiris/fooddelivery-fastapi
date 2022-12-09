from sqlalchemy.orm import Session
import models



def get_all(db:Session):
    menu = db.query(models.Menu).all()
    return menu





