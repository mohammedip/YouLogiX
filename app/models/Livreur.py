from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base 


class Livreur(Base):
    __tablename__ = "livreurs"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    telephone = Column(String, nullable=False)
    vehicule = Column(String, nullable=True)

    id_zone = Column(Integer, ForeignKey("zones.id"), nullable=False)

    zone = relationship("Zone", back_populates="livreurs")
    colis_assignes = relationship("Colis", back_populates="livreur")
