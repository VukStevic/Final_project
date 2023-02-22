from sqlalchemy.exc import IntegrityError
from app.order_status.exceptions import OrderStatusNotFound
from app.order_status.services import OrderStatusServices
from fastapi import HTTPException, Response


class OrderStatusController:
    @staticmethod
    def create_order_status(status_code: str, description: str, order_id: str):
        """
        It creates an order status.
        """
        try:
            order_status = OrderStatusServices.create_order_status(status_code, description, order_id)
            return order_status
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_order_statuses():
        """
        This function returns all order statuses
        """
        order_statuses = OrderStatusServices.get_all_order_statuses()
        return order_statuses

    @staticmethod
    def get_order_status_by_id(id: str):
        """
        It returns the order status by id.

        :param id: str - the id of the order status we want to get
        :type id: str
        :return: The order status with the provided id.
        """
        order_status = OrderStatusServices.get_order_status_by_id(id)
        if order_status:
            return order_status
        else:
            raise HTTPException(status_code=400, detail=f"Order status with provided "
                                                        f"id: {id} does not exist.")

    @staticmethod
    def get_order_status_by_order_id(order_id: str):
        """
        It returns the order status of the order with the given order id.

        :param order_id: str - the order id of the order status you want to get
        :type order_id: str
        :return: Order status object
        """
        order_status = OrderStatusServices.get_order_status_by_order_id(order_id)
        if order_status:
            return order_status
        else:
            raise HTTPException(status_code=400, detail=f"Order status with provided "
                                                        f"id: {order_id} does not exist.")

    @staticmethod
    def get_order_status_by_date_and_time(date_and_time: str):
        """
        It gets an order status by date and time
        """
        order_status = OrderStatusServices.get_order_status_by_date_and_time(date_and_time)
        if order_status:
            return order_status
        else:
            raise HTTPException(status_code=400, detail=f"Order status with provided "
                                                        f"date and time: {date_and_time} does not exist.")

    @staticmethod
    def delete_order_status_by_id(id: str):
        """
        It deletes an order status by id.
        """
        try:
            OrderStatusServices.delete_order_status_by_id(id)
            return Response(content=f'Order status with id: "{id}" successfully deleted.')
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def delete_order_status_by_date_and_time(date_and_time: str):
        """
        It deletes an order status by date and time.
        """
        try:
            OrderStatusServices.delete_order_status_by_date_and_time(date_and_time)
            return Response(content=f'Order status with date and time: "{date_and_time}" successfully deleted.')
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_order_status(id: str, status_code: str, description: str):
        """
        > Update the status of an order
        """
        try:
            return OrderStatusServices.update_order_status(id, status_code, description)
        except OrderStatusNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
