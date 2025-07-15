from sqlalchemy.orm import Session
from backend.app.models.classe import Classe
from backend.app.schemas.classe import *


def get_classe(session: Session, id_classe: int):
    return session.query(Classe).filter(Classe.id == id_classe).first()


def get_classes(session: Session):
    return session.query(Classe).all()


def create_classe(session: Session, classe: ClasseCreate):
    classe_add = Classe(classe.id_campaign, classe.name, classe.bio, classe.image_path)
    session.add(classe_add)
    session.commit()
    session.refresh(classe_add)
    return classe_add
