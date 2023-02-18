from app.order_product.models import OrderProduct
from app.order_product.repositories import OrderProductRepository
from app.db.database import SessionLocal


class OrderProductServices:

    @staticmethod
    def create_order_product(order_id: str, product_id: str, quantity: float):
        with SessionLocal() as db:
            try:
                order_product_repository = OrderProductRepository(db)
                return order_product_repository.create_order_product(order_id, product_id, quantity)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_order_products():
        with SessionLocal() as db:
            order_product_repository = OrderProductRepository(db)
            return order_product_repository.get_all_order_products()

    @staticmethod
    def get_order_product_by_order_id(order_id: str) -> list[OrderProduct]:
        with SessionLocal() as db:
            order_product_repository = OrderProductRepository(db)
            return order_product_repository.get_order_product_by_order_id(order_id)

    @staticmethod
    def get_order_product_by_product_id(product_id: str):
        try:
            with SessionLocal() as db:
                order_product_repository = OrderProductRepository(db)
                return order_product_repository.get_order_product_by_product_id(product_id)
        except Exception as e:
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
    def delete_order_product_by_product_id(product_id: str):
        try:
            with SessionLocal() as db:
                order_product_repository = OrderProductRepository(db)
                return order_product_repository.delete_order_product_by_product_id(product_id)
        except Exception as e:
            raise e
