from app.order_status.exceptions import OrderStatusNotFound
from app.order_status.repositories import OrderStatusRepository
from app.db.database import SessionLocal


class OrderStatusServices:

    @staticmethod
    def create_order_status(status_code: str, status_description: str, order_id: str):
        """
        It creates an order status
        """
        with SessionLocal() as db:
            try:
                order_status_repository = OrderStatusRepository(db)
                return order_status_repository.create_order_status(status_code, status_description, order_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_order_statuses():
        """
        It gets all the order statuses from the database
        """
        with SessionLocal() as db:
            order_status_repository = OrderStatusRepository(db)
            return order_status_repository.get_all_order_statuses()

    @staticmethod
    def get_order_status_by_id(id: str):
        """
        > This function gets an order status by id
        """
        with SessionLocal() as db:
            order_status_repository = OrderStatusRepository(db)
            return order_status_repository.get_order_status_by_id(id)

    @staticmethod
    def get_order_status_by_order_id(order_id: str):
        """
        > This function gets the order status by order id
        """
        with SessionLocal() as db:
            order_status_repository = OrderStatusRepository(db)
            return order_status_repository.get_order_status_by_order_id(order_id)

    @staticmethod
    def get_order_status_by_date_and_time(date_and_time: str):
        """
        It gets the order status by date and time
        """
        with SessionLocal() as db:
            order_status_repository = OrderStatusRepository(db)
            return order_status_repository.get_order_status_by_date_and_time(date_and_time)

    @staticmethod
    def delete_order_status_by_id(id: str):
        """
        It deletes an order status by id
        """
        try:
            with SessionLocal() as db:
                order_status_repository = OrderStatusRepository(db)
                return order_status_repository.delete_order_status_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_order_status_by_date_and_time(date_and_time: str):
        """
        It deletes an order status by date and time
        """
        try:
            with SessionLocal() as db:
                order_status_repository = OrderStatusRepository(db)
                return order_status_repository.delete_order_status_by_date_and_time(date_and_time)
        except Exception as e:
            raise e

    @staticmethod
    def update_order_status(id: str, status_code: str, description: str):
        """
        It updates the order status of an order with the given id
        """
        with SessionLocal() as db:
            try:
                order_status_repository = OrderStatusRepository(db)
                return order_status_repository.update_order_status(id, status_code, description)
            except OrderStatusNotFound as e:
                raise e
            except Exception as e:
                raise e
