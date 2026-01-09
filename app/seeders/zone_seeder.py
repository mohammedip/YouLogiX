from app.factories.zone_factory import zone_factory

def seed_zones(session, count: int = 5):
    zones = []
    for _ in range(count):
        z = zone_factory()
        session.add(z)
        zones.append(z)
    session.commit()
    return zones
