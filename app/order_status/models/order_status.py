from datetime import datetime
from app.db import Base
from sqlalchemy import Column, String, DATETIME, ForeignKey
from sqlalchemy.orm import relationship


class OrderStatus(Base):
    __tablename__ = "order_status"
    status_code = Column(String(90), primary_key=True, autoincrement=False)
    description = Column(String(200))
    date_and_time = Column(DATETIME())

    order_id = Column(String(90), ForeignKey("orders.id"))
    order = relationship("Order", lazy="subquery")

    def __init__(self, status_code: str, status_description: str, order_id: str,
                 date_and_time: str = datetime.now().strftime("%d-%m-%Y, %H:%M:%S"),
                 ):
        self.status_code = status_code
        self.status_description = status_description
        self.date_and_time = datetime.strptime(date_and_time, "%d-%m-%Y, %H:%M:%S")
        self.order_id = order_id
