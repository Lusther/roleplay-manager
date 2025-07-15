from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Map(Base):
    __tablename__ = "map"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    id_campaign = Column(Integer, ForeignKey("campaign.id"))
    image_path = Column(String)
    bio = Column(String)