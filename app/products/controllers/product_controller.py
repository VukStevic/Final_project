from sqlalchemy.exc import IntegrityError
from app.products.services import ProductServices
from fastapi import HTTPException, Response


class ProductController:
    @staticmethod
    def create_product(name: str, description: str, price: float, quantity_available: float,
                       product_category_id: str):
        try:
            product = ProductServices.create_product(name, description, price, quantity_available, product_category_id)
            return product
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_products():
        products = ProductServices.get_all_products()
        return products

    @staticmethod
    def get_product_by_id(product_id: str):
        product = ProductServices.get_product_by_id(product_id)
        if product:
            return product
        else:
            raise HTTPException(status_code=400, detail=f"Product with provided "
                                                        f"id: {product_id} does not exist.")

    @staticmethod
    def get_product_by_name(name: str):
        product = ProductServices.get_product_by_name(name)
        if product:
            return product
        else:
            raise HTTPException(status_code=400, detail=f"Product with provided "
                                                        f"name: {name} does not exist.")

    @staticmethod
    def delete_product_by_id(product_id: str):
        try:
            ProductServices.delete_product_by_id(product_id)
            return Response(content=f'Product with id: "{product_id}" successfully deleted.')
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_product_description(product_id: str, description: str):
        try:
            return ProductServices.update_product_description(product_id, description)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_product_price(product_id: str, price: float):
        try:
            return ProductServices.update_product_price(product_id, price)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_product_quantity_available(product_id: str, quantity_available: float):
        try:
            return ProductServices.update_product_quantity_available(product_id, quantity_available)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
