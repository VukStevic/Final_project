from sqlalchemy.exc import IntegrityError

from app.order_product.exceptions import OrderProductNotFoundException
from app.order_product.services import OrderProductServices
from fastapi import HTTPException, Response

from app.wholesaler_has_products.exceptions import WholesalerProductNotFoundException


class OrderProductController:
    @staticmethod
    def create_order_product(order_id: str, wholesaler_product_id: str, quantity: float):
        """
        It creates an order product
        """
        try:
            order_product = OrderProductServices.create_order_product(order_id, wholesaler_product_id, quantity)
            return order_product
        except WholesalerProductNotFoundException:
            raise HTTPException(status_code=400, detail=f"Wholesaler product with a given id not found.")
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Order product with provided "
                                                        f"order_id/wholesaler_product_id: "
                                                        f"{order_id, wholesaler_product_id} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_order_products():
        """
        It returns all the order products in the database
        """
        order_products = OrderProductServices.get_all_order_products()
        return order_products

    @staticmethod
    def get_average_product_price(wholesaler_product_id):
        """
        It returns the average price of a product, given its wholesaler_product_id
        """
        try:
            return OrderProductServices.get_average_product_price(wholesaler_product_id)
        except OrderProductNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ZeroDivisionError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def get_order_product_by_order_id(order_id: str):
        """
        It gets the order product by order id.
        """
        try:
            order_product = OrderProductServices.get_order_product_by_order_id(order_id)
            return order_product
        except OrderProductNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)

    @staticmethod
    def get_order_product_by_wholesaler_product_id(wholesaler_product_id: str):
        """
        It gets the order product by wholesaler product id.
        """
        try:
            order_product = OrderProductServices.get_order_product_by_wholesaler_product_id(wholesaler_product_id)
            return order_product
        except OrderProductNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)

    @staticmethod
    def get_order_product_by_id(id: str):
        """
        It gets the order product by id.
        """
        try:
            order_product = OrderProductServices.get_order_product_by_id(id)
            return order_product
        except OrderProductNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)

    @staticmethod
    def get_average_product_count_per_order():
        """
        It returns the average number of products per order
        """
        try:
            return OrderProductServices.get_average_product_count_per_order()
        except ZeroDivisionError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def get_total_wholesaler_revenue(wholesaler_id: str):
        """
        It returns the total revenue of a wholesaler
        """
        try:
            return OrderProductServices.get_total_wholesaler_revenue(wholesaler_id)
        except ZeroDivisionError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_order_product(id: str, quantity: float):
        """
        It updates the order product.
        """
        try:
            order_product = OrderProductServices.update_order_product(id, quantity)
            return order_product
        except OrderProductNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)

    @staticmethod
    def delete_order_product_by_order_id(order_id: str):
        """
        It deletes an order product by order id.
        """
        try:
            OrderProductServices.delete_order_product_by_order_id(order_id)
            return Response(content=f"Order product with id: {order_id} successfully deleted.")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def delete_order_product_by_wholesaler_product_id(wholesaler_product_id: str):
        """
        It deletes an order product by its wholesaler product id
        """
        try:
            OrderProductServices.delete_order_product_by_wholesaler_product_id(wholesaler_product_id)
            return Response(content=f'Order product with id: "{wholesaler_product_id}" successfully deleted.')
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
