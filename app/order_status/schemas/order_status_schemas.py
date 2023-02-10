from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from app.orders.schemas import OrderSchema


class OrderStatusSchema(BaseModel):
    status_code: str
    description: str
    date_and_time: datetime
    order_id: str
    order: OrderSchema

    class Config:
        orm_mode = True


class OrderStatusSchemaIn(BaseModel):
    status_code: str
    description: str
    date_and_time: datetime

    class Config:
        orm_mode = True


class OrderStatusSchemaUpdate(BaseModel):
    status_code: Optional[str]
    description: Optional[str]
    date_and_time: Optional[datetime]

    class Config:
        orm_mode = True
