from pydantic import BaseModel, UUID4
from app.product_categories.schemas import ProductCategorySchema
from typing import Optional


class ProductSchema(BaseModel):
    id: UUID4
    name: str
    description: str
    price: float
    quantity_available: float
    product_category_id: UUID4
    product_category: ProductCategorySchema

    class Config:
        orm_mode = True


class ProductSchemaIn(BaseModel):
    name: str
    description: str
    price: float or int
    quantity_available: float or int
    product_category_id: str

    class Config:
        orm_mode = True


class ProductSchemaUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    quantity_available: Optional[float]

    class Config:
        orm_mode = True
