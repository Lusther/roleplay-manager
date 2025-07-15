from sqlalchemy import Column, Integer, ForeignKey
from database import Base


class UserCampaign(Base):
    __tablename__ = "user_campaign"
    id_campaign = Column(Integer, ForeignKey("campaign.id"), primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("user.id"), primary_key=True, index=True)
