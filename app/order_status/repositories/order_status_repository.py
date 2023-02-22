import datetime
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.order_status.exceptions import OrderStatusNotFound
from app.order_status.models import OrderStatus


class OrderStatusRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_order_status(self, status_code: str, description: str, order_id: str):
        """
        It creates an order status object, adds it to the database, commits the changes,
        and returns the order status object
        """
        try:
            order_status = OrderStatus(status_code, description, order_id)
            self.db.add(order_status)
            self.db.commit()
            self.db.refresh(order_status)
            return order_status
        except IntegrityError as e:
            raise e

    def get_all_order_statuses(self):
        """
        It returns all the order statuses from the database
        """
        order_statuses = self.db.query(OrderStatus).all()
        return order_statuses

    def get_order_status_by_id(self, id: str):
        """
        It returns the order status with the given id
        """
        order_status = self.db.query(OrderStatus).filter(OrderStatus.id == id).first()
        return order_status

    def get_order_status_by_order_id(self, order_id: str):
        """
        It returns the order status of a given order id
        """
        order_status = self.db.query(OrderStatus).filter(OrderStatus.order_id == order_id).first()
        return order_status

    def get_order_status_by_date_and_time(self, date_and_time: str):
        """
        It returns the order status of an order given the date and time of the order
        """
        order_status = self.db.query(OrderStatus).filter(OrderStatus.date_and_time == date_and_time).first()
        return order_status

    def delete_order_status_by_id(self, id: str):
        """
        It deletes an order status from the database
        """
        try:
            order_status = self.db.query(OrderStatus).filter(OrderStatus.id == id).first()
            self.db.delete(order_status)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def delete_order_status_by_date_and_time(self, date_and_time: str):
        """
        It deletes an order status from the database by date and time
        """
        try:
            order_status = self.db.query(OrderStatus).filter(OrderStatus.date_and_time == date_and_time).first()
            self.db.delete(order_status)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_order_status(self, id: str, status_code: str, description: str):
        """
        It updates the order status with the provided id, if the order status is not found, it raises an exception
        """
        order_status = self.db.query(OrderStatus).filter(OrderStatus.id == id).first()
        if not order_status:
            raise OrderStatusNotFound(code=400, message=f"Order status with provided id: {id} not found.")
        order_status.date_and_time = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
        if status_code is not None:
            order_status.status_code = status_code
        if description is not None:
            order_status.description = description
        self.db.add(order_status)
        self.db.commit()
        self.db.refresh(order_status)
        return order_status
