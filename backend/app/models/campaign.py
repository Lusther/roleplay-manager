from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Campaign(Base):
    __tablename__ = "campaign"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    id_master = Column(Integer, ForeignKey("user.id"))
