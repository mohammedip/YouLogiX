from fastapi import FastAPI
from database import Base, engine
from routes.colis import router as colis_router
from routes.livreur import router as livreur_router

from routes.zone import router as zone_router

from routes.destinataire import router as destinataire_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="YouLogix API")

app.include_router(colis_router)
app.include_router(livreur_router)

app.include_router(zone_router)

app.include_router(destinataire_router)

