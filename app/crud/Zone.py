from sqlalchemy.orm import Session
from app.models.Zone import Zone
from app.schemas.zone import ZoneCreate, ZoneUpdate

def create_zone(db: Session, data: ZoneCreate):
    zone = Zone(**data.model_dump())
    db.add(zone)
    db.commit()
    db.refresh(zone)
    return zone


def list_zones(db: Session):
    return db.query(Zone).all()


def get_zone(db: Session, zone_id: int):
    return db.query(Zone).filter(Zone.id == zone_id).first()


def get_zone_by_name(db: Session, nom: str):
    return db.query(Zone).filter(Zone.nom == nom).first()

def get_zone_by_code_postal(db: Session, code_postal: str):
    return db.query(Zone).filter(Zone.code_postal == code_postal).first()


def update_zone(db: Session, zone_id: int, data: ZoneUpdate):
    zone = get_zone(db, zone_id)
    if not zone:
        return None
    
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(zone, field, value)
    
    db.commit()
    db.refresh(zone)
    return zone

def delete_zone(db: Session, zone_id: int):
    zone = get_zone(db, zone_id)
    if not zone:
        return None
    
    db.delete(zone)
    db.commit()
    return zone

