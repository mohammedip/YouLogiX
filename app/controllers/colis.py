from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.crud.colis import (
    create_colis,
    list_colis,
    get_colis,
    update_colis,
    delete_colis,
)

def create_colis_service(db: Session, data):
    return create_colis(db, data)

def list_colis_service(db: Session):
    return list_colis(db)

def update_colis_service(db: Session, colis_id: int, data):
    colis = update_colis(db, colis_id, data)
    
    if not colis:
        raise HTTPException(status_code=404, detail="Colis not found")
    
    return colis

def delete_colis_service(db: Session, colis_id: int):
    colis = delete_colis(db, colis_id)
    
    if not colis:
        raise HTTPException(status_code=404, detail="Colis not found")
        
    return {"message": "Colis deleted successfully"}
