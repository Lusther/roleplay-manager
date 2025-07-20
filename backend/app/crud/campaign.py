from sqlmodel import Session, select
from app.models.campaign import Campaign, CampaignCreate, CampaignPublic


def get_campaign(session: Session, id_campaign: int):
    return session.get(Campaign, id_campaign)


def get_campaigns(session: Session):
    return session.exec(select(Campaign)).all()


def create_campaign(session: Session, campaign: CampaignCreate):
    existing_campaign = session.exec(select(Campaign).where(Campaign.name == campaign.name)).first()
    if not existing_campaign:
        db_campaign = Campaign.model_validate(campaign)
        session.add(db_campaign)
        session.commit()
        session.refresh(db_campaign)
        return db_campaign
    else:
        return None

def get_users_in_campaign(session: Session, campaign: Campaign):
    return campaign.users


def delete_campaign(session: Session, campaign: Campaign):
    session.delete(campaign)
    session.commit()


def update_campaign(session: Session, campaign: Campaign, up_campaign: Campaign):
    campaign.name = up_campaign.name
    campaign.id_master = up_campaign.id_master
    session.add(campaign)
    session.commit()
    session.refresh(campaign)
    return campaign
    