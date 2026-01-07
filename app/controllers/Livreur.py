from sqlalchemy.orm import Session
from crud.Livreur import ( create_livreur , list_livreurs , update_livreur , delete_livreur)


def create_livreur_service(db:Session , data):
    return create_livreur(db , data)

def list_livreur_service(db:Session):
    return list_livreurs(db)

def update_livreur_service(db:Session , livreur_id:int , data):
    return update_livreur(db, livreur_id , data)

def delete_livreur_service(db:Session , livreur_id:int):
    return delete_livreur(db , livreur_id)