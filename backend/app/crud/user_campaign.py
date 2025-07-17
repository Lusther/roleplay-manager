from sqlalchemy.orm import Session
from app.models.user_campaign import UserCampaign
from app.models.campaign import Campaign
from app.models.user import User
from app.schemas.user_campaign import *


def get_user_campaign(session: Session, id_campaign: int, id_user: int):
    return session.query(UserCampaign).filter(Campaign.id == id_campaign, User.id == id_user).first()


def get_users_of_campaign(session: Session, id_campaign: int):
    return session.query(UserCampaign).filter(Campaign.id == id_campaign).all()


def get_campaigns_of_user(session: Session, id_user: int):
    return session.query(UserCampaign).filter(User.id == id_user).all()


def create_user_campaign(session: Session, user_campaign: UserCampaignCreate):
    user_campaign_add = UserCampaign(
        id_campaign=user_campaign.id_campaign,
        id_user=user_campaign.id_user
    )
    session.add(user_campaign_add)
    session.commit()
    session.refresh(user_campaign_add)
    return user_campaign_add
