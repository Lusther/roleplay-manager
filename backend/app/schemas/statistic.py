from pydantic import BaseModel


class StatisticBase(BaseModel):
    name: str
    id_campaign: int
    image_path: str
    bio: str
    min_value: int
    max_value: int


class StatisticCreate(StatisticBase):
    pass


class StatisticRead(StatisticBase):
    id: int

    class Config:
        orm_mode = True
