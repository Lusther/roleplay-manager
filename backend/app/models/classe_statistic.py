from sqlalchemy import Column, Integer, ForeignKey
from database import Base


class ClasseStatistic(Base):
    __tablename__ = "classe_statistic"
    id_class = Column(Integer, ForeignKey("classe.id"), primary_key=True, index=True)
    id_statistic = Column(Integer, ForeignKey("statistic.id"), primary_key=True, index=True)
    bonus = Column(Integer)
