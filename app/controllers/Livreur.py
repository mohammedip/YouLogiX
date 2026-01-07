from sqlalchemy.orm import Session
from fastapi import HTTPException
from crud.Livreur import ( create_livreur , list_livreurs , update_livreur , delete_livreur)


def create_livreur_service(db:Session , data):
    return create_livreur(db , data)

def list_livreur_service(db:Session):
    return list_livreurs(db)

def update_livreur_service(db:Session , livreur_id:int , data):
    livreur =  update_livreur(db, livreur_id , data)

    if not livreur:
        raise HTTPException(status_code=404, detail="Livreur not found")
    
    return livreur

def delete_livreur_service(db:Session , livreur_id:int):
    livreur =  delete_livreur(db , livreur_id)

    if not livreur:
        raise HTTPException(status_code=404, detail="Livreur not found")
        
    return {"message": "Livreur deleted successfully"}