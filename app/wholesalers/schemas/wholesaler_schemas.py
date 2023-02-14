from typing import Optional
from pydantic import BaseModel, UUID4, EmailStr
from app.users.schemas import UserSchema


class WholesalerSchema(BaseModel):
    id: UUID4
    name: str
    hq_location: str
    landline: str
    business_email: EmailStr
    business_type_id: UUID4
    user_id: str
    user: UserSchema

    class Config:
        orm_mode = True


class WholesalerSchemaIn(BaseModel):
    name: str
    hq_location: str
    landline: str
    business_email: EmailStr
    business_type_id: str
    user_id: str

    class Config:
        orm_mode = True


class WholesalerSchemaUpdate(BaseModel):
    name: Optional[str]
    hq_location: Optional[str]
    landline: Optional[str]
    business_email: Optional[EmailStr]
    business_type_id: Optional[str]

    class Config:
        orm_mode = True
