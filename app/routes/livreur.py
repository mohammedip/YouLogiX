from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.livreur import LivreurCreate , LivreurUpdate , LivtreurOut
from controllers.Livreur import (create_livreur_service , list_livreur_service , update_livreur_service , delete_livreur_service)


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


@router.post("/",response_model=LivtreurOut)
def create_livreur(data : LivreurCreate , db:Session = Depends(get_db)):
    return create_livreur_service(db , data)


@router.get("/", response_model=list[LivtreurOut])
def list_livreurs(data : LivreurCreate , db:Session=Depends(get_db)):
    return list_livreur_service(db)


@router.put("/{livreur_id}" , response_model=LivtreurOut)
def update_livreur(livreur_id : int , data : LivreurUpdate , db:Session = Depends(get_db)):
    livreur = update_livreur_service(db , livreur_id , data)
    if not livreur:
        raise HTTPException(status_code=404 , detail="Livreur not found")
    return livreur


@router.delete("/{livreur_id}")
def delete_livreur(livreur_id : int , db : Session = Depends(get_db)):
    livreur = delete_livreur_service(db , livreur_id)
    if not livreur:
        raise HTTPException(status_code=404 , detail="Livreur not found")
    return {"message": "Livreur deleted successfully"}