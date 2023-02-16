from uuid import uuid4
from app.db import Base
from sqlalchemy import Column, String


class ProductCategory(Base):
    __tablename__ = "product_categories"
    id = Column(String(90), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(90), unique=True)
    description = Column(String(200))

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
