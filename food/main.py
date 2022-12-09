from fastapi import FastAPI
from database import engine
import models
from routers import menu,Customer,Owner,Delivery






app  = FastAPI()





models.Base.metadata.create_all(engine)

app.include_router(menu.router)

app.include_router(Customer.router)
app.include_router(Owner.router)
app.include_router(Delivery.router)

