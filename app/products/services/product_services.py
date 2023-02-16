from app.products.repositories import ProductRepository
from app.db.database import SessionLocal


class ProductServices:

    @staticmethod
    def create_product(name: str, description: str, price: float, quantity_available: float, 
                       product_category_id: str):
        with SessionLocal() as db:
            try:
                product_repository = ProductRepository(db)
                return product_repository.create_product(name, description, price, quantity_available, 
                                                         product_category_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_products():
        with SessionLocal() as db:
            product_repository = ProductRepository(db)
            return product_repository.get_all_products()

    @staticmethod
    def get_product_by_id(product_id: str):
        with SessionLocal() as db:
            product_repository = ProductRepository(db)
            return product_repository.get_product_by_id(product_id)

    @staticmethod
    def get_product_by_name(name: str):
        with SessionLocal() as db:
            product_repository = ProductRepository(db)
            return product_repository.get_product_by_name(name)

    @staticmethod
    def delete_product_by_id(product_id: str):
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.delete_product_by_id(product_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_product_description(product_id: str, description: str):
        with SessionLocal() as db:
            try:
                product_repository = ProductRepository(db)
                return product_repository.update_product_description(product_id, description)
            except Exception as e:
                raise e

    @staticmethod
    def update_product_price(product_id: str, price: float):
        with SessionLocal() as db:
            try:
                product_repository = ProductRepository(db)
                product = product_repository.update_product_price(product_id, price)
                return product
            except Exception as e:
                raise e

    @staticmethod
    def update_product_quantity_available(product_id: str, quantity_available: float):
        with SessionLocal() as db:
            try:
                product_repository = ProductRepository(db)
                product = product_repository.update_product_quantity_available(product_id, quantity_available)
                return product
            except Exception as e:
                raise e