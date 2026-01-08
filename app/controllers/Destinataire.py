from sqlalchemy.orm import Session
from fastapi import HTTPException
from crud.Destinataire import ( 
    create_destinataire,
    list_destinataire,
    update_destinataire,
    delete_destinataire
)


def create_destinataire_service(db:Session,data):
    return create_destinataire(db,data)

def list_destinataire_service(db:Session):
    return list_destinataire(db)

def update_destinataire_service(db:Session , destinataire_id : int , data):
    destinataire =  update_destinataire(db , destinataire_id , data)

    if not destinataire:
        raise HTTPException(status_code=404, detail="Destinataire not found")
    
    return destinataire

def delete_destinataire_service(db:Session , destinataire_id : int):
    destinataire =  delete_destinataire(db , destinataire_id)

    if not destinataire:
        raise HTTPException(status_code=404, detail="Destinataire not found")
        
    return {"message": "Destinataire deleted successfully"}