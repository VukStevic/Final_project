from datetime import datetime
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.orders.exceptions import OrderNotFoundException
from app.orders.models import Order


class OrderRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_order(self, type: str, order_date: str, wholesaler_id: str, retailer_id: str):
        """
        It creates an order object, adds it to the database, commits the changes, and returns the order object
        """
        try:
            order = Order(type=type, order_date=order_date, wholesaler_id=wholesaler_id, retailer_id=retailer_id)
            self.db.add(order)
            self.db.commit()
            self.db.refresh(order)
            return order
        except IntegrityError as e:
            raise e

    def get_all_orders(self):
        """
        It returns all the orders in the database
        """
        orders = self.db.query(Order).all()
        return orders

    def get_order_by_id(self, order_id: str):
        """
        It gets an order by id
        """
        order = self.db.query(Order).filter(Order.id == order_id).first()
        return order

    def get_order_by_wholesaler_id(self, wholesaler_id: str):
        """
        This function returns all the orders for a wholesaler with a given wholesaler_id
        """
        order = self.db.query(Order).filter(Order.wholesaler_id == wholesaler_id).all()
        return order

    def get_order_by_retailer_id(self, retailer_id: str):
        """
        This function returns all the orders for a given retailer
        """
        order = self.db.query(Order).filter(Order.retailer_id == retailer_id).all()
        return order

    def get_order_by_wholesaler_and_date_range(self, wholesaler_id: str, starting_date: str, ending_date: str):
        """
        It returns all the orders for a wholesaler between two dates
        """
        start = datetime.strptime(starting_date, "%d-%m-%Y")
        end = datetime.strptime(ending_date, "%d-%m-%Y")
        order = self.db.query(Order).filter(Order.wholesaler_id == wholesaler_id,
                                            Order.order_date >= start, Order.order_date <= end).all()
        return order

    def get_order_by_retailer_and_date_range(self, retailer_id: str, starting_date: str, ending_date: str):
        """
        It returns all the orders for a given retailer between two dates
        """
        start = datetime.strptime(starting_date, "%d-%m-%Y")
        end = datetime.strptime(ending_date, "%d-%m-%Y")
        order = self.db.query(Order).filter(Order.retailer_id == retailer_id,
                                            Order.order_date >= start, Order.order_date <= end).all()
        return order

    def delete_order_by_id(self, order_id: str):
        """
        It deletes an order from the database by its id
        """
        try:
            order = self.db.query(Order).filter(Order.id == order_id).first()
            self.db.delete(order)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_order(self, order_id: str, type: str, order_date: str):
        """
        It updates an order in the database

        """
        order = self.db.query(Order).filter(Order.id == order_id).first()
        if not order:
            raise OrderNotFoundException(code=400, message=f"Order with provided id {order_id} not found.")
        if type is not None:
            order.type = type
        if order_date is not None:
            order.order_date = order_date
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order

