from faker import Faker

fake = Faker()

def client_expediteur_factory(nom: str = None, prenom: str = None, email: str = None, telephone: str = None, adresse: str = None):
    """Return a dict representing a client expediteur.

    The real `ClientExpediteur` model file appears to be missing in the repo; this factory
    returns a plain dict so the seeder can either adapt or the user can provide the model.
    If `models.ClientExpediteur` exists in the environment, the seeder will try to convert
    this dict into a model instance.
    """
    return {
        "nom": nom or fake.last_name(),
        "prenom": prenom or fake.first_name(),
        "email": email or fake.email(),
        "telephone": telephone or fake.phone_number(),
        "adresse": adresse or fake.address(),
    }
