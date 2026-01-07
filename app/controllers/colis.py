from sqlalchemy.orm import Session
from crud.colis import (
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
    return update_colis(db, colis_id, data)

def delete_colis_service(db: Session, colis_id: int):
    return delete_colis(db, colis_id)
