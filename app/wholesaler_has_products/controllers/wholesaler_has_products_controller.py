from sqlalchemy.exc import IntegrityError
from app.wholesaler_has_products.services import WholesalerHasProductsServices
from fastapi import HTTPException, Response


class WholesalerHasProductsController:
    @staticmethod
    def create_wholesaler_has_products(wholesaler_id: str, product_id: str, price: float, quantity_available: float):
        try:
            wholesaler_has_products = WholesalerHasProductsServices.create_wholesaler_product(wholesaler_id, product_id,
                                                                                              price, quantity_available)
            return wholesaler_has_products
        except IntegrityError as e:
            return str(e)
            # raise HTTPException(status_code=400, detail=f"Wholesaler product with provided "
            #                                             f"wholesaler_id/product_id: {wholesaler_id, product_id} "
            #                                             f"already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_wholesaler_products():
        wholesaler_has_products = WholesalerHasProductsServices.get_all_wholesaler_products()
        return wholesaler_has_products

    @staticmethod
    def get_wholesaler_product_by_wholesaler_id(wholesaler_id: str):
        wholesaler_has_products = WholesalerHasProductsServices.get_wholesaler_product_by_wholesaler_id(wholesaler_id)
        if wholesaler_has_products:
            return wholesaler_has_products
        else:
            raise HTTPException(status_code=400, detail=f"Wholesaler product with provided "
                                                        f"wholesaler_id: {wholesaler_id} does not exist.")

    @staticmethod
    def get_wholesaler_product_by_id(id: str):
        wholesaler_has_products = WholesalerHasProductsServices.get_wholesaler_product_by_id(id)
        if wholesaler_has_products:
            return wholesaler_has_products
        else:
            raise HTTPException(status_code=400, detail=f"Wholesaler product with provided "
                                                        f"id: {id} does not exist.")

    @staticmethod
    def get_wholesaler_product_by_product_id(product_id: str):
        wholesaler_has_products = WholesalerHasProductsServices.get_wholesaler_product_by_product_id(product_id)
        if wholesaler_has_products:
            return wholesaler_has_products
        else:
            raise HTTPException(status_code=400, detail=f"Wholesaler product with provided "
                                                        f"product_id: {product_id} does not exist.")

    @staticmethod
    def delete_wholesaler_product_by_wholesaler_id(wholesaler_id: str):
        try:
            WholesalerHasProductsServices.delete_wholesaler_product_by_wholesaler_id(wholesaler_id)
            return Response(content=f"Wholesaler product with provided wholesaler_id: {wholesaler_id} "
                                    f"successfully deleted.")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def delete_wholesaler_product_by_product_id(product_id: str):
        try:
            WholesalerHasProductsServices.delete_wholesaler_product_by_product_id(product_id)
            return Response(content=f"Wholesaler product with provided product_id: {product_id} "
                                    f"successfully deleted.")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_wholesaler_product_price(wholesaler_id: str, product_id: str, price: float):
        try:
            return WholesalerHasProductsServices.update_wholesaler_product_price(wholesaler_id, product_id, price)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_wholesaler_product_quantity_available(wholesaler_id: str, product_id: str, quantity_available: float):
        try:
            return WholesalerHasProductsServices.update_wholesaler_product_quantity_available(wholesaler_id,
                                                                                              product_id,
                                                                                              quantity_available)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
