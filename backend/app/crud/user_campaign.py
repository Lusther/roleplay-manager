from sqlalchemy.orm import Session
from backend.app.models.user_campaign import UserCampaign
from backend.app.models.campaign import Campaign
from backend.app.models.user import User
from backend.app.schemas.user_campaign import *


def get_user_campaign(session: Session, id_campaign: int, id_user: int):
    return session.query(UserCampaign).filter(Campaign.id == id_campaign, User.id == id_user).first()


def get_users_of_campaign(session: Session, id_campaign: int):
    return session.query(UserCampaign).filter(Campaign.id == id_campaign).all()


def get_campaigns_of_user(session: Session, id_user: int):
    return session.query(UserCampaign).filter(User.id == id_user).all()


def create_user_campaign(session: Session, user_campaign: UserCampaignCreate):
    user_campaign_add = UserCampaign(user_campaign.id_campaign, user_campaign.id_users)
    session.add(user_campaign_add)
    session.commit()
    session.refresh(user_campaign_add)
    return user_campaign_add
