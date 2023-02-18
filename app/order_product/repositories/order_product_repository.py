from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.order_product.models.order_product import OrderProduct


class OrderProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_order_product(self, order_id: str, product_id: str, quantity: float):
        try:
            order_product = OrderProduct(order_id=order_id, product_id=product_id,
                                         quantity=quantity)
            self.db.add(order_product)
            self.db.commit()
            self.db.refresh(order_product)
            return order_product
        except IntegrityError as e:
            raise e

    def get_all_order_products(self):
        order_products = self.db.query(OrderProduct).all()
        return order_products

    def get_order_product_by_order_id(self, order_id: str):
        order_product = self.db.query(OrderProduct).filter(OrderProduct.order_id == order_id).all()
        return order_product

    def get_order_product_by_product_id(self, product_id: str):
        order_product = self.db.query(OrderProduct).filter(OrderProduct.product_id == product_id).all()
        return order_product

    def delete_order_product_by_order_id(self, order_id: str):
        try:
            order_product = self.db.query(OrderProduct).filter(OrderProduct.order_id == order_id).first()
            self.db.delete(order_product)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def delete_order_product_by_product_id(self, product_id: str):
        try:
            order_product = self.db.query(OrderProduct).filter(OrderProduct.product_id == product_id).first()
            self.db.delete(order_product)
            self.db.commit()
            return True
        except Exception as e:
            raise e
