from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas.user import *
from app.crud.user import *
from typing import List

print("Toto4")

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


# Create user
@router.post("/", response_model=UserRead)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    # You might want to hash the password here
    return create_user(db, user)


# Get all users
@router.get("/get_all", response_model=List[UserRead])
def read_users(db: Session = Depends(get_db)):
    print("Toto")
    return get_users(db)


# Get user by id
@router.get("/{id}", response_model=UserRead)
def read_user(id: int, db: Session = Depends(get_db)):
    user = get_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
