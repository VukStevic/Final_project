from typing import Optional
from pydantic import BaseModel, UUID4
from app.users.schemas import UserSchema


class AdministratorSchema(BaseModel):
    id: UUID4
    name: str
    surname: str
    user_id: str
    user: UserSchema

    class Config:
        orm_mode = True


class AdministratorSchemaIn(BaseModel):
    name: str
    surname: str

    class Config:
        orm_mode = True


class AdministratorSchemaUpdate(BaseModel):
    name: Optional[str]
    surname: Optional[str]

    class Config:
        orm_mode = True
