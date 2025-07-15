from sqlalchemy import Column, Integer, ForeignKey
from database import Base


class CharacterStatistic(Base):
    __tablename__ = "character_statistic"
    id_character = Column(Integer, ForeignKey("character.id"), primary_key=True, index=True)
    id_statistic = Column(Integer, ForeignKey("statistic.id"), primary_key=True, index=True)
    value_statistic = Column(Integer)