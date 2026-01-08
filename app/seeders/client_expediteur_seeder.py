from factories.client_expediteur_factory import client_expediteur_factory

def seed_clients_expediteurs(session, count: int = 10):
    """Try to seed clients. If `models.ClientExpediteur` exists the seeder will
    create model instances, otherwise it will insert raw dicts if the user adapts.
    """
    try:
        from models.ClientExpediteur import ClientExpediteur
    except Exception:
        # Model file missing — return dicts so the user can adapt.
        clients = []
        for _ in range(count):
            c = client_expediteur_factory()
            clients.append(c)
        return clients

    clients = []
    for _ in range(count):
        data = client_expediteur_factory()
        client = ClientExpediteur(**data)
        session.add(client)
        clients.append(client)
    session.commit()
    return clients
