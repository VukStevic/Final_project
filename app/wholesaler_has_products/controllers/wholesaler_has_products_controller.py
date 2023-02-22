from sqlalchemy.exc import IntegrityError

from app.wholesaler_has_products.exceptions import WholesalerProductNotFoundException
from app.wholesaler_has_products.services import WholesalerHasProductsServices
from fastapi import HTTPException, Response


class WholesalerHasProductsController:
    @staticmethod
    def create_wholesaler_has_products(wholesaler_id: str, product_id: str, price: float, quantity_available: float):
        """
        It creates a wholesaler_has_products object and returns it
        """
        try:
            wholesaler_has_products = WholesalerHasProductsServices.create_wholesaler_product(wholesaler_id, product_id,
                                                                                              price, quantity_available)
            return wholesaler_has_products
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Wholesaler product with provided "
                                                        f"wholesaler_id/product_id: {wholesaler_id, product_id} "
                                                        f"already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_wholesaler_products():
        """
        It gets all the wholesaler products
        """
        try:
            wholesaler_has_products = WholesalerHasProductsServices.get_all_wholesaler_products()
            return wholesaler_has_products
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_wholesaler_product_by_wholesaler_id(wholesaler_id: str):
        """
        It gets a wholesaler product by wholesaler id
        """
        wholesaler_has_products = WholesalerHasProductsServices.get_wholesaler_product_by_wholesaler_id(wholesaler_id)
        if wholesaler_has_products:
            return wholesaler_has_products
        else:
            raise HTTPException(status_code=400, detail=f"Wholesaler product with provided "
                                                        f"wholesaler_id: {wholesaler_id} does not exist.")

    @staticmethod
    def get_wholesaler_product_by_id(id: str):
        """
        It gets a wholesaler product by id
        """
        wholesaler_has_products = WholesalerHasProductsServices.get_wholesaler_product_by_id(id)
        if wholesaler_has_products:
            return wholesaler_has_products
        else:
            raise HTTPException(status_code=400, detail=f"Wholesaler product with provided "
                                                        f"id: {id} does not exist.")

    @staticmethod
    def get_wholesaler_product_by_product_id(product_id: str):
        """
        This function gets a wholesaler product by product id
        """
        wholesaler_has_products = WholesalerHasProductsServices.get_wholesaler_product_by_product_id(product_id)
        if wholesaler_has_products:
            return wholesaler_has_products
        else:
            raise HTTPException(status_code=400, detail=f"Wholesaler product with provided "
                                                        f"product_id: {product_id} does not exist.")

    @staticmethod
    def delete_wholesaler_product_by_wholesaler_id(wholesaler_id: str):
        """
        This function deletes a wholesaler product by wholesaler id.
        """
        try:
            WholesalerHasProductsServices.delete_wholesaler_product_by_wholesaler_id(wholesaler_id)
            return Response(content=f"Wholesaler product with provided wholesaler_id: {wholesaler_id} "
                                    f"successfully deleted.")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def delete_wholesaler_product_by_product_id(product_id: str):
        """
        It deletes a wholesaler product by product id
        """
        try:
            WholesalerHasProductsServices.delete_wholesaler_product_by_product_id(product_id)
            return Response(content=f"Wholesaler product with provided product_id: {product_id} "
                                    f"successfully deleted.")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_wholesaler_product(wholesaler_id: str, product_id: str, price: float, quantity_available: float):
        """
        It updates the price and quantity available of a product in a wholesaler's inventory
        """
        try:
            return WholesalerHasProductsServices.update_wholesaler_product(wholesaler_id, product_id, price,
                                                                           quantity_available)
        except WholesalerProductNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
