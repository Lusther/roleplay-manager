from pydantic import BaseModel


class ClasseStatisticBase(BaseModel):
    id_classe: int
    id_statistic: int
    bonus: int


class ClasseStatisticCreate(ClasseStatisticBase):
    pass


class ClasseStatisticRead(ClasseStatisticBase):
    class Config:
        orm_mode = True
