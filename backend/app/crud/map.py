from sqlalchemy.orm import Session
from app.models.map import Map
from app.schemas.map import *


def get_map(session: Session, id_map: int):
    return session.query(Map).filter(Map.id == id_map).first()


def get_maps(session: Session):
    return session.query(Map).all()


def create_map(session: Session, map: MapCreate):
    map_add = Map(
        name=map.name,
        id_campaign=map.id_campaign,
        image_path=map.image_path,
        bio=map.bio
    )
    session.add(map_add)
    session.commit()
    session.refresh(map_add)
    return map_add
