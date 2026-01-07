
from pydantic import BaseModel, EmailStr


class ClientBase(BaseModel):
    nom:str
    prenom:str
    email:EmailStr
    telephone:str
    adresse:str

class ClientCreate(ClientBase):
    pass


class ClientResponse(ClientBase):
    id=int

    class Config:
        orm_mode=True

