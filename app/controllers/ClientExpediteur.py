from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from crud.ClientExpediteur import (
    create_client,
    get_clients,
    get_client_by_id,
    get_client_by_email,
    update_client,
    delete_client
)
from schemas.ClientExpediteur import ClientCreate, ClientUpdate


class ClientExpediteurController:

    @staticmethod
    def create(db: Session, client: ClientCreate):
        if get_client_by_email(db, client.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email déjà utilisé"
            )
        return create_client(db, client)

    @staticmethod
    def list(db: Session):
        return get_clients(db)

    @staticmethod
    def get(db: Session, client_id: int):
        client = get_client_by_id(db, client_id)
        if not client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Client expéditeur non trouvé"
            )
        return client

    @staticmethod
    def update(db: Session, client_id: int, data: ClientUpdate):
        client = update_client(db, client_id, data.dict(exclude_unset=True))
        if not client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Client expéditeur non trouvé"
            )
        return client

    @staticmethod
    def delete(db: Session, client_id: int):
        client = delete_client(db, client_id)
        if not client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Client expéditeur non trouvé"
            )
        return {"message": "Client supprimé avec succès"}
