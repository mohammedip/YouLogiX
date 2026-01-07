from sqlalchemy.orm import Session
from crud.Zone import (create_zone,list_zones,get_zone,get_zone_by_name,get_zone_by_code_postal,update_zone,delete_zone)
def create_zone_service(db: Session, data):
    return create_zone(db, data)

def list_zones_service(db: Session):
    return list_zones(db)


def get_zone_service(db: Session, zone_id: int):
    return get_zone(db, zone_id)


def get_zone_by_name_service(db: Session, nom: str):
    return get_zone_by_name(db, nom)


def get_zone_by_code_postal_service(db: Session, code_postal: str):
    return get_zone_by_code_postal(db, code_postal)


def update_zone_service(db: Session, zone_id: int, data):
    return update_zone(db, zone_id, data)


def delete_zone_service(db: Session, zone_id: int):
    return delete_zone(db, zone_id)

