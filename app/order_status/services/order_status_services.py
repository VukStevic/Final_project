from app.order_status.repositories import OrderStatusRepository
from app.db.database import SessionLocal


class OrderStatusServices:

    @staticmethod
    def create_order_status(status_code: str, status_description: str, order_id: str):
        with SessionLocal() as db:
            try:
                order_status_repository = OrderStatusRepository(db)
                return order_status_repository.create_order_status(status_code, status_description, order_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_order_statuses():
        with SessionLocal() as db:
            order_status_repository = OrderStatusRepository(db)
            return order_status_repository.get_all_order_statuses()

    @staticmethod
    def get_order_status_by_id(id: str):
        with SessionLocal() as db:
            order_status_repository = OrderStatusRepository(db)
            return order_status_repository.get_order_status_by_id(id)

    @staticmethod
    def get_order_status_by_order_id(order_id: str):
        with SessionLocal() as db:
            order_status_repository = OrderStatusRepository(db)
            return order_status_repository.get_order_status_by_order_id(order_id)

    @staticmethod
    def get_order_status_by_date_and_time(date_and_time: str):
        with SessionLocal() as db:
            order_status_repository = OrderStatusRepository(db)
            return order_status_repository.get_order_status_by_date_and_time(date_and_time)

    @staticmethod
    def delete_order_status_by_id(id: str):
        try:
            with SessionLocal() as db:
                order_status_repository = OrderStatusRepository(db)
                return order_status_repository.delete_order_status_by_id(id)
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
    def update_order_status(id: str, status_code: str, description: str):
        with SessionLocal() as db:
            try:
                order_status_repository = OrderStatusRepository(db)
                return order_status_repository.update_order_status(id, status_code, description)
            except Exception as e:
                raise e

    @staticmethod
    def update_order_status_description(id: str, description: str):
        with SessionLocal() as db:
            try:
                order_status_repository = OrderStatusRepository(db)
                order_status = order_status_repository.update_order_status_description(id, description)
                return order_status
            except Exception as e:
                raise e
