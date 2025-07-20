from sqlmodel import Session, select
from app.models.user import User, UserCreate, UserPublic
from app.models.campaign import Campaign,CampaignPublic
from app.models.user_campaign import UserCampaign


def get_user(session: Session, id_user: int):
    return session.get(User, id_user)


def get_users(session: Session):
    return session.exec(select(User)).all()


def create_user(session: Session, user: UserCreate):
    existing_user = session.exec(select(User).where(User.name == user.name)).first()
    if not existing_user:
        db_user = User.model_validate(user)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
    else:
        return None


def add_user_to_campaign(session: Session, user: UserPublic, campaign: CampaignPublic):
    existing_user_campaign = session.exec(select(UserCampaign).where(UserCampaign.id_user == user.id, UserCampaign.id_campaign == campaign.id)).first()
    if not existing_user_campaign:
        user_campaign = UserCampaign(id_user=user.id, id_campaign=campaign.id)
        session.add(user_campaign)
        session.commit()
        session.refresh(user_campaign)
        return user_campaign
    else:
        return None


def get_campaigns_for_user(session: Session, user: User):
    return user.campaigns


def delete_user(session: Session, user: User):
    session.delete(user)
    session.commit()


def update_user(session: Session, user: User, up_user: User):
    user.name = up_user.name
    user.password = up_user.password
    user.is_admin = up_user.is_admin
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

