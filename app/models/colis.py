from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.database import Base 

class StatutColis(enum.Enum):
    CREE = "créé"
    COLLECTE = "collecté"
    EN_STOCK = "en stock"
    EN_TRANSIT = "en transit"
    LIVRE = "livré"


class Colis(Base):
    __tablename__ = "colis"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    poids = Column(Float)
    statut = Column(Enum(StatutColis), default=StatutColis.CREE)
    ville_destination = Column(String)

    id_expediteur = Column(Integer, ForeignKey("clients.id"))
    id_destinataire = Column(Integer, ForeignKey("destinataires.id"))
    id_livreur = Column(Integer, ForeignKey("livreurs.id"), nullable=True)
    id_zone = Column(Integer, ForeignKey("zones.id"))

    expediteur = relationship(
        "ClientExpediteur",
        back_populates="colis_envoyes"
    )

    destinataire = relationship("Destinataire", back_populates="colis")
    historiques = relationship("HistoriqueStatut", back_populates="colis",cascade="all, delete-orphan")

    livreur = relationship(
        "Livreur",
        back_populates="colis_assignes"
    )

    zone = relationship(
        "Zone",
        back_populates="colis"
    )

    
