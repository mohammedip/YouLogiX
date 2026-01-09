"""
Tests CRUD Destinataire
"""
import pytest


class TestDestinataireCRUD:
    """Tests CRUD de base"""
    
    def test_create_destinataire(self, client, sample_destinataire_data):
        """Créer un destinataire"""
        response = client.post("/destinatiares/", json=sample_destinataire_data)
        assert response.status_code == 200
        data = response.json()
        assert data["nom"] == sample_destinataire_data["nom"]
        assert data["email"] == sample_destinataire_data["email"]
        assert "id" in data
    
    def test_list_destinataires(self, client, sample_destinataire_data):
        """Lister les destinataires"""
        client.post("/destinatiares/", json=sample_destinataire_data)
        sample_destinataire_data["email"] = "autre@example.com"
        client.post("/destinatiares/", json=sample_destinataire_data)
        
        response = client.get("/destinatiares/")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
    
    def test_update_destinataire(self, client, sample_destinataire_data):
        """Mettre à jour un destinataire"""
        create_resp = client.post("/destinatiares/", json=sample_destinataire_data)
        dest_id = create_resp.json()["id"]
        
        update_data = {"nom": "Nouveau", "telephone": "0699887766"}
        response = client.put(f"/destinatiares/{dest_id}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["nom"] == "Nouveau"
        assert data["telephone"] == "0699887766"
    
    def test_delete_destinataire(self, client, sample_destinataire_data):
        """Supprimer un destinataire"""
        create_resp = client.post("/destinatiares/", json=sample_destinataire_data)
        dest_id = create_resp.json()["id"]
        
        response = client.delete(f"/destinatiares/{dest_id}")
        assert response.status_code == 200


class TestDestinataireErrors:
    """Tests erreurs"""
    
    def test_update_destinataire_not_found(self, client):
        """UPDATE destinataire inexistant → 404"""
        response = client.put("/destinatiares/99999", json={"nom": "Test"})
        assert response.status_code == 404
    
    def test_delete_destinataire_not_found(self, client):
        """DELETE destinataire inexistant → 404"""
        response = client.delete("/destinatiares/99999")
        assert response.status_code == 404
    
    def test_create_destinataire_missing_fields(self, client):
        """Créer destinataire sans champs requis → 422"""
        response = client.post("/destinatiares/", json={"nom": "Martin"})
        assert response.status_code == 422
