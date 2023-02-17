from sqlalchemy.exc import IntegrityError
from app.order_status.services import OrderStatusServices
from fastapi import HTTPException, Response


class OrderStatusController:
    @staticmethod
    def create_order_status(status_code: str, description: str, date_and_time: str, order_id: str):
        try:
            order_status = OrderStatusServices.create_order_status(status_code, description, date_and_time,
                                                                   order_id)
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
    def get_order_status_by_status_code(status_code: str):
        order_status = OrderStatusServices.get_order_status_by_status_code(status_code)
        if order_status:
            return order_status
        else:
            raise HTTPException(status_code=400, detail=f"Order status with provided "
                                                        f"status code: {status_code} does not exist.")

    @staticmethod
    def get_order_status_by_date_and_time(date_and_time: str):
        order_status = OrderStatusServices.get_order_status_by_date_and_time(date_and_time)
        if order_status:
            return order_status
        else:
            raise HTTPException(status_code=400, detail=f"Order status with provided "
                                                        f"date and time: {date_and_time} does not exist.")

    @staticmethod
    def delete_order_status_by_status_code(status_code: str):
        try:
            OrderStatusServices.delete_order_status_by_status_code(status_code)
            return Response(content=f'Order status with status code: "{status_code}" successfully deleted.')
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
    def update_order_status(status_code: str, new_status_code: str):
        try:
            return OrderStatusServices.update_order_status(status_code, new_status_code)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_order_status_description(status_code: str, description: str):
        try:
            return OrderStatusServices.update_order_status_description(status_code, description)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
