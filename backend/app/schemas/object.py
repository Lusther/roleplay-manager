from pydantic import BaseModel


class ObjectBase(BaseModel):
    name: str
    id_campaign: int
    image_path: str
    bio: str


class ObjectCreate(ObjectBase):
    pass


class ObjectRead(ObjectBase):
    id: int

    class Config:
        from_attributes = True
