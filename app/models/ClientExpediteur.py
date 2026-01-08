from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from database import Base

class ClientExpediteur(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    telephone = Column(String, nullable=False)
    adresse = Column(String, nullable=False)

    colis_envoyes = relationship(
        "Colis",
        back_populates="expediteur",  
        cascade="all, delete-orphan"
    )
