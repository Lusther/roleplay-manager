from sqlalchemy.orm import Session
from backend.app.models.statistic import Statistic
from backend.app.schemas.statistic import *


def get_statistic(session: Session, id_statistic: int):
    return session.query(Statistic).filter(Statistic.id == id_statistic).first()


def get_statistics(session: Session):
    return session.query(Statistic).all()


def create_statistic(session: Session, statistic: StatisticCreate):
    statistic_add = Statistic(statistic.name, statistic.id_campaign, statistic.bio, statistic.image_path, statistic.min_value, statistic.max_value)
    session.add(statistic_add)
    session.commit()
    session.refresh(statistic_add)
    return statistic_add
