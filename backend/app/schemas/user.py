from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    is_admin: bool


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    class Config:
        orm_mode = True
