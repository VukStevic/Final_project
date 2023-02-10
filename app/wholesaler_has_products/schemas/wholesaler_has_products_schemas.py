from pydantic import BaseModel, UUID4
from app.products.schemas import ProductSchema
from app.wholesalers.schemas import WholesalerSchema


class WholesalerHasProductsSchema(BaseModel):
    wholesaler_id: UUID4
    wholesaler: WholesalerSchema
    product_id: UUID4
    product: ProductSchema

    class Config:
        orm_mode = True


class WholesalerHasProductsSchemaIn(BaseModel):
    wholesaler_id: str
    product_id: str

    class Config:
        orm_mode = True

