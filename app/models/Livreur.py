from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base 


class Livreur(Base):
    __tablename__ = "livreurs"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    prenom = Column(String)
    telephone = Column(String)
    vehicule = Column(String) 
    
    id_zone = Column(Integer, ForeignKey("zones.id"))
    
 
    zone = relationship("Zone", back_populates="livreurs")
    colis_assignes = relationship("Colis", back_populates="livreur")
