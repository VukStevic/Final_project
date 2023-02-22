from typing import Optional
from pydantic import BaseModel, UUID4, EmailStr


class UserSchema(BaseModel):
    id: UUID4
    username: str
    email: str
    password: str
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True


class UserSchemaIn(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class UserSchemaUpdate(BaseModel):
    user_id: str
    username: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None

    class Config:
        orm_mode = True
