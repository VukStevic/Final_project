from uuid import uuid4
from sqlalchemy.orm import relationship
from app.db import Base
from sqlalchemy import Column, String, ForeignKey


class Product(Base):
    __tablename__ = "products"
    id = Column(String(90), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(90), unique=True)
    description = Column(String(200))

    product_category_id = Column(String(90), ForeignKey("product_categories.id"))
    product_category = relationship("ProductCategory", lazy="subquery")

    def __init__(self, name: str, description: str, product_category_id: str):
        self.name = name
        self.description = description
        self.product_category_id = product_category_id
        