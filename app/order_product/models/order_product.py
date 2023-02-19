from uuid import uuid4
from app.db import Base
from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.wholesaler_has_products.services import WholesalerHasProductsServices


class OrderProduct(Base):
    __tablename__ = "order_product"
    id = Column(String(90), primary_key=True, default=uuid4, autoincrement=False)
    order_id = Column(String(90), ForeignKey("orders.id"))
    wholesaler_product_id = Column(String(90), ForeignKey("wholesaler_has_products.id"))
    price = Column(Float())
    quantity = Column(Float())

    order = relationship("Order", lazy="subquery")
    product = relationship("WholesalerHasProducts", lazy="subquery")
#

    def __init__(self, order_id: str, wholesaler_product_id: str, quantity: float):
        self.order_id = order_id
        self.wholesaler_product_id = wholesaler_product_id
        wholesaler_product = WholesalerHasProductsServices.get_wholesaler_product_by_id(wholesaler_product_id)
        self.price = wholesaler_product.price
        self.quantity = quantity
