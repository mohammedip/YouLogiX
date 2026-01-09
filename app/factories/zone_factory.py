from faker import Faker
from app.models.Zone import Zone

fake = Faker()

def zone_factory(nom: str = None, code_postal: str = None) -> Zone:
    return Zone(nom=nom or fake.city(), code_postal=code_postal or fake.postcode())
