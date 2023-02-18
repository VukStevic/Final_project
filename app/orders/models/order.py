from datetime import datetime
from app.db import Base
from sqlalchemy import Column, String, DATE, ForeignKey
from sqlalchemy.orm import Relationship
from uuid import uuid4


class Order(Base):
    __tablename__ = "orders"
    id = Column(String(90), primary_key=True, default=uuid4, autoincrement=False)
    type = Column(String(90))
    order_date = Column(DATE())

    wholesaler_id = Column(String(90), ForeignKey("wholesalers.id"))
    wholesaler = Relationship("Wholesaler", lazy="subquery")

    retailer_id = Column(String(90), ForeignKey("retailers.id"))
    retailer = Relationship("Retailer", lazy="subquery")

    def __init__(self, type: str, order_date: str, wholesaler_id: str, retailer_id: str):
        self.type = type
        self.order_date = datetime.strptime(order_date, "%d-%m-%Y")
        self.wholesaler_id = wholesaler_id
        self.retailer_id = retailer_id
