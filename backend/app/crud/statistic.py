from sqlalchemy.orm import Session
from app.models.statistic import Statistic
from app.schemas.statistic import *


def get_statistic(session: Session, id_statistic: int):
    return session.query(Statistic).filter(Statistic.id == id_statistic).first()


def get_statistics(session: Session):
    return session.query(Statistic).all()


def create_statistic(session: Session, statistic: StatisticCreate):
    statistic_add = Statistic(
        name=statistic.name,
        id_campaign=statistic.id_campaign,
        bio=statistic.bio,
        image_path=statistic.image_path,
        min_value=statistic.min_value,
        max_value=statistic.max_value
    )
    session.add(statistic_add)
    session.commit()
    session.refresh(statistic_add)
    return statistic_add
