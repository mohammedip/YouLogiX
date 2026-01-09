from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.livreur import LivreurCreate, LivreurUpdate, LivreurOut
from app.controllers.Livreur import (create_livreur_service , list_livreur_service , update_livreur_service , delete_livreur_service)


router = APIRouter(
    prefix="/livreurs",
    tags = ["Livreurs"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/",response_model=LivreurOut)
def create_livreur(data : LivreurCreate , db:Session = Depends(get_db)):
    return create_livreur_service(db , data)




@router.get("/", response_model=list[LivreurOut])
def list_livreurs(db: Session = Depends(get_db)):
    return list_livreur_service(db)




@router.put("/{livreur_id}" , response_model=LivreurOut)
def update_livreur(livreur_id : int , data : LivreurUpdate , db:Session = Depends(get_db)):
    return update_livreur_service(db , livreur_id , data)



@router.delete("/{livreur_id}")
def delete_livreur(livreur_id : int , db : Session = Depends(get_db)):
    return delete_livreur_service(db , livreur_id)
