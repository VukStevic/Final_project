from sqlalchemy.exc import IntegrityError
from app.orders.exceptions import OrderNotFoundException
from app.orders.services import OrderServices
from fastapi import HTTPException, Response


class OrderController:
    @staticmethod
    def create_order(type: str, order_date: str, wholesaler_id: str, retailer_id: str):
        """
        It creates an order
        """
        try:
            order = OrderServices.create_order(type, order_date, wholesaler_id, retailer_id)
            return order
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_orders():
        """
        It returns all orders
        """
        orders = OrderServices.get_all_orders()
        return orders

    @staticmethod
    def get_order_by_id(order_id: str):
        """
        It gets an order by id.
        """
        order = OrderServices.get_order_by_id(order_id)
        if order:
            return order
        else:
            raise HTTPException(status_code=400, detail=f"Order with provided "
                                                        f"id: {order_id} does not exist.")

    @staticmethod
    def get_order_by_wholesaler_id(wholesaler_id: str):
        """
        It gets an order by wholesaler id
        """
        order = OrderServices.get_order_by_wholesaler_id(wholesaler_id)
        if order:
            return order
        else:
            raise HTTPException(status_code=400, detail=f"Order with provided "
                                                        f"id: {wholesaler_id} does not exist.")

    @staticmethod
    def get_order_by_retailer_id(retailer_id: str):
        """
        It gets the order by retailer id.
        """
        order = OrderServices.get_order_by_retailer_id(retailer_id)
        if order:
            return order
        else:
            raise HTTPException(status_code=400, detail=f"Order with provided "
                                                        f"id: {retailer_id} does not exist.")

    @staticmethod
    def get_order_by_wholesaler_and_date_range(wholesaler_id: str, starting_date: str, ending_date: str):
        """
        This function returns a list of orders for a wholesaler within a date range
        """
        order = OrderServices.get_order_by_wholesaler_and_date_range(wholesaler_id, starting_date, ending_date)
        if order:
            return order
        else:
            raise HTTPException(status_code=400, detail=f"Order with provided parameters does not exist.")

    @staticmethod
    def get_order_by_retailer_and_date_range(retailer_id: str, starting_date: str, ending_date: str):
        """
        This function takes in a retailer id, starting date, and ending date and returns the order with the
        given parameters
        """
        order = OrderServices.get_order_by_retailer_and_date_range(retailer_id, starting_date, ending_date)
        if order:
            return order
        else:
            raise HTTPException(status_code=400, detail=f"Order with provided parameters does not exist.")

    @staticmethod
    def delete_order_by_id(order_id: str):
        """
        It deletes an order by id.
        """
        try:
            OrderServices.delete_order_by_id(order_id)
            return Response(content=f'Order with id: "{order_id}" successfully deleted.')
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_order(order_id: str, type: str, order_date: str):
        """
        It updates an order.
        """
        try:
            return OrderServices.update_order(order_id, type, order_date)
        except OrderNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
