from sqlmodel import SQLModel, Field


class UserCampaign(SQLModel, table=True):
    id_campaign: int | None = Field(default=None, foreign_key="campaign.id", primary_key=True)
    id_user: int | None = Field(default=None, foreign_key="user.id", primary_key=True)
