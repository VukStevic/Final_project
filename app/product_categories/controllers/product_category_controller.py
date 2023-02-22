from sqlalchemy.exc import IntegrityError

from app.product_categories.exceptions import ProductCategoryNotFound
from app.product_categories.services import ProductCategoryServices
from fastapi import HTTPException, Response


class ProductCategoryController:
    @staticmethod
    def create_product_category(name: str, description: str):
        try:
            product_category = ProductCategoryServices.create_product_category(name, description)
            return product_category
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_product_categories():
        product_categories = ProductCategoryServices.get_all_product_categories()
        return product_categories

    @staticmethod
    def get_product_category_by_id(product_category_id: str):
        product_category = ProductCategoryServices.get_product_category_by_id(product_category_id)
        if product_category:
            return product_category
        else:
            raise HTTPException(status_code=400, detail=f"Product category with provided "
                                                        f"id: {product_category_id} does not exist.")

    @staticmethod
    def get_product_category_by_name(name: str):
        product_category = ProductCategoryServices.get_product_category_by_name(name)
        if product_category:
            return product_category
        else:
            raise HTTPException(status_code=400, detail=f"Product category with provided "
                                                        f"name: {name} does not exist.")

    @staticmethod
    def delete_product_category_by_id(product_category_id: str):
        try:
            ProductCategoryServices.delete_product_category_by_id(product_category_id)
            return Response(content=f'Product category with id: "{product_category_id}" successfully deleted.')
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_product_category_name(product_category_id: str, name: str):
        try:
            return ProductCategoryServices.update_product_category_name(product_category_id, name)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_product_category(product_category_id: str, name: str, description: str):
        try:
            return ProductCategoryServices.update_product_category(product_category_id, name, description)
        except ProductCategoryNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
