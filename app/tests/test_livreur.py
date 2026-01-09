"""
Tests CRUD Livreur
"""
import pytest


class TestLivreurCRUD:
    """Tests CRUD de base"""
    
    def test_create_livreur(self, client, sample_livreur_data):
        """Créer un livreur"""
        response = client.post("/livreurs/", json=sample_livreur_data)
        assert response.status_code == 200
        data = response.json()
        assert data["nom"] == sample_livreur_data["nom"]
        assert data["vehicule"] == sample_livreur_data["vehicule"]
        assert data["zoneAssignee"] == sample_livreur_data["zoneAssignee"]
        assert "id" in data
    
    def test_list_livreurs(self, client, sample_livreur_data):
        """✅ Lister les livreurs"""
        client.post("/livreurs/", json=sample_livreur_data)
        sample_livreur_data["telephone"] = "0655667788"
        client.post("/livreurs/", json=sample_livreur_data)
        
        response = client.get("/livreurs/")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
    
    def test_update_livreur(self, client, sample_livreur_data):
        """✅ Mettre à jour un livreur"""
        create_resp = client.post("/livreurs/", json=sample_livreur_data)
        livreur_id = create_resp.json()["id"]
        zone_id = create_resp.json()["zoneAssignee"]
        
        update_data = {"vehicule": "Voiture"}
        response = client.put(f"/livreurs/{livreur_id}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["vehicule"] == "Voiture"
        assert data["zoneAssignee"] == zone_id
    
    def test_delete_livreur(self, client, sample_livreur_data):
        """✅ Supprimer un livreur"""
        create_resp = client.post("/livreurs/", json=sample_livreur_data)
        livreur_id = create_resp.json()["id"]
        
        response = client.delete(f"/livreurs/{livreur_id}")
        assert response.status_code == 200


class TestLivreurErrors:
    """Tests erreurs"""
    
    def test_update_livreur_not_found(self, client):
        """❌ UPDATE livreur inexistant → 404"""
        response = client.put("/livreurs/99999", json={"nom": "Test"})
        assert response.status_code == 404
    
    def test_delete_livreur_not_found(self, client):
        """❌ DELETE livreur inexistant → 404"""
        response = client.delete("/livreurs/99999")
        assert response.status_code == 404
    
    def test_create_livreur_missing_fields(self, client):
        """❌ Créer livreur sans champs requis → 422"""
        response = client.post("/livreurs/", json={"nom": "Leclerc"})
        assert response.status_code == 422
