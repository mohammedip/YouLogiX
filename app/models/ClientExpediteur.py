from sqlalchemy import Column ,Enum,String ,ForeignKey,DateTime,Integer
from sqlalchemy.orm import  relationship
from sqlalchemy.sql import func
from database import Base
class ClientExpediteur(Base):
    __tablename__="clients"
    id=Column(Integer,primary_key=True,index=True)
    nom = Column(String)
    prenom = Column(String)
    email =Column(String ,unique=True)
    telephone=Column(String)
    adress=Column(String)

    Colis_envoyes=relationship("Colis",back_populates="expediteur")