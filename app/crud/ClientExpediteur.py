from sqlalchemy.orm import Session
from models.client_expediteur import ClientExpediteur
from schemas.client_expediteur import ClientCreate

# -------------------------------
# CREATE : créer un nouveau client
# -------------------------------
def create_client(db: Session, client: ClientCreate):
    db_client = ClientExpediteur(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

# -----------------------------------
# READ : récupérer tous les clients
# -----------------------------------
def get_clients(db: Session):
    return db.query(ClientExpediteur).all()

# -----------------------------------
# READ : récupérer un client par ID
# -----------------------------------
def get_client_by_id(db: Session, client_id: int):
    return db.query(ClientExpediteur).filter(ClientExpediteur.id == client_id).first()

# -----------------------------------
# READ : récupérer un client par email
# -----------------------------------
def get_client_by_email(db: Session, email: str):
    return db.query(ClientExpediteur).filter(ClientExpediteur.email == email).first()

# -----------------------------------
# UPDATE : modifier un client
# -----------------------------------
def update_client(db: Session, client_id: int, data: dict):
    client = get_client_by_id(db, client_id)
    if not client:
        return None
    for key, value in data.items():
        setattr(client, key, value)  # met à jour les attributs
    db.commit()
    db.refresh(client)
    return client

# -----------------------------------
# DELETE : supprimer un client
# -----------------------------------
def delete_client(db: Session, client_id: int):
    client = get_client_by_id(db, client_id)
    if not client:
        return None
    db.delete(client)
    db.commit()
    return client
