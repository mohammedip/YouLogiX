from sqlalchemy.orm import Session
from models.Livreur import Livreur
from schemas.livreur import LivreurCreate , LivreurUpdate


def create_livreur(db:Session , data:LivreurCreate):
    livreur = Livreur(**data.model_dump())
    db.add(livreur)
    db.commit()
    db.refresh(livreur)
    return livreur


def list_livreurs(db:Session):
    return db.query(Livreur).all()

def get_livreur(db:Session , livreur_id:int):
    return db.query(Livreur).filter(Livreur.id == livreur_id).first()

def update_livreur(db:Session , livreur_id:int , data:LivreurUpdate):
    livreur = get_livreur(db , livreur_id)
    if not livreur:
        return None
    
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(livreur,field,value)

    db.commit()
    db.refresh(livreur)
    return livreur


def delete_livreur(db:Session , livreur_id : int):
    livreur = get_livreur(db, livreur_id)
    if not livreur:
        return None
    
    db.delete(livreur)
    db.commit()
    return livreur