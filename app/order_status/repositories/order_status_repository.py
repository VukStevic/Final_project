import datetime
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.order_status.models import OrderStatus


class OrderStatusRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_order_status(self, status_code: str, description: str, date_and_time: str, order_id: str):
        try:
            order_status = OrderStatus(status_code, description, date_and_time, order_id)
            self.db.add(order_status)
            self.db.commit()
            self.db.refresh(order_status)
            return order_status
        except IntegrityError as e:
            raise e

    def get_all_order_statuses(self):
        order_statuses = self.db.query(OrderStatus).all()
        return order_statuses

    def get_order_status_by_status_code(self, status_code: str):
        order_status = self.db.query(OrderStatus).filter(OrderStatus.status_code == status_code).first()
        return order_status

    def get_order_status_by_date_and_time(self, date_and_time: str):
        order_status = self.db.query(OrderStatus).filter(OrderStatus.date_and_time == date_and_time).first()
        return order_status

    def delete_order_status_by_status_code(self, status_code: str):
        try:
            order_status = self.db.query(OrderStatus).filter(OrderStatus.status_code == status_code).first()
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

    def update_order_status(self, status_code: str, new_status_code: str):
        try:
            order_status = self.db.query(OrderStatus).filter(OrderStatus.status_code == status_code).first()
            order_status.status_code = new_status_code
            order_status.date_and_time = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
            self.db.add(order_status)
            self.db.commit()
            self.db.refresh(order_status)
            return order_status
        except Exception as e:
            raise e

    def update_order_status_description(self, status_code: str, description: str):
        try:
            order_status = self.db.query(OrderStatus).filter(OrderStatus.status_code == status_code).first()
            order_status.description = description
            self.db.add(order_status)
            self.db.commit()
            self.db.refresh(order_status)
            return order_status
        except Exception as e:
            raise e
