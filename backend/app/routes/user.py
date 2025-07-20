from fastapi import APIRouter, HTTPException, Depends
from app.database import SessionDep
from app.crud.user import *
from app.models.user import UserCreate, UserPublic
from app.models.campaign import CampaignPublic
from app.routes.campaign import get_existing_campaign


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


def get_existing_user(id: int, session: SessionDep):
    user = get_user(session, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# Create user
@router.post("/", response_model=UserPublic)
def create_new_user(user: UserCreate, session: SessionDep):
    new_user = create_user(session, user)
    if new_user != None:
        return new_user
    else:
        raise HTTPException(status_code=409, detail="This user already exist.")


# Get all users
@router.get("/")
def read_users(session: SessionDep):
    return get_users(session)


# Get user by id
@router.get("/{id}")
def read_user(user: UserPublic = Depends(get_existing_user)):
    return user


@router.post("/{id_user}/join_campaign/{id_campaign}")
def join_campaign(id_user: int, id_campaign: int, session: SessionDep):
    user = get_existing_user(id_user, session)
    campaign = get_existing_campaign(id_campaign, session)
    new_user_campaign = add_user_to_campaign(session, user, campaign)
    if new_user_campaign != None:
        return new_user_campaign
    else:
        raise HTTPException(status_code=409, detail="This user is already in this campaign.")


@router.post("/{id_user}/campaigns")
def read_campaigns_for_user(id_user: int, session: SessionDep):
    user = get_existing_user(id_user, session)
    return get_campaigns_for_user(session, user)


@router.delete("/{id_user}")
def remove_user(id_user: int, session: SessionDep):
    user = get_existing_user(id_user, session)
    delete_user(session, user)
