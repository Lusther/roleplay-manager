from pydantic import BaseModel


class ClasseBase(BaseModel):
    id_campaign: int
    name: int
    bio: int
    image_path: str


class ClasseCreate(ClasseBase):
    pass


class ClasseRead(ClasseBase):
    id: int

    class Config:
        from_attributes = True
