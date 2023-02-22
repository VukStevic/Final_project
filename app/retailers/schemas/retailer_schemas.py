from typing import Optional
from pydantic import BaseModel, UUID4, EmailStr
from app.users.schemas import UserSchema


class RetailerSchema(BaseModel):
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


class RetailerSchemaIn(BaseModel):
    name: str
    hq_location: str
    landline: str
    business_email: EmailStr
    business_type_id: str
    user_id: str

    class Config:
        orm_mode = True


class RetailerSchemaUpdate(BaseModel):
    retailer_id: str
    name: Optional[str] = None
    hq_location: Optional[str] = None
    landline: Optional[str] = None
    business_email: Optional[EmailStr] = None

    class Config:
        orm_mode = True
