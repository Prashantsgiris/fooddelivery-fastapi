from fastapi import FastAPI
from .database import engine
from food import models
from .routers import menu,Customer,Owner,Delivery,bill






app  = FastAPI()





models.Base.metadata.create_all(engine)

app.include_router(menu.router)
app.include_router(bill.router)
app.include_router(Customer.router)
app.include_router(Owner.router)
app.include_router(Delivery.router)



