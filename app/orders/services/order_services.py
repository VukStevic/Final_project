from app.orders.exceptions import OrderNotFoundException
from app.orders.repositories import OrderRepository
from app.db.database import SessionLocal


class OrderServices:

    @staticmethod
    def create_order(type: str, order_date: str, wholesaler_id: str, retailer_id: str):
        """
        It creates an order
        """
        with SessionLocal() as db:
            try:
                order_repository = OrderRepository(db)
                return order_repository.create_order(type, order_date, wholesaler_id, retailer_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_orders():
        """
        It gets all the orders from the database
        """
        with SessionLocal() as db:
            order_repository = OrderRepository(db)
            return order_repository.get_all_orders()

    @staticmethod
    def get_order_by_id(order_id: str):
        """
        > This function gets an order by its id
        """
        with SessionLocal() as db:
            order_repository = OrderRepository(db)
            return order_repository.get_order_by_id(order_id)

    @staticmethod
    def get_order_by_wholesaler_id(wholesaler_id: str):
        """
        It gets an order by wholesaler id
        """
        with SessionLocal() as db:
            order_repository = OrderRepository(db)
            return order_repository.get_order_by_wholesaler_id(wholesaler_id)

    @staticmethod
    def get_order_by_retailer_id(retailer_id: str):
        """
        > This function gets an order by retailer id
        """
        with SessionLocal() as db:
            order_repository = OrderRepository(db)
            return order_repository.get_order_by_retailer_id(retailer_id)

    @staticmethod
    def get_order_by_wholesaler_and_date_range(wholesaler_id: str, starting_date: str, ending_date: str):
        """
        > This function returns a list of orders for a given wholesaler and date range
        """
        with SessionLocal() as db:
            order_repository = OrderRepository(db)
            return order_repository.get_order_by_wholesaler_and_date_range(wholesaler_id, starting_date, ending_date)

    @staticmethod
    def get_order_by_retailer_and_date_range(retailer_id: str, starting_date: str, ending_date: str):
        """
        > This function gets all the orders for a retailer within a date range
        """
        with SessionLocal() as db:
            order_repository = OrderRepository(db)
            return order_repository.get_order_by_retailer_and_date_range(retailer_id, starting_date, ending_date)

    @staticmethod
    def delete_order_by_id(order_id: str):
        """
        It deletes an order from the database by its id
        """
        try:
            with SessionLocal() as db:
                order_repository = OrderRepository(db)
                return order_repository.delete_order_by_id(order_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_order(order_id: str, type: str, order_date: str):
        """
        It updates an order in the database
        """
        with SessionLocal() as db:
            try:
                order_repository = OrderRepository(db)
                order = order_repository.update_order(order_id, type, order_date)
                return order
            except OrderNotFoundException as e:
                raise e
            except Exception as e:
                raise e
