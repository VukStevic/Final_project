from pydantic import BaseModel, UUID4
from typing import Optional
from app.payments.schemas import PaymentSchema


class PaymentStatusSchema(BaseModel):
    id: UUID4
    status_code: str
    status_description: str
    date_and_time: str
    payment_id: str
    payment: PaymentSchema

    class Config:
        orm_mode = True


class PaymentStatusSchemaIn(BaseModel):
    status_code: str
    status_description: str
    payment_id: str

    class Config:
        orm_mode = True


class PaymentStatusSchemaUpdate(BaseModel):
    id: str
    status_code: Optional[str] = None
    status_description: Optional[str] = None

    class Config:
        orm_mode = True
