from database import SessionLocal, engine, Base
from seeders.client_expediteur_seeder import seed_clients_expediteurs
from seeders.zone_seeder import seed_zones
from seeders.livreur_seeder import seed_livreurs
from seeders.destinataire_seeder import seed_destinataires
from seeders.colis_seeder import seed_colis
from seeders.historique_seeder import seed_historiques


def run_all():

    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    try:
        print("Seeding zones...")
        zones = seed_zones(session, count=5)

        print("Seeding livreurs...")
        livreurs = seed_livreurs(session, zones, per_zone=2)

        print("Seeding destinataires...")
        destinataires = seed_destinataires(session, count=10)

        print("Seeding clients expediteurs (if model present)...")
        clients = seed_clients_expediteurs(session, count=10)

        print("Seeding colis...")
        colis = seed_colis(session, clients if isinstance(clients, list) and clients and hasattr(clients[0], 'id') else [], destinataires, livreurs, zones, count=20)

        print("Seeding historiques...")
        historiques = seed_historiques(session, colis, livreurs, per_colis=2)

        print("Seeding finished.")
    finally:
        session.close()


if __name__ == "__main__":
    run_all()
