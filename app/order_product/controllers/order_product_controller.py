from sqlalchemy.exc import IntegrityError
from app.order_product.services import OrderProductServices
from fastapi import HTTPException, Response


class OrderProductController:
    @staticmethod
    def create_order_product(order_id: str, product_id: str):
        try:
            order_product = OrderProductServices.create_order_product(order_id, product_id)
            return order_product
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Order product with provided "
                                                        f"order_id/product_id: {order_id, product_id} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_order_products():
        order_products = OrderProductServices.get_all_order_products()
        return order_products

    @staticmethod
    def get_order_product_by_order_id(order_id: str):
        order_product = OrderProductServices.get_order_product_by_order_id(order_id)
        if order_product:
            return order_product
        else:
            raise HTTPException(status_code=400, detail=f"Order product with provided "
                                                        f"id: {order_id} does not exist.")

    @staticmethod
    def get_order_product_by_product_id(product_id: str):
        order_product = OrderProductServices.get_order_product_by_product_id(product_id)
        if order_product:
            return order_product
        else:
            raise HTTPException(status_code=400, detail=f"Order product with provided "
                                                        f"id: {product_id} does not exist.")

    @staticmethod
    def delete_order_product_by_order_id(order_id: str):
        try:
            OrderProductServices.delete_order_product_by_order_id(order_id)
            return Response(content=f"Order product with id: {order_id} successfully deleted.")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def delete_order_product_by_product_id(product_id: str):
        try:
            OrderProductServices.delete_order_product_by_product_id(product_id)
            return Response(content=f'Order product with id: "{product_id}" successfully deleted.')
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
