from sqlalchemy.orm import Session
from app.models.character_statistic import CharacterStatistic
from app.models.character import Character
from app.models.statistic import Statistic
from app.schemas.character_statistic import *


def get_character_statistic(session: Session, id_character: int, id_statistic: int):
    return session.query(CharacterStatistic).filter(Character.id == id_character, Statistic.id == id_statistic).first()


def get_statistic_of_character(session: Session, id_character: int):
    return session.query(CharacterStatistic).filter(Character.id == id_character).all()


def create_character_statistic(session: Session, character_statistic: CharacterStatisticCreate):
    character_statistic_add = CharacterStatistic(
        id_character=character_statistic.id_character,
        id_statistic=character_statistic.id_statistic,
        value_statistic=character_statistic.value_statistic
    )
    session.add(character_statistic_add)
    session.commit()
    session.refresh(character_statistic_add)
    return character_statistic_add
