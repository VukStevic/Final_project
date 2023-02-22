from typing import Optional
from pydantic import BaseModel, UUID4, EmailStr
from app.users.schemas import UserSchema


class WholesalerSchema(BaseModel):
    id: UUID4
    name: str
    hq_location: str
    landline: str
    business_email: str
    business_type_id: UUID4
    user_id: UUID4
    user: UserSchema

    class Config:
        orm_mode = True


class WholesalerSchemaIn(BaseModel):
    name: str
    hq_location: str
    landline: str
    business_email: str
    business_type_id: str
    user_id: str

    class Config:
        orm_mode = True


class WholesalerSchemaUpdate(BaseModel):
    wholesaler_id: str
    name: Optional[str] = None
    landline: Optional[str] = None
    business_email: Optional[EmailStr] = None
    hq_location: Optional[str] = None

    class Config:
        orm_mode = True
