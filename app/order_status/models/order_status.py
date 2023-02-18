from datetime import datetime
from uuid import uuid4
from app.db import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class OrderStatus(Base):
    __tablename__ = "order_status"
    id = Column(String(90), primary_key=True, default=uuid4, autoincrement=False)
    status_code = Column(String(90))
    description = Column(String(200))
    date_and_time = Column(String(90), default=datetime.now().strftime("%d-%m-%Y, %H:%M:%S"))

    order_id = Column(String(90), ForeignKey("orders.id"))
    order = relationship("Order", lazy="subquery")

    def __init__(self, status_code: str, description: str, order_id: str):
        self.status_code = status_code
        self.description = description
        self.date_and_time = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
        self.order_id = order_id
