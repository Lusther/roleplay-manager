from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Classe(Base):
    __tablename__ = "classe"
    id = Column(Integer, primary_key=True, index=True)
    id_campaign = Column(Integer, ForeignKey("campaign.id"))
    name = Column(String, unique=True)
    bio = Column(String)
    image_path = Column(String)
