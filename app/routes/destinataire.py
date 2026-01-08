from fastapi import APIRouter , Depends 
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.destinataire import DestinataireCreate , DestinataireUpdate , DestinataireOut
from controllers.Destinataire import (
    create_destinataire_service,
    list_destinataire_service,
    update_destinataire_service,
    delete_destinataire_service
)


router = APIRouter(prefix="/destinatiares" , tags=["Destinataires"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/" , response_model=DestinataireOut)
def create_destinataire(data:DestinataireCreate , db:Session = Depends(get_db)):
    return create_destinataire_service(db,data)


@router.get("/" , response_model=list[DestinataireOut])
def list_destinataires(db : Session = Depends(get_db)):
    return list_destinataire_service(db)


@router.put("/{destinataire_id}" , response_model=DestinataireOut)
def update_destinataire(destinataire_id:int , data:DestinataireUpdate , db:Session = Depends(get_db)):
    return update_destinataire_service(db , destinataire_id , data)


@router.delete("/{destinataire_id}")
def delete_destinatiare(destinataire_id : int , db : Session = Depends(get_db)):
    return delete_destinataire_service(db , destinataire_id)
