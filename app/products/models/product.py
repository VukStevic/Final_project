from app.db import Base
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "products"
    id = Column(String(90), primary_key=True, autoincrement=False)
    name = Column(String(90), unique=True)
    description = Column(String(200))
    price = Column(Float)
    quantity_available = Column(Float)

    # product_category_id = Column(String(90), ForeignKey("product_categories.id"))
    # product_category = relationship("ProductCategory", lazy="subquery")

    def __init__(self, name: str, description: str, price: float, quantity_available: float, product_category_id: str):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_available = quantity_available
        self.product_category_id = product_category_id
        