from app.orders.repositories import OrderRepository
from app.db.database import SessionLocal


class OrderServices:

    @staticmethod
    def create_order(type: str, order_date: str, wholesaler_id: str, retailer_id: str):
        with SessionLocal() as db:
            try:
                order_repository = OrderRepository(db)
                return order_repository.create_order(type, order_date, wholesaler_id, retailer_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_orders():
        with SessionLocal() as db:
            order_repository = OrderRepository(db)
            return order_repository.get_all_orders()

    @staticmethod
    def get_order_by_id(order_id: str):
        with SessionLocal() as db:
            order_repository = OrderRepository(db)
            return order_repository.get_order_by_id(order_id)

    @staticmethod
    def delete_order_by_id(order_id: str):
        try:
            with SessionLocal() as db:
                order_repository = OrderRepository(db)
                return order_repository.delete_order_by_id(order_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_order_type(order_id: str, type: str):
        with SessionLocal() as db:
            try:
                order_repository = OrderRepository(db)
                return order_repository.update_order_type(order_id, type)
            except Exception as e:
                raise e

    @staticmethod
    def update_order_date(order_id: str, order_date: str):
        with SessionLocal() as db:
            try:
                order_repository = OrderRepository(db)
                order = order_repository.update_order_date(order_id, order_date)
                return order
            except Exception as e:
                raise e
