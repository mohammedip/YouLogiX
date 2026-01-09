"""
Tests CRUD Zone
"""
import pytest


class TestZoneCRUD:
    """Tests CRUD de base"""
    
    def test_create_zone(self, client, sample_zone_data):
        """Créer une zone"""
        response = client.post("/zones/", json=sample_zone_data)
        assert response.status_code == 201
        data = response.json()
        assert data["nom"] == sample_zone_data["nom"]
        assert data["code_postal"] == sample_zone_data["code_postal"]
        assert "id" in data
    
    def test_list_zones(self, client, sample_zone_data):
        """Lister les zones"""
        client.post("/zones/", json=sample_zone_data)
        sample_zone_data["code_postal"] = "69001"
        sample_zone_data["nom"] = "Lyon Centre"
        client.post("/zones/", json=sample_zone_data)
        
        response = client.get("/zones/")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
    
    def test_get_zone(self, client, sample_zone_data):
        """Récupérer une zone par ID"""
        create_resp = client.post("/zones/", json=sample_zone_data)
        zone_id = create_resp.json()["id"]
        
        response = client.get(f"/zones/{zone_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == zone_id
        assert data["nom"] == sample_zone_data["nom"]
    
    def test_update_zone(self, client, sample_zone_data):
        """Mettre à jour une zone"""
        create_resp = client.post("/zones/", json=sample_zone_data)
        zone_id = create_resp.json()["id"]
        
        update_data = {"nom": "Paris Est", "code_postal": "75012"}
        response = client.put(f"/zones/{zone_id}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["nom"] == "Paris Est"
        assert data["code_postal"] == "75012"
    
    def test_delete_zone(self, client, sample_zone_data):
        """Supprimer une zone"""
        create_resp = client.post("/zones/", json=sample_zone_data)
        zone_id = create_resp.json()["id"]
        
        response = client.delete(f"/zones/{zone_id}")
        assert response.status_code == 204
        
        # Vérifier suppression
        get_resp = client.get(f"/zones/{zone_id}")
        assert get_resp.status_code == 404


class TestZoneErrors:
    """Tests erreurs"""
    
    def test_get_zone_not_found(self, client):
        """GET zone inexistante → 404"""
        response = client.get("/zones/99999")
        assert response.status_code == 404
    
    def test_update_zone_not_found(self, client):
        """UPDATE zone inexistante → 404"""
        response = client.put("/zones/99999", json={"nom": "Test"})
        assert response.status_code == 404
    
    def test_delete_zone_not_found(self, client):
        """DELETE zone inexistante → 404"""
        response = client.delete("/zones/99999")
        assert response.status_code == 404
    
    def test_create_zone_missing_fields(self, client):
        """Créer zone sans champs requis → 422"""
        response = client.post("/zones/", json={"nom": "Paris"})
        assert response.status_code == 422
