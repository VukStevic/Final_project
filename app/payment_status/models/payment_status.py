from datetime import datetime
from uuid import uuid4
from app.db import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class PaymentStatus(Base):
    __tablename__ = "payment_status"
    id = Column(String(90), primary_key=True, default=uuid4, autoincrement=False)
    status_code = Column(String(90))
    status_description = Column(String(200))
    date_and_time = Column(String(90), default=datetime.now().strftime("%d-%m-%Y, %H:%M:%S"))

    payment_id = Column(String(90), ForeignKey("payments.id"))
    payment = relationship("Payment", lazy="subquery")

    def __init__(self, status_code: str, status_description: str, payment_id: str):
        self.status_code = status_code
        self.status_description = status_description
        self.date_and_time = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
        self.payment_id = payment_id
