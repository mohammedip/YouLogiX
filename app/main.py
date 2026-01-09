from fastapi import FastAPI
from app.database import Base, engine
from app.routes.colis import router as colis_router
from app.routes.livreur import router as livreur_router
from app.routes.zone import router as zone_router
from app.routes.destinataire import router as destinataire_router
from app.routes.ClientExpediteur import router as ClientExpediteur_router
from app.routes.HistoriqueStatut import router as historique_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="YouLogix API")

app.include_router(colis_router)
app.include_router(livreur_router)
app.include_router(zone_router)
app.include_router(destinataire_router)
app.include_router(ClientExpediteur_router)
app.include_router(historique_router)



