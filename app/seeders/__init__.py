
from .zone_seeder import seed_zones
from .livreur_seeder import seed_livreurs
from .destinataire_seeder import seed_destinataires
from .colis_seeder import seed_colis
from .historique_seeder import seed_historiques
from .client_expediteur_seeder import seed_clients_expediteurs

__all__ = [
    "seed_zones",
    "seed_livreurs",
    "seed_destinataires",
    "seed_colis",
    "seed_historiques",
    "seed_clients_expediteurs",
]
