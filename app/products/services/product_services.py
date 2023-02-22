from app.products.exceptions.product_exceptions import ProductNotFound
from app.products.repositories import ProductRepository
from app.db.database import SessionLocal


class ProductServices:

    @staticmethod
    def create_product(name: str, description: str, product_category_id: str):
        """
        It creates a product with the given name, description and product category id
        """
        with SessionLocal() as db:
            try:
                product_repository = ProductRepository(db)
                return product_repository.create_product(name, description, product_category_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_products():
        """
        It gets all the products from the database
        """
        with SessionLocal() as db:
            product_repository = ProductRepository(db)
            return product_repository.get_all_products()

    @staticmethod
    def get_product_by_id(product_id: str):
        """
        > This function gets a product by its id
        """
        with SessionLocal() as db:
            product_repository = ProductRepository(db)
            return product_repository.get_product_by_id(product_id)

    @staticmethod
    def get_product_by_name(name: str):
        """
        "Get a product by name."
        """
        with SessionLocal() as db:
            product_repository = ProductRepository(db)
            return product_repository.get_product_by_name(name)

    @staticmethod
    def delete_product_by_id(product_id: str):
        """
        It deletes a product from the database by its id
        """
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.delete_product_by_id(product_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_product(product_id: str, name: str, description: str):
        """
        It updates a product in the database
        """
        with SessionLocal() as db:
            try:
                product_repository = ProductRepository(db)
                return product_repository.update_product(product_id, name, description)
            except ProductNotFound as e:
                raise e
            except Exception as e:
                raise e
