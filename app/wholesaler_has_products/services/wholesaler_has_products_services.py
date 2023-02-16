from app.wholesaler_has_products.repositories import WholesalerHasProductsRepository
from app.db.database import SessionLocal


class WholesalerHasProductsServices:

    @staticmethod
    def create_wholesaler_product(wholesaler_id: str, product_id: str):
        with SessionLocal() as db:
            try:
                wholesaler_has_products_repository = WholesalerHasProductsRepository(db)
                return wholesaler_has_products_repository.create_wholesaler_product(wholesaler_id, product_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_wholesaler_products():
        with SessionLocal() as db:
            wholesaler_has_products_repository = WholesalerHasProductsRepository(db)
            return wholesaler_has_products_repository.get_all_wholesaler_products()

    @staticmethod
    def get_wholesaler_product_by_wholesaler_id(wholesaler_id: str):
        with SessionLocal() as db:
            wholesaler_has_products_repository = WholesalerHasProductsRepository(db)
            return wholesaler_has_products_repository.get_wholesaler_product_by_wholesaler_id(wholesaler_id)

    @staticmethod
    def get_wholesaler_product_by_product_id(product_id: str):
        try:
            with SessionLocal() as db:
                wholesaler_has_products_repository = WholesalerHasProductsRepository(db)
                return wholesaler_has_products_repository.get_wholesaler_product_by_product_id(product_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_wholesaler_product_by_wholesaler_id(wholesaler_id: str):
        try:
            with SessionLocal() as db:
                wholesaler_has_products_repository = WholesalerHasProductsRepository(db)
                return wholesaler_has_products_repository.delete_wholesaler_product_by_wholesaler_id(wholesaler_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_wholesaler_product_by_product_id(product_id: str):
        try:
            with SessionLocal() as db:
                wholesaler_has_products_repository = WholesalerHasProductsRepository(db)
                return wholesaler_has_products_repository.delete_wholesaler_product_by_product_id(product_id)
        except Exception as e:
            raise e