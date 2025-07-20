from fastapi import APIRouter, HTTPException, Depends
from app.database import SessionDep
from app.crud.campaign import *
from app.models.campaign import CampaignCreate, CampaignPublic

router = APIRouter(
    prefix="/campaigns",
    tags=["campaigns"],
)


def get_existing_campaign(id: int, session: SessionDep):
    campaign = get_campaign(session, id)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign


# Create campaign
@router.post("/", response_model=CampaignPublic)
def create_new_campaign(campaign: CampaignCreate, session: SessionDep):
    new_campaign = create_campaign(session, campaign)
    if new_campaign != None:
        return new_campaign
    else:
        raise HTTPException(status_code=409, detail="This campaign already exist.")


# Get all campaigns
@router.get("/")
def read_campaigns(session: SessionDep):
    return get_campaigns(session)


# Get campaign by id
@router.get("/{id}")
def read_campaign(campaign: CampaignPublic = Depends(get_existing_campaign)):
    return campaign


@router.post("/{id_campaign}/users")
def read_users_in_campaign(id_campaign: int, session: SessionDep):
    campaign = get_existing_campaign(id_campaign, session)
    return get_users_in_campaign(session, campaign)


@router.delete("/{id_campaign}")
def remove_campaign(id_campaign: int, session: SessionDep):
    campaign = get_existing_campaign(id_campaign, session)
    delete_campaign(session, campaign)


# Update the campaign
@router.put("/{id_campaign}")
def put_user(id_campaign: int, up_campaign: CampaignCreate, session: SessionDep):
    user = get_existing_campaign(id_campaign, session)
    update_campaign(session, user, up_campaign)