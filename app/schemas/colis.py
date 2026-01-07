from pydantic import BaseModel
from typing import Optional

class ColisBase(BaseModel):
    description: str
    poids: float
    idClientExpediteur: int
    idDestinataire: int
    idZone: int
    villeDestination: str

class ColisCreate(ColisBase):
    pass

class ColisUpdate(BaseModel):
    description: Optional[str] = None
    poids: Optional[float] = None
    idClientExpediteur: Optional[int] = None
    idDestinataire: Optional[int] = None
    idZone: Optional[int] = None
    villeDestination: Optional[str] = None
    statut: Optional[str] = None

class ColisOut(ColisBase):
    id: int
    statut: str

    class Config:
        from_attributes = True
