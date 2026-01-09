from sqlalchemy.orm import Session
from app.models.HistoriqueStatut import HistoriqueStatut
from app.schemas.HistoriqueStatut import HistoriqueStatutCreate

def create_historique(db: Session, historique: HistoriqueStatutCreate):
    db_historique = HistoriqueStatut(**historique.model_dump())
    db.add(db_historique)
    db.commit()
    db.refresh(db_historique)
    return db_historique

def get_historiques_by_colis(db: Session, colis_id: int):
    return (
        db.query(HistoriqueStatut)
        .filter(HistoriqueStatut.id_colis == colis_id)
        .order_by(HistoriqueStatut.timestamp.desc())
        .all()
    )
