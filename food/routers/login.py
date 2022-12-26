from fastapi import APIRouter,Depends, HTTPException,status
from food import schemas, database,models, token, oauth2
from sqlalchemy.orm import Session
from ..repository import login
from fastapi.security import OAuth2PasswordRequestForm
from ..hashing import Hash
from fastapi.security import OAuth2PasswordBearer



get_db = database.get_db

router = APIRouter(
    tags=['LOGIN/SIGNUP']
)

@router.post('/signup_for_owner')
def create_owner(request:schemas.loginowner, db:Session = Depends(get_db)):
    return login.create_owner(db,request)

@router.post('/signup_for_customer')
def create_customer(request:schemas.logincustomer, db:Session=Depends(get_db)):
    return login.create_customer(db,request)


@router.post('/signup_for_delivery')
def create_delivery(request:schemas.logindelivery, db:Session = Depends(get_db)):
    return login.create_delivery(db, request)

@router.post('/login_as_OWNER')
def login_as_owner(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.loginowner).filter(models.loginowner.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Incorrect password")
    access_token = oauth2.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post('/login_as_customer')
def login_as_Customer(request:schemas.logincustomer, db:Session = Depends(get_db)):
    user = db.query(models.logincustomer).filter(models.logincustomer.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Incorrect Password")
    return user


@router.post('/login_as_delivery')
def login_as_delivery(request:schemas.logindelivery,db:Session=Depends(get_db)):
    user = db.query(models.logindelivery).filter(models.logindelivery.email == request.email).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Incorrect password")
    return user

