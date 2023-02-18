from app.payment_status.repositories import PaymentStatusRepository
from app.db.database import SessionLocal


class PaymentStatusServices:

    @staticmethod
    def create_payment_status(status_code: str, status_description: str, payment_id: str):
        with SessionLocal() as db:
            try:
                payment_status_repository = PaymentStatusRepository(db)
                return payment_status_repository.create_payment_status(status_code, status_description, payment_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_payment_statuses():
        with SessionLocal() as db:
            payment_status_repository = PaymentStatusRepository(db)
            return payment_status_repository.get_all_payment_statuses()

    @staticmethod
    def get_payment_status_by_id(id: str):
        with SessionLocal() as db:
            payment_status_repository = PaymentStatusRepository(db)
            return payment_status_repository.get_payment_status_by_id(id)

    @staticmethod
    def get_payment_status_by_date_and_time(date_and_time: str):
        with SessionLocal() as db:
            payment_status_repository = PaymentStatusRepository(db)
            return payment_status_repository.get_payment_status_by_date_and_time(date_and_time)

    @staticmethod
    def delete_payment_status_by_id(id: str):
        try:
            with SessionLocal() as db:
                payment_status_repository = PaymentStatusRepository(db)
                return payment_status_repository.delete_payment_status_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_payment_status_by_date_and_time(date_and_time: str):
        try:
            with SessionLocal() as db:
                payment_status_repository = PaymentStatusRepository(db)
                return payment_status_repository.delete_payment_status_by_date_and_time(date_and_time)
        except Exception as e:
            raise e

    @staticmethod
    def update_payment_status(id: str, status_code: str):
        with SessionLocal() as db:
            try:
                payment_status_repository = PaymentStatusRepository(db)
                return payment_status_repository.update_payment_status(id, status_code)
            except Exception as e:
                raise e

    @staticmethod
    def update_payment_status_description(id: str, status_description: str):
        with SessionLocal() as db:
            try:
                payment_status_repository = PaymentStatusRepository(db)
                payment_status = payment_status_repository.update_payment_status_description(id, status_description)
                return payment_status
            except Exception as e:
                raise e
