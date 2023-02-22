from sqlalchemy.exc import IntegrityError
from app.order_status.services import OrderStatusServices
from fastapi import HTTPException, Response


class OrderStatusController:
    @staticmethod
    def create_order_status(status_code: str, description: str, order_id: str):
        try:
            order_status = OrderStatusServices.create_order_status(status_code, description, order_id)
            return order_status
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_order_statuses():
        order_statuses = OrderStatusServices.get_all_order_statuses()
        return order_statuses

    @staticmethod
    def get_order_status_by_id(id: str):
        order_status = OrderStatusServices.get_order_status_by_id(id)
        if order_status:
            return order_status
        else:
            raise HTTPException(status_code=400, detail=f"Order status with provided "
                                                        f"id: {id} does not exist.")

    @staticmethod
    def get_order_status_by_order_id(order_id: str):
        order_status = OrderStatusServices.get_order_status_by_order_id(order_id)
        if order_status:
            return order_status
        else:
            raise HTTPException(status_code=400, detail=f"Order status with provided "
                                                        f"id: {order_id} does not exist.")

    @staticmethod
    def get_order_status_by_date_and_time(date_and_time: str):
        order_status = OrderStatusServices.get_order_status_by_date_and_time(date_and_time)
        if order_status:
            return order_status
        else:
            raise HTTPException(status_code=400, detail=f"Order status with provided "
                                                        f"date and time: {date_and_time} does not exist.")

    @staticmethod
    def delete_order_status_by_id(id: str):
        try:
            OrderStatusServices.delete_order_status_by_id(id)
            return Response(content=f'Order status with id: "{id}" successfully deleted.')
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def delete_order_status_by_date_and_time(date_and_time: str):
        try:
            OrderStatusServices.delete_order_status_by_date_and_time(date_and_time)
            return Response(content=f'Order status with date and time: "{date_and_time}" successfully deleted.')
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_order_status(id: str, status_code: str, description: str):
        try:
            return OrderStatusServices.update_order_status(id, status_code, description)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_order_status_description(id: str, description: str):
        try:
            return OrderStatusServices.update_order_status_description(id, description)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
