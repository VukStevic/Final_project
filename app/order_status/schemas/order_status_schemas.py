
from pydantic import BaseModel, UUID4
from typing import Optional
from app.orders.schemas import OrderSchema


class OrderStatusSchema(BaseModel):
    id: UUID4
    status_code: str
    description: str
    date_and_time: str
    order_id: str
    order: OrderSchema

    class Config:
        orm_mode = True


class OrderStatusSchemaIn(BaseModel):
    status_code: str
    description: str
    order_id: str

    class Config:
        orm_mode = True


class OrderStatusSchemaUpdate(BaseModel):
    id: str
    status_code: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True
