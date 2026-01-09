"""
Tests HistoriqueStatut
"""
import pytest


@pytest.fixture
def setup_colis(client, sample_client_data, sample_destinataire_data, sample_zone_data, sample_colis_data):
    """Fixture: créer entités + colis pour historique"""
    client_resp = client.post("/clients-expediteurs/", json=sample_client_data)
    dest_resp = client.post("/destinatiares/", json=sample_destinataire_data)
    zone_resp = client.post("/zones/", json=sample_zone_data)
    
    colis_data = {
        **sample_colis_data,
        "id_expediteur": client_resp.json()["id"],
        "id_destinataire": dest_resp.json()["id"],
        "id_zone": zone_resp.json()["id"]
    }
    colis_resp = client.post("/colis/", json=colis_data)
    
    return {
        "colis_id": colis_resp.json()["id"],
        "initial_statut": colis_resp.json()["statut"]
    }


class TestHistoriqueStatutCRUD:
    """Tests CRUD Historique Statut"""
    
    def test_create_historique(self, client, setup_colis):
        """Créer une entrée historique"""
        historique_data = {
            "id_colis": setup_colis["colis_id"],
            "ancien_statut": setup_colis["initial_statut"],
            "nouveau_statut": "En transit"
        }
        
        response = client.post("/historiques-statuts/", json=historique_data)
        assert response.status_code == 200
        data = response.json()
        assert data["id_colis"] == setup_colis["colis_id"]
        assert data["ancien_statut"] == setup_colis["initial_statut"]
        assert data["nouveau_statut"] == "En transit"
        assert "timestamp" in data
        assert "id" in data
    
    def test_list_historiques_by_colis(self, client, setup_colis):
        """Lister l'historique d'un colis"""
        historiques = [
            {
                "id_colis": setup_colis["colis_id"],
                "ancien_statut": setup_colis["initial_statut"],
                "nouveau_statut": "En transit"
            },
            {
                "id_colis": setup_colis["colis_id"],
                "ancien_statut": "En transit",
                "nouveau_statut": "Livré"
            }
        ]
        
        for hist in historiques:
            client.post("/historiques-statuts/", json=hist)
        
        response = client.get(f"/historiques-statuts/colis/{setup_colis['colis_id']}")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2


class TestHistoriqueStatutMetier:
    """Tests métier"""
    
    def test_historique_with_livreur(self, client, setup_colis, sample_livreur_data):
        """Créer historique avec livreur assigné"""
        livreur_resp = client.post("/livreurs/", json=sample_livreur_data)
        livreur_id = livreur_resp.json()["id"]
        
        historique_data = {
            "id_colis": setup_colis["colis_id"],
            "ancien_statut": setup_colis["initial_statut"],
            "nouveau_statut": "En livraison",
            "id_livreur": livreur_id
        }
        
        response = client.post("/historiques-statuts/", json=historique_data)
        assert response.status_code == 200
        data = response.json()
        assert data["id_livreur"] == livreur_id
    
    def test_historique_timestamp_auto(self, client, setup_colis):
        """Timestamp créé automatiquement"""
        historique_data = {
            "id_colis": setup_colis["colis_id"],
            "ancien_statut": setup_colis["initial_statut"],
            "nouveau_statut": "En transit"
        }
        
        response = client.post("/historiques-statuts/", json=historique_data)
        data = response.json()
        assert "timestamp" in data
        assert data["timestamp"] is not None


class TestHistoriqueStatutErrors:
    """Tests erreurs"""
    
    def test_create_historique_invalid_colis(self, client):
        """Créer historique avec colis inexistant → 404 ou 400"""
        historique_data = {
            "id_colis": 99999,
            "ancien_statut": "En attente",
            "nouveau_statut": "En transit"
        }
        
        response = client.post("/historiques-statuts/", json=historique_data)
        assert response.status_code in [400, 404, 422]
    
    def test_list_historiques_colis_not_found(self, client):
        """Lister historique colis inexistant → liste vide ou 404"""
        response = client.get("/historiques-statuts/colis/99999")
        assert response.status_code in [200, 404]
    
    def test_create_historique_missing_fields(self, client):
        """Créer historique sans champs requis → 422"""
        response = client.post("/historiques-statuts/", json={"id_colis": 1})
        assert response.status_code == 422
