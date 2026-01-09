from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class HistoriqueStatutBase(BaseModel):
    id_colis: int
    ancien_statut: str
    nouveau_statut: str
    id_livreur: Optional[int] = None

class HistoriqueStatutCreate(HistoriqueStatutBase):
    pass

class HistoriqueStatutResponse(HistoriqueStatutBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True
