from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from database import Base 


class Zone(Base):
    __tablename__ = "zones"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, unique=True, nullable=False) 
    code_postal = Column(String, nullable=False)
    livreurs = relationship("Livreur", back_populates="zone")
    colis = relationship("Colis", back_populates="zone")
