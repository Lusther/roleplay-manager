from sqlalchemy.orm import Session
from backend.app.models.token import Token
from backend.app.models.map import Map
from backend.app.models.character import Character
from backend.app.schemas.token import *


def get_token(session: Session, id_map: int, id_character: int):
    return session.query(Token).filter(Map.id == id_map, Character.id == id_character).first()


def get_tokens_on_map(session: Session, id_map: int):
    return session.query(Token).filter(Map.id == id_map).all()


def create_token(session: Session, token: TokenCreate):
    token_add = Token(token.id_map, token.id_character, token.pos_x, token.pos_y)
    session.add(token_add)
    session.commit()
    session.refresh(token_add)
    return token_add
