from sqlalchemy.orm import Session
from app.models.colis import Colis, StatutColis
from app.schemas.colis import ColisCreate, ColisUpdate

def create_colis(db: Session, data: ColisCreate):
    colis = Colis(**data.model_dump())
    db.add(colis)
    db.commit()
    db.refresh(colis)
    return colis

def list_colis(db: Session):
    return db.query(Colis).all()

def get_colis(db: Session, colis_id: int):
    return db.query(Colis).filter(Colis.id == colis_id).first()

def update_colis(db: Session, colis_id: int, data: ColisUpdate):
    colis = get_colis(db, colis_id)
    if not colis:
        return None

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(colis, field, value)

    db.commit()
    db.refresh(colis)
    return colis

def delete_colis(db: Session, colis_id: int):
    colis = get_colis(db, colis_id)
    if not colis:
        return None

    db.delete(colis)
    db.commit()
    return colis
