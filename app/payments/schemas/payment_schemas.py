from pydantic import BaseModel, UUID4
from typing import Optional
from app.orders.schemas import OrderSchema


class PaymentSchema(BaseModel):
    id: UUID4
    payment_amount: float
    order_id: str
    # order: OrderSchema

    class Config:
        orm_mode = True


class PaymentSchemaIn(BaseModel):
    order_id: str

    class Config:
        orm_mode = True


class PaymentSchemaUpdate(BaseModel):
    payment_amount: Optional[float]

    class Config:
        orm_mode = True
