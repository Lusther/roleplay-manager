from sqlalchemy.orm import Session
from app.models.campaign import Campaign
from app.schemas.campaign import *


def get_campaign(session: Session, id_campaign: int):
    return session.query(Campaign).filter(Campaign.id == id_campaign).first()


def get_campaigns(session: Session):
    return session.query(Campaign).all()


def create_campaign(session: Session, campaign: CampaignCreate):
    campaign_add = Campaign(
        name=campaign.name,
        id_master=campaign.id_master
    )
    session.add(campaign_add)
    session.commit()
    session.refresh(campaign_add)
    return campaign_add
