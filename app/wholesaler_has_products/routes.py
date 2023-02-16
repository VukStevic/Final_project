from fastapi import APIRouter
from app.wholesaler_has_products.schemas import WholesalerHasProductsSchema, WholesalerHasProductsSchemaIn
from app.wholesaler_has_products.controllers import WholesalerHasProductsController


wholesaler_has_products_router = APIRouter(prefix="/api/wholesaler-has-products", tags=["Wholesaler has products"])


@wholesaler_has_products_router.post("/create-wholesaler-has-product", response_model=WholesalerHasProductsSchema)
def create_wholesaler_has_products(wholesaler_has_products: WholesalerHasProductsSchemaIn):
    return WholesalerHasProductsController.create_wholesaler_has_products(
        wholesaler_id=wholesaler_has_products.wholesaler_id,
        product_id=wholesaler_has_products.product_id)


@wholesaler_has_products_router.get("/get-all-wholesaler-products", response_model=list[WholesalerHasProductsSchema])
def get_all_wholesaler_products():
    return WholesalerHasProductsController.get_all_wholesaler_products()


@wholesaler_has_products_router.get("/get-wholesaler-product-by-wholesaler-id",
                                    response_model=WholesalerHasProductsSchema)
def get_wholesaler_product_by_wholesaler_id(wholesaler_id: str):
    return WholesalerHasProductsController.get_wholesaler_product_by_wholesaler_id(wholesaler_id=wholesaler_id)


@wholesaler_has_products_router.get("/get-wholesaler-product-by-product-id", response_model=WholesalerHasProductsSchema)
def get_wholesaler_product_by_product_id(product_id: str):
    return WholesalerHasProductsController.get_wholesaler_product_by_product_id(product_id=product_id)


@wholesaler_has_products_router.delete("/delete-wholesaler-product-by-wholesaler-id")
def delete_wholesaler_product_by_wholesaler_id(wholesaler_id: str):
    return WholesalerHasProductsController.delete_wholesaler_product_by_wholesaler_id(wholesaler_id=wholesaler_id)


@wholesaler_has_products_router.delete("/delete-wholesaler-product-by-product-id")
def delete_wholesaler_product_by_product_id(product_id: str):
    return WholesalerHasProductsController.delete_wholesaler_product_by_product_id(product_id=product_id)
