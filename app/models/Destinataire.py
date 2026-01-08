from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base 

class Destinataire(Base):
    __tablename__ = "destinataires"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    prenom = Column(String)
    email = Column(String)
    telephone = Column(String)
    adresse = Column(String)

    colis_attendus = relationship("Colis", back_populates="destinataire")
    colis = relationship("Colis", back_populates="destinataire")
