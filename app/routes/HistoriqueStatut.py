from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers.historique_statut import HistoriqueStatutController
from schemas.historique_statut import (
    HistoriqueStatutCreate,
    HistoriqueStatutResponse
)

router = APIRouter(
    prefix="/historiques-statuts",
    tags=["Historique Statut"]
)

@router.post("/", response_model=HistoriqueStatutResponse)
def create_historique(
    historique: HistoriqueStatutCreate,
    db: Session = Depends(get_db)
):
    return HistoriqueStatutController.add(db, historique)

@router.get(
    "/colis/{colis_id}",
    response_model=list[HistoriqueStatutResponse]
)
def get_historiques(colis_id: int, db: Session = Depends(get_db)):
    return HistoriqueStatutController.list_by_colis(db, colis_id)
