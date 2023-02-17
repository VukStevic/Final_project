from app.payment_status.repositories import PaymentStatusRepository
from app.db.database import SessionLocal


class PaymentStatusServices:

    @staticmethod
    def create_payment_status(status_code: str, status_description: str, date_and_time: str, payment_id: str):
        with SessionLocal() as db:
            try:
                payment_status_repository = PaymentStatusRepository(db)
                return payment_status_repository.create_payment_status(status_code, status_description, date_and_time,
                                                                       payment_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_payment_statuses():
        with SessionLocal() as db:
            payment_status_repository = PaymentStatusRepository(db)
            return payment_status_repository.get_all_payment_statuses()

    @staticmethod
    def get_payment_status_by_status_code(status_code: str):
        with SessionLocal() as db:
            payment_status_repository = PaymentStatusRepository(db)
            return payment_status_repository.get_payment_status_by_status_code(status_code)

    @staticmethod
    def get_payment_status_by_date_and_time(date_and_time: str):
        with SessionLocal() as db:
            payment_status_repository = PaymentStatusRepository(db)
            return payment_status_repository.get_payment_status_by_date_and_time(date_and_time)

    @staticmethod
    def delete_payment_status_by_status_code(status_code: str):
        try:
            with SessionLocal() as db:
                payment_status_repository = PaymentStatusRepository(db)
                return payment_status_repository.delete_payment_status_by_status_code(status_code)
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
    def update_payment_status(status_code: str, new_status_code: str):
        with SessionLocal() as db:
            try:
                payment_status_repository = PaymentStatusRepository(db)
                return payment_status_repository.update_payment_status(status_code, new_status_code)
            except Exception as e:
                raise e

    @staticmethod
    def update_payment_status_description(status_code: str, status_description: str):
        with SessionLocal() as db:
            try:
                payment_status_repository = PaymentStatusRepository(db)
                payment_status = payment_status_repository.update_payment_status_description(status_code,
                                                                                             status_description)
                return payment_status
            except Exception as e:
                raise e
