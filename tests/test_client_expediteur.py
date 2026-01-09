"""
Tests CRUD ClientExpediteur
"""
import pytest


class TestClientExpediteurCRUD:
    """Tests CRUD de base"""
    
    def test_create_client(self, client, sample_client_data):
        """Créer un client expéditeur"""
        response = client.post("/clients-expediteurs/", json=sample_client_data)
        assert response.status_code == 200
        data = response.json()
        assert data["nom"] == sample_client_data["nom"]
        assert data["email"] == sample_client_data["email"]
        assert "id" in data
    
    def test_list_clients(self, client, sample_client_data):
        """ Lister les clients expéditeurs"""
        client.post("/clients-expediteurs/", json=sample_client_data)
        sample_client_data["email"] = "autre@example.com"
        client.post("/clients-expediteurs/", json=sample_client_data)
        
        response = client.get("/clients-expediteurs/")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
    
    def test_get_client(self, client, sample_client_data):
        """ Récupérer un client par ID"""
        create_resp = client.post("/clients-expediteurs/", json=sample_client_data)
        client_id = create_resp.json()["id"]
        
        response = client.get(f"/clients-expediteurs/{client_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == client_id
        assert data["nom"] == sample_client_data["nom"]
    
    def test_update_client(self, client, sample_client_data):
        """ Mettre à jour un client"""
        create_resp = client.post("/clients-expediteurs/", json=sample_client_data)
        client_id = create_resp.json()["id"]
        
        update_data = {"nom": "Durand", "telephone": "0611223344"}
        response = client.put(f"/clients-expediteurs/{client_id}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["nom"] == "Durand"
        assert data["telephone"] == "0611223344"
    
    def test_delete_client(self, client, sample_client_data):
        """Supprimer un client"""
        create_resp = client.post("/clients-expediteurs/", json=sample_client_data)
        client_id = create_resp.json()["id"]
        
        response = client.delete(f"/clients-expediteurs/{client_id}")
        assert response.status_code == 200
        
        get_resp = client.get(f"/clients-expediteurs/{client_id}")
        assert get_resp.status_code == 404


class TestClientExpediteurErrors:
    """Tests erreurs et validations"""
    
    def test_get_client_not_found(self, client):
        """ GET client inexistant → 404"""
        response = client.get("/clients-expediteurs/99999")
        assert response.status_code == 404
    
    def test_update_client_not_found(self, client):
        """UPDATE client inexistant → 404"""
        response = client.put("/clients-expediteurs/99999", json={"nom": "Test"})
        assert response.status_code == 404
    
    def test_delete_client_not_found(self, client):
        """DELETE client inexistant → 404"""
        response = client.delete("/clients-expediteurs/99999")
        assert response.status_code == 404
    
    def test_create_client_invalid_email(self, client, sample_client_data):
        """Créer client avec email invalide → 422"""
        sample_client_data["email"] = "invalid-email"
        response = client.post("/clients-expediteurs/", json=sample_client_data)
        assert response.status_code == 422
    
    def test_create_client_missing_fields(self, client):
        """Créer client sans champs requis → 422"""
        response = client.post("/clients-expediteurs/", json={"nom": "Dupont"})
        assert response.status_code == 422
