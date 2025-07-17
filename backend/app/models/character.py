from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    id_campaign = Column(Integer, ForeignKey("campaign.id"))
    id_user = Column(Integer, ForeignKey("user.id"))
    id_class = Column(Integer, ForeignKey("classe.id"))
    bio = Column(String)
    image_path = Column(String)
    level = Column(Integer)