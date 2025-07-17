from pydantic import BaseModel


class CharacterBase(BaseModel):
    name: str
    id_campaign: int
    id_user: int
    id_class: int
    bio: str
    image_path: str
    level: int


class CharacterCreate(CharacterBase):
    pass


class CharacterRead(CharacterBase):
    id: int

    class Config:
        from_attributes = True
