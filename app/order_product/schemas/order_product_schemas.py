from typing import Optional
from pydantic import BaseModel, UUID4


class OrderProductSchema(BaseModel):
    id: UUID4
    order_id: str
    wholesaler_product_id: str
    quantity: float
    price: float

    class Config:
        orm_mode = True


class OrderProductSchemaIn(BaseModel):
    order_id: str
    wholesaler_product_id: str
    quantity: float

    class Config:
        orm_mode = True


class OrderProductSchemaUpdate(BaseModel):
    id: str
    quantity: Optional[float] = None

    class Config:
        orm_mode = True


class AveragePriceSchema(BaseModel):
    average_price: str

    class Config:
        orm_mode = True
