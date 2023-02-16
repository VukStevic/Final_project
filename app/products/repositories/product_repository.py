from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.products.models import Product


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_product(self, name: str, description: str, price: float, quantity_available: float,
                       product_category_id: str):
        try:
            product = Product(name, description, price, quantity_available, product_category_id)
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except IntegrityError as e:
            raise e

    def get_all_products(self):
        products = self.db.query(Product).all()
        return products

    def get_product_by_id(self, product_id: str):
        product = self.db.query(Product).filter(Product.id == product_id).first()
        return product

    def get_product_by_name(self, name: str):
        product = self.db.query(Product).filter(Product.name == name).first()
        return product

    def delete_product_by_id(self, product_id: str):
        try:
            product = self.db.query(Product).filter(Product.id == product_id).first()
            self.db.delete(product)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_product_description(self, product_id: str, description: str):
        try:
            product = self.db.query(Product).filter(Product.id == product_id).first()
            product.description = description
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except Exception as e:
            raise e

    def update_product_price(self, product_id: str, price: float):
        try:
            product = self.db.query(Product).filter(Product.id == product_id).first()
            product.price = price
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except Exception as e:
            raise e

    def update_product_quantity_available(self, product_id: str, quantity_available: float):
        try:
            product = self.db.query(Product).filter(Product.id == product_id).first()
            product.quantity_available = quantity_available
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except Exception as e:
            raise e
