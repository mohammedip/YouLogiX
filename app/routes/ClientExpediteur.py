from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.controllers.ClientExpediteur import ClientExpediteurController
from app.schemas.ClientExpediteur import ClientCreate, ClientUpdate, ClientResponse

router = APIRouter(
    prefix="/clients-expediteurs",
    tags=["Clients Expéditeurs"]
)


@router.post("/", response_model=ClientResponse)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    return ClientExpediteurController.create(db, client)


@router.get("/", response_model=list[ClientResponse])
def list_clients(db: Session = Depends(get_db)):
    return ClientExpediteurController.list(db)


@router.get("/{client_id}", response_model=ClientResponse)
def get_client(client_id: int, db: Session = Depends(get_db)):
    return ClientExpediteurController.get(db, client_id)


@router.put("/{client_id}", response_model=ClientResponse)
def update_client(
    client_id: int,
    data: ClientUpdate,
    db: Session = Depends(get_db)
):
    return ClientExpediteurController.update(db, client_id, data)


@router.delete("/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    return ClientExpediteurController.delete(db, client_id)
