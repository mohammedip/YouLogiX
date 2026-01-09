from pydantic import BaseModel
from typing import Optional

# ===== Base =====
class LivreurBase(BaseModel):
    nom: str
    prenom: str
    telephone: str
    vehicule: Optional[str] = None
    id_zone: int


# ===== Create =====
class LivreurCreate(LivreurBase):
    pass


# ===== Update =====
class LivreurUpdate(BaseModel):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    telephone: Optional[str] = None
    vehicule: Optional[str] = None
    id_zone: Optional[int] = None


# ===== Response =====
class LivreurOut(LivreurBase):
    id: int

    class Config:
        from_attributes = True  