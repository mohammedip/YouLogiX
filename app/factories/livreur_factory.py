from faker import Faker
from models.Livreur import Livreur

fake = Faker()

def livreur_factory(zone_id: int = None, nom: str = None, prenom: str = None, telephone: str = None, vehicule: str = None) -> Livreur:
    return Livreur(
        nom=nom or fake.last_name(),
        prenom=prenom or fake.first_name(),
        telephone=telephone or fake.phone_number(),
        vehicule=vehicule or fake.word(),
        id_zone=zone_id,
    )
