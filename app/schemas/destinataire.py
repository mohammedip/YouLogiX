from pydantic import BaseModel
from typing import Optional

from typing import List

class ColisOut(BaseModel):
    id: int
    description: str

    class Config:
        from_attributes = True



class DestinataireBase(BaseModel):
    nom:str
    prenom:str
    email:str
    telephone:str
    adresse:str


class DestinataireCreate(DestinataireBase):
    pass

class DestinataireUpdate(BaseModel):
    nom:Optional[str] = None
    prenom:Optional[str] = None
    email:Optional[str] = None
    telephone:Optional[str] = None
    adresse:Optional[str] = None

class DestinataireOut(DestinataireBase):
    id:int


    class Config:
        from_attributes = True


class DestinataireOutSimple(DestinataireBase):
    id:int
    colis: List[ColisOut] = [] 


    class Config:
        from_attributes = True