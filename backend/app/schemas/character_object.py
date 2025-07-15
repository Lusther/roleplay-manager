from pydantic import BaseModel


class CharacterObjectBase(BaseModel):
    id_character: int
    id_object: int
    quantity: int


class CharacterObjectCreate(CharacterObjectBase):
    pass


class CharacterObjectRead(CharacterObjectBase):
    class Config:
        orm_mode = True
