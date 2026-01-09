from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base 

class HistoriqueStatut(Base):
    __tablename__ = "historique_statuts"
    id = Column(Integer, primary_key=True, index=True)
    id_colis = Column(Integer, ForeignKey("colis.id"))
    ancien_statut = Column(String)
    nouveau_statut = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    id_livreur = Column(Integer, ForeignKey("livreurs.id"))

    colis = relationship("Colis", back_populates="historiques")
    