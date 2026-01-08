from factories.historique_factory import historique_factory

def seed_historiques(session, colis_list, livreurs, per_colis: int = 2):
    historiques = []
    for i, c in enumerate(colis_list):
        for _ in range(per_colis):
            l = livreurs[i % len(livreurs)].id if livreurs else None
            h = historique_factory(id_colis=c.id if hasattr(c, 'id') else None, id_livreur=l)
            session.add(h)
            historiques.append(h)
    session.commit()
    return historiques
