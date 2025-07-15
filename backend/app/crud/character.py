from sqlalchemy.orm import Session
from backend.app.models.character import Character
from backend.app.schemas.character import *


def get_character(session: Session, id_character: int):
    return session.query(Character).filter(Character.id == id_character).first()


def get_characters(session: Session):
    return session.query(Character).all()


def create_character(session: Session, character: CharacterCreate):
    character_add = Character(character.name, character.id_campaign, character.id_user, character.id_class, character.bio, character.image_path, character.level)
    session.add(character_add)
    session.commit()
    session.refresh(character_add)
    return character_add
