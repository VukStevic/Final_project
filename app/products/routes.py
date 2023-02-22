from fastapi import APIRouter, Depends
from app.products.schemas import ProductSchema, ProductSchemaIn, ProductSchemaUpdate
from app.products.controllers import ProductController
from app.users.controllers import JWTBearer

product_router = APIRouter(prefix="/api/products", tags=["Products"])


@product_router.post("/create-product", response_model=ProductSchema)
def create_product(product: ProductSchemaIn):
    return ProductController.create_product(name=product.name,
                                            description=product.description,
                                            product_category_id=product.product_category_id)


@product_router.get("/get-all-products", response_model=list[ProductSchema])
def get_all_products():
    return ProductController.get_all_products()


@product_router.get("/get-product-by-id", response_model=ProductSchema)
def get_product_by_id(product_id: str):
    return ProductController.get_product_by_id(product_id=product_id)


@product_router.get("/get-product-by-name", response_model=ProductSchema)
def get_product_by_name(name: str):
    return ProductController.get_product_by_name(name=name)


@product_router.put("/update-product", response_model=ProductSchema)
def update_product(product: ProductSchemaUpdate):
    return ProductController.update_product(product_id=product.product_id, name=product.name,
                                            description=product.description)


@product_router.delete("/delete-product-by-id", dependencies=[Depends(JWTBearer("super_user"))])
def delete_product_by_id(product_id: str):
    return ProductController.delete_product_by_id(product_id=product_id)
