from faker import Faker
import random
from models.colis import Colis, StatutColis

fake = Faker()

def colis_factory(
    description: str = None,
    poids: float = None,
    ville_destination: str = None,
    id_expediteur: int = None,
    id_destinataire: int = None,
    id_livreur: int = None,
    id_zone: int = None,
    statut: StatutColis = None,
) -> Colis:
    statut = statut or random.choice(list(StatutColis))
    return Colis(
        description=description or fake.sentence(nb_words=6),
        poids=poids or round(random.uniform(0.1, 20.0), 2),
        ville_destination=ville_destination or fake.city(),
        id_expediteur=id_expediteur,
        id_destinataire=id_destinataire,
        id_livreur=id_livreur,
        id_zone=id_zone,
        statut=statut,
    )
