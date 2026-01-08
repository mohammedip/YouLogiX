from factories.livreur_factory import livreur_factory

def seed_livreurs(session, zones, per_zone: int = 2):
    livreurs = []
    for z in zones:
        for _ in range(per_zone):
            l = livreur_factory(zone_id=z.id)
            session.add(l)
            livreurs.append(l)
    session.commit()
    return livreurs
