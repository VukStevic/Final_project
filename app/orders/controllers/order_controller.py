from sqlalchemy.exc import IntegrityError
from app.orders.services import OrderServices
from fastapi import HTTPException, Response


class OrderController:
    @staticmethod
    def create_order(type: str, order_date: str, wholesaler_id: str, retailer_id: str):
        try:
            order = OrderServices.create_order(type, order_date, wholesaler_id, retailer_id)
            return order
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_orders():
        orders = OrderServices.get_all_orders()
        return orders

    @staticmethod
    def get_order_by_id(order_id: str):
        order = OrderServices.get_order_by_id(order_id)
        if order:
            return order
        else:
            raise HTTPException(status_code=400, detail=f"Order with provided "
                                                        f"id: {order_id} does not exist.")

    @staticmethod
    def delete_order_by_id(order_id: str):
        try:
            OrderServices.delete_order_by_id(order_id)
            return Response(content=f'Order with id: "{order_id}" successfully deleted.')
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_order_type(order_id: str, type: str):
        try:
            return OrderServices.update_order_type(order_id, type)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_order_date(order_id: str, order_date: str):
        try:
            return OrderServices.update_order_date(order_id, order_date)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
