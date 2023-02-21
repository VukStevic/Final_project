from app.db import Base
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4
from app.order_product.services import OrderProductServices


class Payment(Base):
    __tablename__ = "payments"
    id = Column(String(90), primary_key=True, default=uuid4, autoincrement=False)
    payment_amount = Column(Float())
    order_id = Column(String(90), ForeignKey("orders.id"), unique=True)
    order = relationship("Order", lazy="subquery")

    def __init__(self, order_id: str, payment_amount: float):
        self.order_id = order_id
        self.payment_amount = payment_amount
        order_products = OrderProductServices.get_order_product_by_order_id(order_id)
        for product in order_products:
            self.payment_amount += product.price * product.quantity
