from typing import Optional

from pydantic import BaseModel, UUID4
from app.products.schemas import ProductSchema
from app.wholesalers.schemas import WholesalerSchema


class WholesalerHasProductsSchema(BaseModel):
    id: UUID4
    wholesaler_id: UUID4
    wholesaler: WholesalerSchema
    product_id: UUID4
    product: ProductSchema
    price: float
    quantity_available: float

    class Config:
        orm_mode = True


class WholesalerHasProductsSchemaIn(BaseModel):
    wholesaler_id: str
    product_id: str
    price: float
    quantity_available: float

    class Config:
        orm_mode = True


class WholesalerHasProductsSchemaUpdate(BaseModel):
    id: str
    wholesaler_id: str
    product_id: str
    price: Optional[float] = None
    quantity_available: Optional[float] = None

    class Config:
        orm_mode = True
