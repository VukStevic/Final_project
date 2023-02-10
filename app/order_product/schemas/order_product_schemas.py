from pydantic import BaseModel
from app.orders.schemas import OrderSchema
from app.products.schemas import ProductSchema


class OrderProductSchema(BaseModel):
    order_id: str
    order: OrderSchema
    product_id: str
    product: ProductSchema

    class Config:
        orm_mode = True


class OrderProductSchemaIn(BaseModel):
    order_id: str
    product_id: str

    class Config:
        orm_mode = True

