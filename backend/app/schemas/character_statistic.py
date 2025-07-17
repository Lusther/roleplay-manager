from pydantic import BaseModel


class CharacterStatisticBase(BaseModel):
    id_character: int
    id_statistic: int
    value_statistic: int


class CharacterStatisticCreate(CharacterStatisticBase):
    pass


class CharacterStatisticRead(CharacterStatisticBase):
    class Config:
        from_attributes = True
