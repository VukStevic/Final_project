from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.product_categories.exceptions import ProductCategoryNotFound
from app.product_categories.models import ProductCategory


class ProductCategoryRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_product_category(self, name: str, description: str):
        try:
            product_category = ProductCategory(name, description)
            self.db.add(product_category)
            self.db.commit()
            self.db.refresh(product_category)
            return product_category
        except IntegrityError as e:
            raise e

    def get_all_product_categories(self):
        product_categories = self.db.query(ProductCategory).all()
        return product_categories

    def get_product_category_by_id(self, product_category_id: str):
        product_category = self.db.query(ProductCategory).filter(ProductCategory.id == product_category_id).first()
        return product_category

    def get_product_category_by_name(self, name: str):
        product_category = self.db.query(ProductCategory).filter(ProductCategory.name == name).first()
        return product_category

    def delete_product_category_by_id(self, product_category_id: str):
        try:
            product_category = self.db.query(ProductCategory).filter(ProductCategory.id == product_category_id).first()
            self.db.delete(product_category)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_product_category_name(self, product_category_id: str, name: str):
        try:
            product_category = self.db.query(ProductCategory).filter(ProductCategory.id == product_category_id).first()
            product_category.name = name
            self.db.add(product_category)
            self.db.commit()
            self.db.refresh(product_category)
            return product_category
        except Exception as e:
            raise e

    def update_product_category(self, product_category_id: str, name: str, description: str):
        product_category = self.db.query(ProductCategory).filter(ProductCategory.id == product_category_id).first()
        if not product_category:
            raise ProductCategoryNotFound(code=400, message=f"Product category with provided product category id: "
                                                            f"{product_category_id} not found.")
        if name is not None:
            product_category.name = name
        if description is not None:
            product_category.description = description
        self.db.add(product_category)
        self.db.commit()
        self.db.refresh(product_category)
        return product_category
