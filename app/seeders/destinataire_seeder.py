from factories.destinataire_factory import destinataire_factory

def seed_destinataires(session, count: int = 10):
    destinataires = []
    for _ in range(count):
        d = destinataire_factory()
        session.add(d)
        destinataires.append(d)
    session.commit()
    return destinataires
