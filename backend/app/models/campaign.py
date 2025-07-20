from sqlmodel import SQLModel, Field, Relationship
from app.models.user_campaign import UserCampaign

class CampaignBase(SQLModel):
    name: str
    id_master: int | None = Field(default=None, foreign_key="user.id")


class Campaign(CampaignBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    users: list["User"] = Relationship(back_populates="campaigns", link_model=UserCampaign)


class CampaignCreate(CampaignBase):
    pass


class CampaignPublic(CampaignBase):
    id: int