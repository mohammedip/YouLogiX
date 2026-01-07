from sqlalchemy.orm import Session
from crud.destinataire import ( 
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
    return update_destinataire(db , destinataire_id , data)

def delete_destinataire_service(db:Session , destinataire_id : int):
    return delete_destinataire(db , destinataire_id)