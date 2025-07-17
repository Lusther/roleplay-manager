from pydantic import BaseModel


class UserCampaignBase(BaseModel):
    id_campaign: int
    id_user: int


class UserCampaignCreate(UserCampaignBase):
    pass


class UserCampaignRead(UserCampaignBase):
    class Config:
        from_attributes = True
