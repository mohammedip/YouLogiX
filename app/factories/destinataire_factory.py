from faker import Faker
from app.models.Destinataire import Destinataire

fake = Faker()

def destinataire_factory(nom: str = None, prenom: str = None, email: str = None, telephone: str = None, adresse: str = None) -> Destinataire:
    return Destinataire(
        nom=nom or fake.last_name(),
        prenom=prenom or fake.first_name(),
        email=email or fake.email(),
        telephone=telephone or fake.phone_number(),
        adresse=adresse or fake.address(),
    )
