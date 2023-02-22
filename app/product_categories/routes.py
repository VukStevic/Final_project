from fastapi import APIRouter, Depends
from app.product_categories.schemas import ProductCategorySchema, ProductCategorySchemaIn, ProductCategorySchemaUpdate
from app.product_categories.controllers import ProductCategoryController
from app.users.controllers import JWTBearer

product_category_router = APIRouter(prefix="/api/product_categories", tags=["Product categories"])


@product_category_router.post("/create-product_category", response_model=ProductCategorySchema)
def create_product_category(product_category: ProductCategorySchemaIn):
    return ProductCategoryController.create_product_category(name=product_category.name,
                                                             description=product_category.description)


@product_category_router.get("/get-all-product-categories", response_model=list[ProductCategorySchema])
def get_all_product_categories():
    return ProductCategoryController.get_all_product_categories()


@product_category_router.get("/get-product_category-by-id", response_model=ProductCategorySchema)
def get_product_category_by_id(product_category_id: str):
    return ProductCategoryController.get_product_category_by_id(product_category_id=product_category_id)


@product_category_router.get("/get-product_category-by-name", response_model=ProductCategorySchema)
def get_product_category_by_name(name: str):
    return ProductCategoryController.get_product_category_by_name(name=name)


@product_category_router.put("/update-product_category", response_model=ProductCategorySchema)
def update_product_category(product_category: ProductCategorySchemaUpdate):
    return ProductCategoryController.update_product_category(product_category_id=product_category.product_category_id,
                                                             name=product_category.name,
                                                             description=product_category.description)


@product_category_router.delete("/delete-product_category-by-id", dependencies=[Depends(JWTBearer("super_user"))])
def delete_product_category_by_id(product_category_id: str):
    return ProductCategoryController.delete_product_category_by_id(product_category_id=product_category_id)
