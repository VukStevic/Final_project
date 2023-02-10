from app.db import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class OrderProduct(Base):
    __tablename__ = "order_product"
    order_id = Column(String(90), ForeignKey("orders.id"))
    order = relationship("Order", lazy="subquery")

    product_id = Column(String(90), ForeignKey("products.id"))
    product = relationship("Product", lazy="subquery")

    def __init__(self, order_id: str, product_id: str):
        self.order_id = order_id
        self.product_id = product_id
