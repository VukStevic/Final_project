from pydantic import BaseModel, UUID4
from typing import Optional


class ProductCategorySchema(BaseModel):
    id: UUID4
    name: str
    description: str

    class Config:
        orm_mode = True


class ProductCategorySchemaIn(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True


class ProductCategorySchemaUpdate(BaseModel):
    product_category_id: str
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True
