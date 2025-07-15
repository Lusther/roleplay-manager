from sqlalchemy.orm import Session
from backend.app.models.map import Map
from backend.app.schemas.map import *


def get_map(session: Session, id_map: int):
    return session.query(Map).filter(Map.id == id_map).first()


def get_maps(session: Session):
    return session.query(Map).all()


def create_map(session: Session, map: MapCreate):
    map_add = Map(map.name, map.id_campaign, map.image_path, map.bio)
    session.add(map_add)
    session.commit()
    session.refresh(map_add)
    return map_add
