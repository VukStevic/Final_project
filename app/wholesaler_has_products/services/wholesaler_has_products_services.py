from app.wholesaler_has_products.exceptions import WholesalerProductNotFoundException
from app.wholesaler_has_products.repositories import WholesalerHasProductsRepository
from app.db.database import SessionLocal


class WholesalerHasProductsServices:

    @staticmethod
    def create_wholesaler_product(wholesaler_id: str, product_id: str, price: float, quantity_available: float):
        """
        It creates a new wholesaler product
        """
        with SessionLocal() as db:
            try:
                wholesaler_has_products_repository = WholesalerHasProductsRepository(db)
                return wholesaler_has_products_repository.create_wholesaler_product(wholesaler_id, product_id, price,
                                                                                    quantity_available)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_wholesaler_products():
        """
        It gets all the wholesaler products
        """
        try:
            with SessionLocal() as db:
                wholesaler_has_products_repository = WholesalerHasProductsRepository(db)
                return wholesaler_has_products_repository.get_all_wholesaler_products()
        except Exception as e:
            raise e

    @staticmethod
    def get_wholesaler_product_by_wholesaler_id(wholesaler_id: str):
        """
        It gets all the products that belong to a wholesaler by the wholesaler's id
        """
        with SessionLocal() as db:
            wholesaler_has_products_repository = WholesalerHasProductsRepository(db)
            return wholesaler_has_products_repository.get_wholesaler_product_by_wholesaler_id(wholesaler_id)

    @staticmethod
    def get_wholesaler_product_by_product_id(product_id: str):
        """
        It gets a wholesaler product by product id
        """
        try:
            with SessionLocal() as db:
                wholesaler_has_products_repository = WholesalerHasProductsRepository(db)
                return wholesaler_has_products_repository.get_wholesaler_product_by_product_id(product_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_wholesaler_product_by_id(id: str):
        """
        It gets a wholesaler product by id
        """
        try:
            with SessionLocal() as db:
                wholesaler_has_products_repository = WholesalerHasProductsRepository(db)
                return wholesaler_has_products_repository.get_wholesaler_product_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_wholesaler_product_by_wholesaler_id(wholesaler_id: str):
        """
        It deletes all the products of a wholesaler by the wholesaler's id
        """
        try:
            with SessionLocal() as db:
                wholesaler_has_products_repository = WholesalerHasProductsRepository(db)
                return wholesaler_has_products_repository.delete_wholesaler_product_by_wholesaler_id(wholesaler_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_wholesaler_product_by_product_id(product_id: str):
        """
        It deletes a wholesaler product by product id
        """
        try:
            with SessionLocal() as db:
                wholesaler_has_products_repository = WholesalerHasProductsRepository(db)
                return wholesaler_has_products_repository.delete_wholesaler_product_by_product_id(product_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_wholesaler_product(wholesaler_id: str, product_id: str, price: float, quantity_available: float):
        """
        Update a wholesaler's product
        """
        with SessionLocal() as db:
            try:
                wholesaler_product_repository = WholesalerHasProductsRepository(db)
                return wholesaler_product_repository.update_wholesaler_product(wholesaler_id, product_id, price,
                                                                               quantity_available)
            except WholesalerProductNotFoundException as e:
                raise e
            except Exception as e:
                raise e
