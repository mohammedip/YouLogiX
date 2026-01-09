from pydantic import BaseModel
from typing import Optional

class ColisBase(BaseModel):
    description: str
    poids: float
    id_expediteur: int
    id_destinataire: int
    id_zone: int
    ville_destination: str

class ColisCreate(ColisBase):
    pass

class ColisUpdate(BaseModel):
    description: Optional[str] = None
    poids: Optional[float] = None
    id_expediteur: Optional[int] = None
    id_destinataire: Optional[int] = None
    id_zone: Optional[int] = None
    ville_destination: Optional[str] = None
    statut: Optional[str] = None

class ColisOut(ColisBase):
    id: int
    statut: str

    class Config:
        from_attributes = True
