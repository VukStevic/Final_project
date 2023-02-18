from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.orders.models import Order


class OrderRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_order(self, type: str, order_date: str, wholesaler_id: str, retailer_id: str):
        try:
            order = Order(type=type, order_date=order_date, wholesaler_id=wholesaler_id, retailer_id=retailer_id)
            self.db.add(order)
            self.db.commit()
            self.db.refresh(order)
            return order
        except IntegrityError as e:
            raise e

    def get_all_orders(self):
        orders = self.db.query(Order).all()
        return orders

    def get_order_by_id(self, order_id: str):
        order = self.db.query(Order).filter(Order.id == order_id).first()
        return order

    def delete_order_by_id(self, order_id: str):
        try:
            order = self.db.query(Order).filter(Order.id == order_id).first()
            self.db.delete(order)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_order_type(self, order_id: str, type: str):
        try:
            order = self.db.query(Order).filter(Order.id == order_id).first()
            order.type = type
            self.db.add(order)
            self.db.commit()
            self.db.refresh(order)
            return order
        except Exception as e:
            raise e

    def update_order_date(self, order_id: str, order_date: str):
        try:
            order = self.db.query(Order).filter(Order.id == order_id).first()
            order.order_date = order_date
            self.db.add(order)
            self.db.commit()
            self.db.refresh(order)
            return order
        except Exception as e:
            raise e
