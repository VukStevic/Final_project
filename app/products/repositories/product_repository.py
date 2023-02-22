from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.products.exceptions.product_exceptions import ProductNotFound
from app.products.models import Product


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_product(self, name: str, description: str, product_category_id: str):
        """
        It creates a new product and adds it to the database
        """
        try:
            product = Product(name, description, product_category_id)
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except IntegrityError as e:
            raise e

    def get_all_products(self):
        """
        It returns all the products in the database
        """
        products = self.db.query(Product).all()
        return products

    def get_product_by_id(self, product_id: str):
        """
        It returns a product from the database, given a product id
        """
        product = self.db.query(Product).filter(Product.id == product_id).first()
        return product

    def get_product_by_name(self, name: str):
        """
        It returns the first product in the database that matches the name passed in
        """
        product = self.db.query(Product).filter(Product.name == name).first()
        return product

    def delete_product_by_id(self, product_id: str):
        """
        It deletes a product from the database by its id
        """
        try:
            product = self.db.query(Product).filter(Product.id == product_id).first()
            self.db.delete(product)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_product(self, product_id: str, name: str, description: str):
        """
        It updates a product with the given product id, name and description
        """
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise ProductNotFound(code=400, message=f"Product with provided product id {product_id} not found.")
        if name is not None:
            product.name = name
        if description is not None:
            product.description = description
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

