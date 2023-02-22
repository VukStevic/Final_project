from pydantic import BaseModel, UUID4
from app.product_categories.schemas import ProductCategorySchema
from typing import Optional


class ProductSchema(BaseModel):
    id: UUID4
    name: str
    description: str
    product_category_id: UUID4
    product_category: ProductCategorySchema

    class Config:
        orm_mode = True


class ProductSchemaIn(BaseModel):
    name: str
    description: str
    product_category_id: str

    class Config:
        orm_mode = True


class ProductSchemaUpdate(BaseModel):
    product_id: str
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True
