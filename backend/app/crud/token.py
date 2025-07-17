from sqlalchemy.orm import Session
from app.models.token import Token
from app.models.map import Map
from app.models.character import Character
from app.schemas.token import *


def get_token(session: Session, id_map: int, id_character: int):
    return session.query(Token).filter(Map.id == id_map, Character.id == id_character).first()


def get_tokens_on_map(session: Session, id_map: int):
    return session.query(Token).filter(Map.id == id_map).all()


def create_token(session: Session, token: TokenCreate):
    token_add = Token(
        id_map=token.id_map,
        id_character=token.id_character,
        pos_x=token.pos_x,
        pos_y=token.pos_y
    )
    session.add(token_add)
    session.commit()
    session.refresh(token_add)
    return token_add
