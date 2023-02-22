from sqlalchemy.exc import IntegrityError

from app.products.exceptions.product_exceptions import ProductNotFound
from app.products.services import ProductServices
from fastapi import HTTPException, Response


class ProductController:
    @staticmethod
    def create_product(name: str, description: str, product_category_id: str):
        """
        It creates a product
        """
        try:
            product = ProductServices.create_product(name, description, product_category_id)
            return product
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_products():
        """
        It returns all products
        """
        products = ProductServices.get_all_products()
        return products

    @staticmethod
    def get_product_by_id(product_id: str):
        """
        If the product exists, return it, otherwise raise an exception
        """
        product = ProductServices.get_product_by_id(product_id)
        if product:
            return product
        else:
            raise HTTPException(status_code=400, detail=f"Product with provided "
                                                        f"id: {product_id} does not exist.")

    @staticmethod
    def get_product_by_name(name: str):
        """
        If the product exists, return it, otherwise raise an exception
        """
        product = ProductServices.get_product_by_name(name)
        if product:
            return product
        else:
            raise HTTPException(status_code=400, detail=f"Product with provided "
                                                        f"name: {name} does not exist.")

    @staticmethod
    def delete_product_by_id(product_id: str):
        """
        It takes a product_id as a string, and if it's valid, it deletes the product from the database
        """
        try:
            ProductServices.delete_product_by_id(product_id)
            return Response(content=f'Product with id: "{product_id}" successfully deleted.')
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_product(product_id: str, name: str, description: str):
        """
        It updates a product.
        """
        try:
            return ProductServices.update_product(product_id, name, description)
        except ProductNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
