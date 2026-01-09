"""
Configuration Pytest: fixtures DB test + TestClient
"""
import pytest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

os.environ["TESTING"] = "1"

from app.database import Base
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    """Override de get_db pour utiliser la DB de test"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def db_session():
    """Fixture: session DB de test, reset après chaque test"""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    """Fixture: TestClient FastAPI avec DB override"""
    from app.database import get_db as main_get_db
    from app.routes import colis, destinataire, livreur, zone
    
    app.dependency_overrides[main_get_db] = override_get_db
    
    if hasattr(colis, 'get_db'):
        app.dependency_overrides[colis.get_db] = override_get_db
    if hasattr(destinataire, 'get_db'):
        app.dependency_overrides[destinataire.get_db] = override_get_db
    if hasattr(livreur, 'get_db'):
        app.dependency_overrides[livreur.get_db] = override_get_db
    if hasattr(zone, 'get_db'):
        app.dependency_overrides[zone.get_db] = override_get_db
    
    with TestClient(app) as test_client:
        yield test_client
    
    app.dependency_overrides.clear()


@pytest.fixture
def sample_client_data():
    return {
        "nom": "bouizmoune",
        "prenom": "salma",
        "email": "boui.sal@example.com",
        "telephone": "0600000000",
        "adresse": "XXXXXXXXXXXXX"
    }


@pytest.fixture
def sample_destinataire_data():
    return {
        "nom": "oussama",
        "prenom": "D",
        "email": "oussama.D@example.com",
        "telephone": "0600000000",
        "adresse": "XXXXXXXXXXXXX"
    }


@pytest.fixture
def sample_livreur_data(db_session):
    from app.models.Zone import Zone
    # Créer une zone unique pour chaque livreur
    import time
    zone = Zone(nom=f"Zone Livreur {int(time.time()*1000)}", code_postal="75001")
    db_session.add(zone)
    db_session.commit()
    db_session.refresh(zone)
    
    return {
        "nom": "Leclerc",
        "prenom": "Paul",
        "telephone": "0645678912",
        "vehicule": "Moto",
        "id_zone": zone.id
    }


@pytest.fixture
def sample_zone_data():
    return {
        "nom": "Paris Centre",
        "code_postal": "75001"
    }


@pytest.fixture
def sample_colis_data():
    """Retourne données colis (nécessite IDs créés en test)"""
    return {
        "description": "Colis fragile - Electronique",
        "poids": 2.5,
        "ville_destination": "Lyon"
    }
