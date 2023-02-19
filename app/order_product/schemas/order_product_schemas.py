from pydantic import BaseModel, UUID4
from app.orders.schemas import OrderSchema
from app.products.schemas import ProductSchema


class OrderProductSchema(BaseModel):
    id: UUID4
    order_id: str
    wholesaler_product_id: str
    quantity: float
    price: float
    # order: OrderSchema
    # product: ProductSchema

    class Config:
        orm_mode = True


class OrderProductSchemaIn(BaseModel):
    order_id: str
    wholesaler_product_id: str
    quantity: float

    class Config:
        orm_mode = True


class AveragePriceSchema(BaseModel):
    average_price: str

    class Config:
        orm_mode = True



