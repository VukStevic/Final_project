from datetime import date
from pydantic import BaseModel, UUID4
from app.wholesalers.schemas import WholesalerSchema
from app.retailers.schemas import RetailerSchema
from typing import Optional


class OrderSchema(BaseModel):
    id: UUID4
    type: str
    order_date: date
    wholesaler_id: UUID4
    retailer_id: UUID4
    wholesaler: WholesalerSchema
    retailer: RetailerSchema

    class Config:
        orm_mode = True


class OrderSchemaIn(BaseModel):
    type: str
    order_date: str
    wholesaler_id: str
    retailer_id: str

    class Config:
        orm_mode = True


class OrderSchemaUpdate(BaseModel):
    type: Optional[str]
    order_date: Optional[date]

    class Config:
        orm_mode = True


class OrderSchemaAnalytics(BaseModel):
    type: str
    order_date: date
    wholesaler_id: UUID4
    retailer_id: UUID4

    class Config:
        orm_mode = True
