from sqlalchemy.orm import Session
from app.models.character import Character
from app.schemas.character import *


def get_character(session: Session, id_character: int):
    return session.query(Character).filter(Character.id == id_character).first()


def get_characters(session: Session):
    return session.query(Character).all()


def create_character(session: Session, character: CharacterCreate):
    character_add = Character(
        name=character.name,
        id_campaign=character.id_campaign,
        id_user=character.id_user,
        id_class=character.id_class,
        bio=character.bio,
        image_path=character.image_path,
        level=character.level
    )
    session.add(character_add)
    session.commit()
    session.refresh(character_add)
    return character_add
