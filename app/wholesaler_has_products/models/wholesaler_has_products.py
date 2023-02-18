from uuid import uuid4
from app.db import Base
from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class WholesalerHasProducts(Base):
    __tablename__ = "wholesaler_has_products"
    id = Column(String(90), primary_key=True, default=uuid4, autoincrement=False)
    wholesaler_id = Column(String(90), ForeignKey("wholesalers.id"))
    product_id = Column(String(90), ForeignKey("products.id"))
    price = Column(Float())
    quantity_available = Column(Float())

    wholesaler = relationship("Wholesaler", lazy="subquery")
    product = relationship("Product", lazy="subquery")

    def __init__(self, wholesaler_id: str, product_id: str, price: float, quantity_available: float):
        self.wholesaler_id = wholesaler_id
        self.product_id = product_id
        self.price = price
        self.quantity_available = quantity_available
