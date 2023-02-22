import datetime
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.order_status.models import OrderStatus


class OrderStatusRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_order_status(self, status_code: str, description: str, order_id: str):
        try:
            order_status = OrderStatus(status_code, description, order_id)
            self.db.add(order_status)
            self.db.commit()
            self.db.refresh(order_status)
            return order_status
        except IntegrityError as e:
            raise e

    def get_all_order_statuses(self):
        order_statuses = self.db.query(OrderStatus).all()
        return order_statuses

    def get_order_status_by_id(self, id: str):
        order_status = self.db.query(OrderStatus).filter(OrderStatus.id == id).first()
        return order_status

    def get_order_status_by_order_id(self, order_id: str):
        order_status = self.db.query(OrderStatus).filter(OrderStatus.order_id == order_id).first()
        return order_status

    def get_order_status_by_date_and_time(self, date_and_time: str):
        order_status = self.db.query(OrderStatus).filter(OrderStatus.date_and_time == date_and_time).first()
        return order_status

    def delete_order_status_by_id(self, id: str):
        try:
            order_status = self.db.query(OrderStatus).filter(OrderStatus.id == id).first()
            self.db.delete(order_status)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def delete_order_status_by_date_and_time(self, date_and_time: str):
        try:
            order_status = self.db.query(OrderStatus).filter(OrderStatus.date_and_time == date_and_time).first()
            self.db.delete(order_status)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_order_status_description(self, id: str, description: str):
        try:
            order_status = self.db.query(OrderStatus).filter(OrderStatus.id == id).first()
            order_status.description = description
            self.db.add(order_status)
            self.db.commit()
            self.db.refresh(order_status)
            return order_status
        except Exception as e:
            raise e

    def update_order_status(self, id: str, status_code: str, description: str):
        try:
            order_status = self.db.query(OrderStatus).filter(OrderStatus.id == id).first()
            order_status.date_and_time = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
            if status_code is not None:
                order_status.status_code = status_code
            if description is not None:
                order_status.description = description
            self.db.add(order_status)
            self.db.commit()
            self.db.refresh(order_status)
            return order_status
        except Exception as e:
            raise e
