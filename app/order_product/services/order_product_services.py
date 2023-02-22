from app.order_product.exceptions import OrderProductNotFoundException
from app.order_product.models import OrderProduct
from app.order_product.repositories import OrderProductRepository
from app.db.database import SessionLocal
from app.wholesaler_has_products.exceptions import WholesalerProductNotFoundException


class OrderProductServices:

    @staticmethod
    def create_order_product(order_id: str, wholesaler_product_id: str, quantity: float):
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
        with SessionLocal() as db:
            order_product_repository = OrderProductRepository(db)
            return order_product_repository.get_all_order_products()

    @staticmethod
    def get_average_product_price(wholesaler_product_id):
        try:
            with SessionLocal() as db:
                order_product_repository = OrderProductRepository(db)
                return order_product_repository.get_average_product_price(wholesaler_product_id)
        except ZeroDivisionError as e:
            raise e

    @staticmethod
    def get_order_product_by_order_id(order_id: str) -> list[OrderProduct]:
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
        try:
            with SessionLocal() as db:
                order_product_repository = OrderProductRepository(db)
                return order_product_repository.get_average_product_count_per_order()
        except ZeroDivisionError as e:
            raise e

    @staticmethod
    def get_total_wholesaler_revenue(wholesaler_id: str):
        try:
            with SessionLocal() as db:
                order_product_repository = OrderProductRepository(db)
                return order_product_repository.get_total_wholesaler_revenue(wholesaler_id)
        except ZeroDivisionError as e:
            raise e

    @staticmethod
    def delete_order_product_by_order_id(order_id: str):
        try:
            with SessionLocal() as db:
                order_product_repository = OrderProductRepository(db)
                return order_product_repository.delete_order_product_by_order_id(order_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_order_product(id: str, quantity: float):
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
        try:
            with SessionLocal() as db:
                order_product_repository = OrderProductRepository(db)
                return order_product_repository.delete_order_product_by_wholesaler_product_id(wholesaler_product_id)
        except Exception as e:
            raise e
