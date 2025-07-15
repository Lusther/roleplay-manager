from sqlalchemy.orm import Session
from backend.app.models.campaign import Campaign
from backend.app.schemas.campaign import *


def get_campaign(session: Session, id_campaign: int):
    return session.query(Campaign).filter(Campaign.id == id_campaign).first()


def get_campaigns(session: Session):
    return session.query(Campaign).all()


def create_campaign(session: Session, campaign: CampaignCreate):
    campaign_add = Campaign(campaign.name, campaign.id_master)
    session.add(campaign_add)
    session.commit()
    session.refresh(campaign_add)
    return campaign_add
