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
    name: Optional[str]
    description: Optional[str]

    class Config:
        orm_mode = True
