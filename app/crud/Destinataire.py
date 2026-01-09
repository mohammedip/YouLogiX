from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from models.Destinataire import Destinataire
from schemas.destinataire import DestinataireCreate , DestinataireUpdate


def create_destinataire(db:Session , data:DestinataireCreate):
    destinataire = Destinataire(**data.model_dump(), statut="créé")
    db.add(destinataire)
    db.commit()
    db.refresh(destinataire)
    return destinataire

def list_destinataire(db:Session):
    return db.query(Destinataire).all()

def get_destinataire(db:Session,destinataire_id : int):
    return db.query(Destinataire).filter(Destinataire.id == destinataire_id).first()

def update_destinataire(db : Session,destinataire_id:int , data:DestinataireUpdate):
    destinataire = get_destinataire(db , destinataire_id)
    if not destinataire:
        return None
    
    for field , value in data.model_dump(exclude_unset=True).items():
        setattr(destinataire , field , value)

    db.commit()
    db.refresh(destinataire)
    return destinataire


def delete_destinataire(db:Session,destinataire_id : int):
    destinataire = get_destinataire(db , destinataire_id)
    if not destinataire:
        return None
    
    db.delete(destinataire)
    db.commit()
    return destinataire

def list_destinataire_colis(db:Session):
    return db.query(Destinataire).options(joinedload(Destinataire.colis)).all()
