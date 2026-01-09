from sqlalchemy.orm import Session
from crud.HistoriqueStatut import create_historique, get_historiques_by_colis
from schemas.HistoriqueStatut import HistoriqueStatutCreate

class HistoriqueStatutController:

    @staticmethod
    def add(db: Session, historique: HistoriqueStatutCreate):
        return create_historique(db, historique)

    @staticmethod
    def list_by_colis(db: Session, colis_id: int):
        return get_historiques_by_colis(db, colis_id)
