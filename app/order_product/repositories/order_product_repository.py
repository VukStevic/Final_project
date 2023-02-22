from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.order_product.models.order_product import OrderProduct
from app.orders.services import OrderServices
from app.wholesaler_has_products.exceptions import WholesalerProductNotFoundException
from app.wholesaler_has_products.services import WholesalerHasProductsServices


class OrderProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_order_product(self, order_id: str, wholesaler_product_id: str, quantity: float):
        try:
            wholesaler_product = WholesalerHasProductsServices.get_wholesaler_product_by_id(wholesaler_product_id)
            price = wholesaler_product.price
            order_product = OrderProduct(order_id=order_id, wholesaler_product_id=wholesaler_product_id,
                                         quantity=quantity, price=price)
            self.db.add(order_product)
            self.db.commit()
            self.db.refresh(order_product)
            return order_product
        except IntegrityError as e:
            raise e
        except Exception:
            raise WholesalerProductNotFoundException(code=400, message="Wholesaler product with a given id not found.")

    def get_all_order_products(self):
        order_products = self.db.query(OrderProduct).all()
        return order_products

    def get_average_product_price(self, wholesaler_product_id):
        try:
            sum = 0
            count = 0
            order_products = self.get_order_product_by_wholesaler_product_id(wholesaler_product_id)
            for order_product in order_products:
                sum += order_product.price * order_product.quantity
                count += order_product.quantity
            average_price = round(sum / count, 2)
            return average_price
        except ZeroDivisionError as e:
            raise e

    def get_order_product_by_id(self, id: str):
        order_product = self.db.query(OrderProduct).filter(OrderProduct.id == id).first()
        return order_product

    def get_order_product_by_order_id(self, order_id: str):
        order_product = self.db.query(OrderProduct).filter(OrderProduct.order_id == order_id).all()
        return order_product

    def get_order_product_by_wholesaler_product_id(self, wholesaler_product_id: str):
        order_product = self.db.query(OrderProduct).\
            filter(OrderProduct.wholesaler_product_id == wholesaler_product_id).all()
        return order_product

    def get_average_product_count_per_order(self):
        try:
            order_products = self.db.query(OrderProduct).all()
            product_count = 0
            for order_product in order_products:
                product_count += order_product.quantity
            order_count = len(OrderServices.get_all_orders())
            count_per_order = product_count / order_count
            return count_per_order
        except ZeroDivisionError as e:
            raise e
        except Exception as e:
            raise e

    def get_total_wholesaler_revenue(self, wholesaler_id: str):
        try:
            revenue = 0
            orders = OrderServices.get_order_by_wholesaler_id(wholesaler_id)
            order_products = self.db.query(OrderProduct).all()
            for order in orders:
                for order_product in order_products:
                    if order.id == order_product.order_id:
                        revenue += order_product.quantity * order_product.price
            return revenue
        except ZeroDivisionError as e:
            raise e
        except Exception as e:
            raise e

    def update_order_product(self, id: str, quantity: float):
        try:
            order_product = self.db.query(OrderProduct).filter(OrderProduct.id == id).first()
            if quantity is not None:
                order_product.quantity = quantity
            self.db.add(order_product)
            self.db.commit()
            self.db.refresh(order_product)
            return order_product
        except Exception as e:
            raise e

    def delete_order_product_by_order_id(self, order_id: str):
        try:
            order_product = self.db.query(OrderProduct).filter(OrderProduct.order_id == order_id).first()
            self.db.delete(order_product)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def delete_order_product_by_wholesaler_product_id(self, wholesaler_product_id: str):
        try:
            order_product = self.db.query(OrderProduct).\
                filter(OrderProduct.wholesaler_product_id == wholesaler_product_id).first()
            self.db.delete(order_product)
            self.db.commit()
            return True
        except Exception as e:
            raise e
