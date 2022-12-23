from passlib.context import CryptContext
from typing import Union



pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    @staticmethod
    def bcrypt(password: str):
        hashed_Password = pwd_cxt.hash(password)
        return hashed_Password

    @staticmethod
    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)
