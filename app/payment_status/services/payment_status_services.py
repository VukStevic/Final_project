from app.payment_status.exceptions.payment_status_exceptions import PaymentStatusNotFound
from app.payment_status.repositories import PaymentStatusRepository
from app.db.database import SessionLocal


class PaymentStatusServices:

    @staticmethod
    def create_payment_status(status_code: str, status_description: str, payment_id: str):
        """
        It creates a payment status in the database
        """
        with SessionLocal() as db:
            try:
                payment_status_repository = PaymentStatusRepository(db)
                return payment_status_repository.create_payment_status(status_code, status_description, payment_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_payment_statuses():
        """
        It gets all payment statuses from the database
        """
        with SessionLocal() as db:
            payment_status_repository = PaymentStatusRepository(db)
            return payment_status_repository.get_all_payment_statuses()

    @staticmethod
    def get_payment_status_by_id(id: str):
        """
        > This function gets a payment status by id
        """
        with SessionLocal() as db:
            payment_status_repository = PaymentStatusRepository(db)
            return payment_status_repository.get_payment_status_by_id(id)

    @staticmethod
    def get_payment_status_by_payment_id(payment_id: str):
        """
        > This function gets the payment status by payment id
        """
        with SessionLocal() as db:
            payment_status_repository = PaymentStatusRepository(db)
            return payment_status_repository.get_payment_status_by_payment_id(payment_id)

    @staticmethod
    def get_payment_status_by_date_and_time(date_and_time: str):
        """
        It gets a payment status by date and time
        """
        with SessionLocal() as db:
            payment_status_repository = PaymentStatusRepository(db)
            return payment_status_repository.get_payment_status_by_date_and_time(date_and_time)

    @staticmethod
    def delete_payment_status_by_id(id: str):
        """
        It deletes a payment status by id.
        """
        try:
            with SessionLocal() as db:
                payment_status_repository = PaymentStatusRepository(db)
                return payment_status_repository.delete_payment_status_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_payment_status_by_date_and_time(date_and_time: str):
        """
        It deletes a payment status by date and time
        """
        try:
            with SessionLocal() as db:
                payment_status_repository = PaymentStatusRepository(db)
                return payment_status_repository.delete_payment_status_by_date_and_time(date_and_time)
        except Exception as e:
            raise e

    @staticmethod
    def update_payment_status(id: str, status_code: str, status_description: str):
        """
        It updates the payment status of a payment with the given id
        """
        with SessionLocal() as db:
            try:
                payment_status_repository = PaymentStatusRepository(db)
                return payment_status_repository.update_payment_status(id, status_code, status_description)
            except PaymentStatusNotFound as e:
                raise e
            except Exception as e:
                raise e
