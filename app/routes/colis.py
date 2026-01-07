from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.colis import ColisCreate, ColisUpdate, ColisOut
from controllers.colis import (
    create_colis_service,
    list_colis_service,
    update_colis_service,
    delete_colis_service,
)

router = APIRouter(prefix="/colis", tags=["Colis"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ColisOut)
def create_colis(data: ColisCreate, db: Session = Depends(get_db)):
    return create_colis_service(db, data)

@router.get("/", response_model=list[ColisOut])
def list_colis(db: Session = Depends(get_db)):
    return list_colis_service(db)

@router.put("/{colis_id}", response_model=ColisOut)
def update_colis(colis_id: int, data: ColisUpdate, db: Session = Depends(get_db)):
    return update_colis_service(db, colis_id, data)


@router.delete("/{colis_id}")
def delete_colis(colis_id: int, db: Session = Depends(get_db)):
    return delete_colis_service(db, colis_id)



   
