from app.db import Base
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4


class Payment(Base):
    __tablename__ = "payments"
    id = Column(String(90), primary_key=True, default=uuid4, autoincrement=False)
    payment_amount = Column(Float())
    order_id = Column(String(90), ForeignKey("orders.id"))
    order = relationship("Order", lazy="subquery")

    def __init__(self, payment_amount: float, order_id: str):
        self.payment_amount = payment_amount
        self.order_id = order_id

