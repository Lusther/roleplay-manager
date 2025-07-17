from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base


class Token(Base):
    __tablename__ = "token"
    id_map = Column(Integer, ForeignKey("map.id"), primary_key=True, index=True)
    id_character = Column(Integer, ForeignKey("character.id"), primary_key=True, index=True)
    pos_x = Column(Integer)
    pos_y = Column(Integer)