from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal
from schemas.zone import ZoneCreate, ZoneUpdate, ZoneOut
from controllers.Zone import (
    create_zone_service,
    list_zones_service,
    get_zone_service,
    update_zone_service,
    delete_zone_service
)

router = APIRouter(prefix="/zones", tags=["Zones"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ZoneOut, status_code=status.HTTP_201_CREATED)
def create_zone(zone: ZoneCreate, db: Session = Depends(get_db)):
    """Créer une nouvelle zone"""
    return create_zone_service(db, zone)


@router.get("/", response_model=List[ZoneOut])
def list_zones(db: Session = Depends(get_db)):
    """Lister toutes les zones"""
    return list_zones_service(db)


@router.get("/{zone_id}", response_model=ZoneOut)
def get_zone(zone_id: int, db: Session = Depends(get_db)):
    """Récupérer une zone par son ID"""
    zone = get_zone_service(db, zone_id)
    if not zone:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Zone avec l'ID {zone_id} non trouvée"
        )
    return zone


@router.put("/{zone_id}", response_model=ZoneOut)
def update_zone(zone_id: int, zone: ZoneUpdate, db: Session = Depends(get_db)):
    """Mettre à jour une zone"""
    updated_zone = update_zone_service(db, zone_id, zone)
    if not updated_zone:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Zone avec l'ID {zone_id} non trouvée"
        )
    return updated_zone


@router.delete("/{zone_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_zone(zone_id: int, db: Session = Depends(get_db)):
    """Supprimer une zone"""
    zone = delete_zone_service(db, zone_id)
    if not zone:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Zone avec l'ID {zone_id} non trouvée"
        )
    return None
