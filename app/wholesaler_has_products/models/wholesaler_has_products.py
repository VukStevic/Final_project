from app.db import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class WholesalerHasProducts(Base):
    __tablename__ = "wholesaler_has_products"
    wholesaler_id = Column(String(90), ForeignKey("wholesalers.id"), primary_key=True)
    product_id = Column(String(90), ForeignKey("products.id"), primary_key=True)

    wholesaler = relationship("Wholesaler", lazy="subquery")
    product = relationship("Product", lazy="subquery")

    def __init__(self, wholesaler_id: str, product_id: str):
        self.order_id = wholesaler_id
        self.product_id = product_id
