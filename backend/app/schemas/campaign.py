from pydantic import BaseModel

class CampaignBase(BaseModel):
    name: str
    id_master: int


class CampaignCreate(CampaignBase):
    pass


class CampaignRead(CampaignBase):
    id: int

    class Config:
        from_attributes = True
