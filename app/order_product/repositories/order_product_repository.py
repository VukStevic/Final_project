from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.order_product.exceptions import OrderProductNotFoundException
from app.order_product.models.order_product import OrderProduct
from app.orders.services import OrderServices
from app.wholesaler_has_products.exceptions import WholesalerProductNotFoundException
from app.wholesaler_has_products.services import WholesalerHasProductsServices


class OrderProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_order_product(self, order_id: str, wholesaler_product_id: str, quantity: float):
        """
        It creates an order product by taking in an order id, a wholesaler product id, and a quantity
        """
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
        """
        It returns all the order products in the database
        """
        order_products = self.db.query(OrderProduct).all()
        return order_products

    def get_average_product_price(self, wholesaler_product_id):
        """
        It gets the average price of a product by summing up the prices of all the orders that contain the product and
        dividing by the total quantity of the product in all the orders
        """
        try:
            sum = 0
            count = 0
            order_products = self.get_order_product_by_wholesaler_product_id(wholesaler_product_id)
            for order_product in order_products:
                sum += order_product.price * order_product.quantity
                count += order_product.quantity
            average_price = round(sum / count, 2)
            return average_price
        except OrderProductNotFoundException as e:
            raise e
        except ZeroDivisionError as e:
            raise e

    def get_order_product_by_id(self, id: str):
        """
        It returns an order product by id
        """
        order_product = self.db.query(OrderProduct).filter(OrderProduct.id == id).first()
        if not order_product:
            raise OrderProductNotFoundException(code=400, message=f"Order product with provided id: {id} not found.")
        return order_product

    def get_order_product_by_order_id(self, order_id: str):
        """
        It returns all the order products that have the same order id as the one provided
        """
        order_product = self.db.query(OrderProduct).filter(OrderProduct.order_id == order_id).all()
        if not order_product:
            raise OrderProductNotFoundException(code=400, message=f"Order product with provided order id: {order_id} "
                                                                  f"not found.")
        return order_product

    def get_order_product_by_wholesaler_product_id(self, wholesaler_product_id: str):
        """
        It returns a list of order products that have the same wholesaler product id as the one provided
        """
        order_product = self.db.query(OrderProduct).\
            filter(OrderProduct.wholesaler_product_id == wholesaler_product_id).all()
        if not order_product:
            raise OrderProductNotFoundException(code=400, message=f"Order product with provided wholesaler product id: "
                                                                  f"{wholesaler_product_id} not found.")
        return order_product

    def get_average_product_count_per_order(self):
        """
        It gets the average product count per order by getting the total product count and dividing it by the total
        order count

        """
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
        """
        It gets the total revenue of a wholesaler by getting all the orders of the wholesaler, then getting all the order
        products, then adding the quantity of the order product multiplied by the price of the order product to the revenue
        """
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
        """
        It updates an order product with the given id, and returns the updated order product
        """
        order_product = self.db.query(OrderProduct).filter(OrderProduct.id == id).first()
        if not order_product:
            raise OrderProductNotFoundException(code=400, message=f"Order product with provided id {id} not found.")
        if quantity is not None:
            order_product.quantity = quantity
        self.db.add(order_product)
        self.db.commit()
        self.db.refresh(order_product)
        return order_product

    def delete_order_product_by_order_id(self, order_id: str):
        """
        It deletes an order product by order id
        """
        try:
            order_product = self.db.query(OrderProduct).filter(OrderProduct.order_id == order_id).first()
            self.db.delete(order_product)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def delete_order_product_by_wholesaler_product_id(self, wholesaler_product_id: str):
        """
        It deletes an order product from the database by its wholesaler product id
        """
        try:
            order_product = self.db.query(OrderProduct).\
                filter(OrderProduct.wholesaler_product_id == wholesaler_product_id).first()
            self.db.delete(order_product)
            self.db.commit()
            return True
        except Exception as e:
            raise e
