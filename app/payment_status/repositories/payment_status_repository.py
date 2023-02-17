import datetime

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.payment_status.models import PaymentStatus


class PaymentStatusRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_payment_status(self, status_code: str, status_description: str, date_and_time: str, payment_id: str):
        try:
            payment_status = PaymentStatus(status_code, status_description, date_and_time, payment_id)
            self.db.add(payment_status)
            self.db.commit()
            self.db.refresh(payment_status)
            return payment_status
        except IntegrityError as e:
            raise e

    def get_all_payment_statuses(self):
        payment_statuses = self.db.query(PaymentStatus).all()
        return payment_statuses

    def get_payment_status_by_status_code(self, status_code: str):
        payment_status = self.db.query(PaymentStatus).filter(PaymentStatus.status_code == status_code).first()
        return payment_status

    def get_payment_status_by_date_and_time(self, date_and_time: str):
        payment_status = self.db.query(PaymentStatus).filter(PaymentStatus.date_and_time == date_and_time).first()
        return payment_status

    def delete_payment_status_by_status_code(self, status_code: str):
        try:
            payment_status = self.db.query(PaymentStatus).filter(PaymentStatus.status_code == status_code).first()
            self.db.delete(payment_status)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def delete_payment_status_by_date_and_time(self, date_and_time: str):
        try:
            payment_status = self.db.query(PaymentStatus).filter(PaymentStatus.date_and_time == date_and_time).first()
            self.db.delete(payment_status)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_payment_status(self, status_code: str, new_status_code: str):
        try:
            payment_status = self.db.query(PaymentStatus).filter(PaymentStatus.status_code == status_code).first()
            payment_status.status_code = new_status_code
            payment_status.date_and_time = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
            self.db.add(payment_status)
            self.db.commit()
            self.db.refresh(payment_status)
            return payment_status
        except Exception as e:
            raise e

    def update_payment_status_description(self, status_code: str, status_description: str):
        try:
            payment_status = self.db.query(PaymentStatus).filter(PaymentStatus.status_code == status_code).first()
            payment_status.status_description = status_description
            self.db.add(payment_status)
            self.db.commit()
            self.db.refresh(payment_status)
            return payment_status
        except Exception as e:
            raise e
