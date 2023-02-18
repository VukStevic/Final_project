from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.payments.models import Payment


class PaymentRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_payment(self, order_id: str):
        try:
            payment = Payment(order_id=order_id)
            self.db.add(payment)
            self.db.commit()
            self.db.refresh(payment)
            return payment
        except IntegrityError as e:
            raise e

    def get_all_payments(self):
        payments = self.db.query(Payment).all()
        return payments

    def get_payment_by_id(self, payment_id: str):
        payment = self.db.query(Payment).filter(Payment.id == payment_id).first()
        return payment

    def get_payment_by_order_id(self, order_id: str):
        payment = self.db.query(Payment).filter(Payment.order_id == order_id).first()
        return payment

    def delete_payment_by_id(self, payment_id: str):
        try:
            payment = self.db.query(Payment).filter(Payment.id == payment_id).first()
            self.db.delete(payment)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def delete_payment_by_order_id(self, order_id: str):
        try:
            payment = self.db.query(Payment).filter(Payment.order_id == order_id).first()
            self.db.delete(payment)
            self.db.commit()
            return True
        except Exception as e:
            raise e
