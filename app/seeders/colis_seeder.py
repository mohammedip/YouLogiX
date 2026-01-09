from app.factories.colis_factory import colis_factory

def seed_colis(session, expediteurs, destinataires, livreurs, zones, count: int = 20):
    colis_list = []
    for _ in range(count):
        expediteur_id = expediteurs[0].id if expediteurs and hasattr(expediteurs[0], 'id') else None
        destinataire_id = destinataires[_ % len(destinataires)].id if destinataires else None
        livreur_id = livreurs[_ % len(livreurs)].id if livreurs else None
        zone_id = zones[_ % len(zones)].id if zones else None
        c = colis_factory(
            id_expediteur=expediteur_id,
            id_destinataire=destinataire_id,
            id_livreur=livreur_id,
            id_zone=zone_id,
        )
        session.add(c)
        colis_list.append(c)
    session.commit()
    return colis_list
