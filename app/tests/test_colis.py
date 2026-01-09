"""
Tests CRUD Colis + Tests métier
"""
import pytest


@pytest.fixture
def setup_entities(client, sample_client_data, sample_destinataire_data, sample_zone_data):
    """Fixture: créer client, destinataire, zone nécessaires pour colis"""
    client_resp = client.post("/clients-expediteurs/", json=sample_client_data)
    dest_resp = client.post("/destinatiares/", json=sample_destinataire_data)
    zone_resp = client.post("/zones/", json=sample_zone_data)
    
    return {
        "client_id": client_resp.json()["id"],
        "destinataire_id": dest_resp.json()["id"],
        "zone_id": zone_resp.json()["id"]
    }


class TestColisCRUD:
    """Tests CRUD de base"""
    
    def test_create_colis(self, client, sample_colis_data, setup_entities):
        """Créer un colis"""
        colis_data = {
            **sample_colis_data,
            "id_expediteur": setup_entities["client_id"],
            "id_destinataire": setup_entities["destinataire_id"],
            "id_zone": setup_entities["zone_id"]
        }
        
        
        response = client.post("/colis/", json=colis_data)
        assert response.status_code == 200
        data = response.json()
        assert data["description"] == colis_data["description"]
        assert data["poids"] == colis_data["poids"]
        assert "id" in data
        assert "statut" in data
    
    def test_list_colis(self, client, sample_colis_data, setup_entities):
        """Lister les colis"""
        colis_data = {
            **sample_colis_data,
            "id_expediteur": setup_entities["client_id"],
            "id_destinataire": setup_entities["destinataire_id"],
            "id_zone": setup_entities["zone_id"]
        }
        
        client.post("/colis/", json=colis_data)
        colis_data["description"] = "Autre colis"
        client.post("/colis/", json=colis_data)
        
        response = client.get("/colis/")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
    
    def test_update_colis(self, client, sample_colis_data, setup_entities):
        """Mettre à jour un colis"""
        colis_data = {
            **sample_colis_data,
            "id_expediteur": setup_entities["client_id"],
            "id_destinataire": setup_entities["destinataire_id"],
            "id_zone": setup_entities["zone_id"]
        }
        
        create_resp = client.post("/colis/", json=colis_data)
        colis_id = create_resp.json()["id"]
        
        update_data = {"description": "Colis mis à jour", "poids": 3.5}
        response = client.put(f"/colis/{colis_id}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["description"] == "Colis mis à jour"
        assert data["poids"] == 3.5
    
    def test_delete_colis(self, client, sample_colis_data, setup_entities):
        """Supprimer un colis"""
        colis_data = {
            **sample_colis_data,
            "id_expediteur": setup_entities["client_id"],
            "id_destinataire": setup_entities["destinataire_id"],
            "id_zone": setup_entities["zone_id"]
        }
        
        create_resp = client.post("/colis/", json=colis_data)
        colis_id = create_resp.json()["id"]
        
        response = client.delete(f"/colis/{colis_id}")
        assert response.status_code == 200


class TestColisMetier:
    """Tests métier spécifiques"""
    
    def test_colis_has_default_statut(self, client, sample_colis_data, setup_entities):
        """Colis créé doit avoir un statut initial"""
        colis_data = {
            **sample_colis_data,
            "id_expediteur": setup_entities["client_id"],
            "id_destinataire": setup_entities["destinataire_id"],
            "id_zone": setup_entities["zone_id"]
        }
        
        response = client.post("/colis/", json=colis_data)
        data = response.json()
        assert "statut" in data
        assert data["statut"] is not None
    
    def test_update_statut_colis(self, client, sample_colis_data, setup_entities):
        """Mettre à jour le statut d'un colis"""
        colis_data = {
            **sample_colis_data,
            "id_expediteur": setup_entities["client_id"],
            "id_destinataire": setup_entities["destinataire_id"],
            "id_zone": setup_entities["zone_id"]
        }
        
        create_resp = client.post("/colis/", json=colis_data)
        colis_id = create_resp.json()["id"]
        
        update_data = {"statut": "En transit"}
        response = client.put(f"/colis/{colis_id}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["statut"] == "En transit"


class TestColisErrors:
    """Tests erreurs"""
    
    def test_update_colis_not_found(self, client):
        """UPDATE colis inexistant → 404"""
        response = client.put("/colis/99999", json={"description": "Test"})
        assert response.status_code == 404
    
    def test_delete_colis_not_found(self, client):
        """ DELETE colis inexistant → 404"""
        response = client.delete("/colis/99999")
        assert response.status_code == 404
    
    def test_create_colis_invalid_foreign_keys(self, client, sample_colis_data):
        """Créer colis avec IDs invalides → 404 ou 400"""
        colis_data = {
            **sample_colis_data,
            "id_expediteur": 99999,
            "id_destinataire": 99999,
            "id_zone": 99999
        }
        
        response = client.post("/colis/", json=colis_data)
        assert response.status_code in [400, 404, 422]
    
    def test_create_colis_missing_fields(self, client):
        """Créer colis sans champs requis → 422"""
        response = client.post("/colis/", json={"description": "Test"})
        assert response.status_code == 422
