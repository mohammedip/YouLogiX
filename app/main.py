# from fastapi import FastAPI

# app = FastAPI(title="YouLogiX")

# @app.get("/")
# def read_root():
#     return {"message": "YouLogiX API"}

from database import engine, Base
Base.metadata.create_all(bind=engine)
