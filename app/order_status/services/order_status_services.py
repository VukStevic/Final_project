from app.order_status.repositories import OrderStatusRepository
from app.db.database import SessionLocal


class OrderStatusServices:

    @staticmethod
    def create_order_status(status_code: str, status_description: str, date_and_time: str, order_id: str):
        with SessionLocal() as db:
            try:
                order_status_repository = OrderStatusRepository(db)
                return order_status_repository.create_order_status(status_code, status_description, date_and_time,
                                                                   order_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_order_statuses():
        with SessionLocal() as db:
            order_status_repository = OrderStatusRepository(db)
            return order_status_repository.get_all_order_statuses()

    @staticmethod
    def get_order_status_by_status_code(status_code: str):
        with SessionLocal() as db:
            order_status_repository = OrderStatusRepository(db)
            return order_status_repository.get_order_status_by_status_code(status_code)

    @staticmethod
    def get_order_status_by_date_and_time(date_and_time: str):
        with SessionLocal() as db:
            order_status_repository = OrderStatusRepository(db)
            return order_status_repository.get_order_status_by_date_and_time(date_and_time)

    @staticmethod
    def delete_order_status_by_status_code(status_code: str):
        try:
            with SessionLocal() as db:
                order_status_repository = OrderStatusRepository(db)
                return order_status_repository.delete_order_status_by_status_code(status_code)
        except Exception as e:
            raise e

    @staticmethod
    def delete_order_status_by_date_and_time(date_and_time: str):
        try:
            with SessionLocal() as db:
                order_status_repository = OrderStatusRepository(db)
                return order_status_repository.delete_order_status_by_date_and_time(date_and_time)
        except Exception as e:
            raise e

    @staticmethod
    def update_order_status(status_code: str, new_status_code: str):
        with SessionLocal() as db:
            try:
                order_status_repository = OrderStatusRepository(db)
                return order_status_repository.update_order_status(status_code, new_status_code)
            except Exception as e:
                raise e

    @staticmethod
    def update_order_status_description(status_code: str, description: str):
        with SessionLocal() as db:
            try:
                order_status_repository = OrderStatusRepository(db)
                order_status = order_status_repository.update_order_status_description(status_code, description)
                return order_status
            except Exception as e:
                raise e
