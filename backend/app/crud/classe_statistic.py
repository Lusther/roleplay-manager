from sqlalchemy.orm import Session
from app.models.classe_statistic import ClasseStatistic
from app.models.classe import Classe
from app.models.statistic import Statistic
from app.schemas.classe_statistic import *


def get_classe_statistic(session: Session, id_classe: int, id_statistic: int):
    return session.query(ClasseStatistic).filter(Classe.id == id_classe, Statistic.id == id_statistic).first()


def get_statistic_of_classe(session: Session, id_classe: int):
    return session.query(ClasseStatistic).filter(Classe.id == id_classe).all()


def create_classe_statistic(session: Session, classe_statistic: ClasseStatisticCreate):
    classe_statistic_add = ClasseStatistic(
        id_classe=classe_statistic.id_classe,
        id_statistic=classe_statistic.id_statistic,
        bonus=classe_statistic.bonus
    )
    session.add(classe_statistic_add)
    session.commit()
    session.refresh(classe_statistic_add)
    return classe_statistic_add
