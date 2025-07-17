from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Statistic(Base):
    __tablename__ = "statistic"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    id_campaign = Column(Integer, ForeignKey("campaign.id"))
    bio = Column(String)
    image_path = Column(String)
    min_value = Column(Integer)
    max_value = Column(Integer)
