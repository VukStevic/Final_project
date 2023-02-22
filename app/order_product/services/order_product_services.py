from app.order_product.exceptions import OrderProductNotFoundException
from app.order_product.models import OrderProduct
from app.order_product.repositories import OrderProductRepository
from app.db.database import SessionLocal
from app.wholesaler_has_products.exceptions import WholesalerProductNotFoundException


class OrderProductServices:

    @staticmethod
    def create_order_product(order_id: str, wholesaler_product_id: str, quantity: float):
        """
        It creates an order product
        """
        with SessionLocal() as db:
            try:
                order_product_repository = OrderProductRepository(db)
                return order_product_repository.create_order_product(order_id, wholesaler_product_id, quantity)
            except WholesalerProductNotFoundException as e:
                raise e
            except Exception as e:
                raise e

    @staticmethod
    def get_all_order_products():
        """
        It gets all the order products
        """
        with SessionLocal() as db:
            order_product_repository = OrderProductRepository(db)
            return order_product_repository.get_all_order_products()

    @staticmethod
    def get_average_product_price(wholesaler_product_id):
        """
        It gets the average product price for a given wholesaler product id
        """
        try:
            with SessionLocal() as db:
                order_product_repository = OrderProductRepository(db)
                return order_product_repository.get_average_product_price(wholesaler_product_id)
        except OrderProductNotFoundException as e:
            raise e
        except ZeroDivisionError as e:
            raise e

    @staticmethod
    def get_order_product_by_order_id(order_id: str) -> list[OrderProduct]:
        """
        It gets a list of order products by order id
        """
        try:
            with SessionLocal() as db:
                order_product_repository = OrderProductRepository(db)
                return order_product_repository.get_order_product_by_order_id(order_id)
        except OrderProductNotFoundException as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def get_order_product_by_wholesaler_product_id(wholesaler_product_id: str):
        """
        It gets an order product by its wholesaler product id
        """
        try:
            with SessionLocal() as db:
                order_product_repository = OrderProductRepository(db)
                return order_product_repository.get_order_product_by_wholesaler_product_id(wholesaler_product_id)
        except OrderProductNotFoundException as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def get_order_product_by_id(id: str) -> OrderProduct:
        """
        It gets an order product by id
        """
        try:
            with SessionLocal() as db:
                order_product_repository = OrderProductRepository(db)
                return order_product_repository.get_order_product_by_id(id)
        except OrderProductNotFoundException as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def get_average_product_count_per_order():
        """
        It gets the average product count per order
        """
        try:
            with SessionLocal() as db:
                order_product_repository = OrderProductRepository(db)
                return order_product_repository.get_average_product_count_per_order()
        except ZeroDivisionError as e:
            raise e

    @staticmethod
    def get_total_wholesaler_revenue(wholesaler_id: str):
        """
        It gets the total revenue of a wholesaler by getting the sum of the total price of all the products in all the
        orders of the wholesaler
        """
        try:
            with SessionLocal() as db:
                order_product_repository = OrderProductRepository(db)
                return order_product_repository.get_total_wholesaler_revenue(wholesaler_id)
        except ZeroDivisionError as e:
            raise e

    @staticmethod
    def delete_order_product_by_order_id(order_id: str):
        """
        It deletes all order products that have the same order id as the one passed in
        """
        try:
            with SessionLocal() as db:
                order_product_repository = OrderProductRepository(db)
                return order_product_repository.delete_order_product_by_order_id(order_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_order_product(id: str, quantity: float):
        """
        It updates the quantity of an order product
        """
        try:
            with SessionLocal() as db:
                order_product_repository = OrderProductRepository(db)
                return order_product_repository.update_order_product(id, quantity)
        except OrderProductNotFoundException as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def delete_order_product_by_wholesaler_product_id(wholesaler_product_id: str):
        """
        It deletes an order product by its wholesaler product id
        """
        try:
            with SessionLocal() as db:
                order_product_repository = OrderProductRepository(db)
                return order_product_repository.delete_order_product_by_wholesaler_product_id(wholesaler_product_id)
        except Exception as e:
            raise e
