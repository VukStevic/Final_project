import datetime

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.payment_status.exceptions.payment_status_exceptions import PaymentStatusNotFound
from app.payment_status.models import PaymentStatus


class PaymentStatusRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_payment_status(self, status_code: str, status_description: str, payment_id: str):
        """
        It creates a new payment status and returns it
        """
        try:
            payment_status = PaymentStatus(status_code, status_description, payment_id)
            self.db.add(payment_status)
            self.db.commit()
            self.db.refresh(payment_status)
            return payment_status
        except IntegrityError as e:
            raise e

    def get_all_payment_statuses(self):
        """
        It returns all the payment statuses from the database
        """
        payment_statuses = self.db.query(PaymentStatus).all()
        return payment_statuses

    def get_payment_status_by_id(self, id: str):
        """
        It returns a payment status object from the database, given an id
        """
        payment_status = self.db.query(PaymentStatus).filter(PaymentStatus.id == id).first()
        return payment_status

    def get_payment_status_by_payment_id(self, payment_id: str):
        """
        It returns the payment status of a payment with a given payment id
        """
        payment_status = self.db.query(PaymentStatus).filter(PaymentStatus.payment_id == payment_id).first()
        return payment_status

    def get_payment_status_by_date_and_time(self, date_and_time: str):
        """
        It returns a payment status object from the database, given a date and time
        """
        payment_status = self.db.query(PaymentStatus).filter(PaymentStatus.date_and_time == date_and_time).first()
        return payment_status

    def delete_payment_status_by_id(self, id: str):
        """
        It deletes a payment status from the database by its id
        """
        try:
            payment_status = self.db.query(PaymentStatus).filter(PaymentStatus.id == id).first()
            self.db.delete(payment_status)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def delete_payment_status_by_date_and_time(self, date_and_time: str):
        """
        It deletes a payment status from the database by date and time
        """
        try:
            payment_status = self.db.query(PaymentStatus).filter(PaymentStatus.date_and_time == date_and_time).first()
            self.db.delete(payment_status)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_payment_status(self, id: str, status_code: str, status_description: str):
        """
        It updates the payment status of a payment with the given id, if the payment status exists
        """
        payment_status = self.db.query(PaymentStatus).filter(PaymentStatus.id == id).first()
        if not payment_status:
            raise PaymentStatusNotFound(code=400, message=f"Payment status with provided id: {id} not found.")
        payment_status.date_and_time = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
        if status_code is not None:
            payment_status.status_code = status_code
        if status_description is not None:
            payment_status.status_description = status_description
        self.db.add(payment_status)
        self.db.commit()
        self.db.refresh(payment_status)
        return payment_status
