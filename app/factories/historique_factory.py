from faker import Faker
from datetime import datetime
from models.HistoriqueStatut import HistoriqueStatut

fake = Faker()

def historique_factory(id_colis: int = None, ancien_statut: str = None, nouveau_statut: str = None, id_livreur: int = None) -> HistoriqueStatut:
    return HistoriqueStatut(
        id_colis=id_colis,
        ancien_statut=ancien_statut or fake.word(),
        nouveau_statut=nouveau_statut or fake.word(),
        id_livreur=id_livreur,
    )
