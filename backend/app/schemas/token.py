from pydantic import BaseModel


class TokenBase(BaseModel):
    id_map: int
    id_character: int
    pos_x: str
    pos_y: str


class TokenCreate(TokenBase):
    pass


class TokenRead(TokenBase):
    class Config:
        from_attributes = True
