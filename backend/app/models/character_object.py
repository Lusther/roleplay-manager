from sqlalchemy import Column, Integer, ForeignKey
from database import Base


class CharacterObject(Base):
    __tablename__ = "character_object"
    id_character = Column(Integer, ForeignKey("character.id"), primary_key=True, index=True)
    id_object = Column(Integer, ForeignKey("object.id"), primary_key=True, index=True)
    quantity = Column(Integer)