from sqlmodel import SQLModel, Field, Relationship
from app.models.user_campaign import UserCampaign

class UserBase(SQLModel):
    name: str
    password: str
    is_admin: bool


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    campaigns: list["Campaign"] = Relationship(back_populates="users", link_model=UserCampaign)


class UserCreate(UserBase):
    pass


class UserPublic(UserBase):
    id: int
