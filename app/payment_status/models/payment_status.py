from datetime import datetime
from app.db import Base
from sqlalchemy import Column, String, DATETIME, ForeignKey
from sqlalchemy.orm import relationship


class PaymentStatus(Base):
    __tablename__ = "payment_status"
    status_code = Column(String(90), primary_key=True, autoincrement=False, unique=True)
    status_description = Column(String(200))
    date_and_time = Column(DATETIME())

    payment_id = Column(String(90), ForeignKey("payments.id"))
    payment = relationship("Payment", lazy="subquery")

    def __init__(self, status_code: str, status_description: str, payment_id: str,
                 date_and_time: str = datetime.now().strftime("%d-%m-%Y, %H:%M:%S"),
                 ):
        self.status_code = status_code
        self.status_description = status_description
        self.date_and_time = datetime.strptime(date_and_time, "%d-%m-%Y, %H:%M:%S")
        self.payment_id = payment_id
