from pydantic import BaseModel


class MapBase(BaseModel):
    name: str
    id_campaign: int
    image_path: str
    bio: str


class MapCreate(MapBase):
    pass


class MapRead(MapBase):
    id: int

    class Config:
        from_attributes = True
