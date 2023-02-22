from app.product_categories.exceptions import ProductCategoryNotFound
from app.product_categories.repositories import ProductCategoryRepository
from app.db.database import SessionLocal


class ProductCategoryServices:

    @staticmethod
    def create_product_category(name: str, description: str):
        with SessionLocal() as db:
            try:
                product_category_repository = ProductCategoryRepository(db)
                return product_category_repository.create_product_category(name,description)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_product_categories():
        with SessionLocal() as db:
            product_category_repository = ProductCategoryRepository(db)
            return product_category_repository.get_all_product_categories()

    @staticmethod
    def get_product_category_by_id(product_category_id: str):
        with SessionLocal() as db:
            product_category_repository = ProductCategoryRepository(db)
            return product_category_repository.get_product_category_by_id(product_category_id)

    @staticmethod
    def get_product_category_by_name(name: str):
        with SessionLocal() as db:
            product_category_repository = ProductCategoryRepository(db)
            return product_category_repository.get_product_category_by_name(name)

    @staticmethod
    def delete_product_category_by_id(product_category_id: str):
        try:
            with SessionLocal() as db:
                product_category_repository = ProductCategoryRepository(db)
                return product_category_repository.delete_product_category_by_id(product_category_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_product_category_name(product_category_id: str, name: str):
        with SessionLocal() as db:
            try:
                product_category_repository = ProductCategoryRepository(db)
                return product_category_repository.update_product_category_name(product_category_id, name)
            except Exception as e:
                raise e

    @staticmethod
    def update_product_category(product_category_id: str, name: str, description: str):
        with SessionLocal() as db:
            try:
                product_category_repository = ProductCategoryRepository(db)
                product_category = product_category_repository.update_product_category(product_category_id, name,
                                                                                       description)
                return product_category
            except ProductCategoryNotFound as e:
                raise e
