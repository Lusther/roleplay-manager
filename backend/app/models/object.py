from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Object(Base):
    __tablename__ = "object"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    id_campaign = Column(Integer, ForeignKey("campaign.id"))
    bio = Column(String)
    image_path = Column(String)