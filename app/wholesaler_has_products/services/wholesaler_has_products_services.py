from app.wholesaler_has_products.exceptions import WholesalerProductNotFoundException
from app.wholesaler_has_products.repositories import WholesalerHasProductsRepository
from app.db.database import SessionLocal


class WholesalerHasProductsServices:

    @staticmethod
    def create_wholesaler_product(wholesaler_id: str, product_id: str, price: float, quantity_available: float):
        with SessionLocal() as db:
            try:
                wholesaler_has_products_repository = WholesalerHasProductsRepository(db)
                return wholesaler_has_products_repository.create_wholesaler_product(wholesaler_id, product_id, price,
                                                                                    quantity_available)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_wholesaler_products():
        try:
            with SessionLocal() as db:
                wholesaler_has_products_repository = WholesalerHasProductsRepository(db)
                return wholesaler_has_products_repository.get_all_wholesaler_products()
        except Exception as e:
            raise e

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
    def get_wholesaler_product_by_id(id: str):
        try:
            with SessionLocal() as db:
                wholesaler_has_products_repository = WholesalerHasProductsRepository(db)
                return wholesaler_has_products_repository.get_wholesaler_product_by_id(id)
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

    @staticmethod
    def update_wholesaler_product_price(wholesaler_id: str, product_id: str, price: float):
        with SessionLocal() as db:
            try:
                wholesaler_product_repository = WholesalerHasProductsRepository(db)
                return wholesaler_product_repository.update_wholesaler_product_price(wholesaler_id, product_id, price)
            except Exception as e:
                raise e

    @staticmethod
    def update_wholesaler_product_quantity_available(wholesaler_id: str, product_id: str, quantity_available: float):
        with SessionLocal() as db:
            try:
                wholesaler_product_repository = WholesalerHasProductsRepository(db)
                return wholesaler_product_repository.update_wholesaler_product_quantity_available(wholesaler_id,
                                                                                                  product_id,
                                                                                                  quantity_available)
            except Exception as e:
                raise e

    @staticmethod
    def update_wholesaler_product(wholesaler_id: str, product_id: str, price: float, quantity_available: float):
        with SessionLocal() as db:
            try:
                wholesaler_product_repository = WholesalerHasProductsRepository(db)
                return wholesaler_product_repository.update_wholesaler_product(wholesaler_id, product_id, price,
                                                                               quantity_available)
            except WholesalerProductNotFoundException as e:
                raise e
            except Exception as e:
                raise e
