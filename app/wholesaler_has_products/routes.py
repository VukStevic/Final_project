from fastapi import APIRouter, Depends
from app.users.controllers import JWTBearer
from app.wholesaler_has_products.schemas import WholesalerHasProductsSchema, WholesalerHasProductsSchemaIn, \
    WholesalerHasProductsSchemaUpdate
from app.wholesaler_has_products.controllers import WholesalerHasProductsController


wholesaler_has_products_router = APIRouter(prefix="/api/wholesaler-has-products", tags=["Wholesaler has products"])


@wholesaler_has_products_router.post("/create-wholesaler-has-product", response_model=WholesalerHasProductsSchema)
def create_wholesaler_has_products(wholesaler_has_products: WholesalerHasProductsSchemaIn):
    return WholesalerHasProductsController.create_wholesaler_has_products(
        wholesaler_id=wholesaler_has_products.wholesaler_id,
        product_id=wholesaler_has_products.product_id,
        price=wholesaler_has_products.price,
        quantity_available=wholesaler_has_products.quantity_available)


@wholesaler_has_products_router.get("/get-all-wholesaler-products", response_model=list[WholesalerHasProductsSchema])
def get_all_wholesaler_products():
    return WholesalerHasProductsController.get_all_wholesaler_products()


@wholesaler_has_products_router.get("/get-wholesaler-product-by-wholesaler-id",
                                    response_model=WholesalerHasProductsSchema)
def get_wholesaler_product_by_wholesaler_id(wholesaler_id: str):
    return WholesalerHasProductsController.get_wholesaler_product_by_wholesaler_id(wholesaler_id=wholesaler_id)


@wholesaler_has_products_router.get("/get-wholesaler-product-by-id", response_model=WholesalerHasProductsSchema)
def get_wholesaler_product_by_id(id: str):
    return WholesalerHasProductsController.get_wholesaler_product_by_id(id=id)


@wholesaler_has_products_router.get("/get-wholesaler-product-by-product-id", response_model=WholesalerHasProductsSchema)
def get_wholesaler_product_by_product_id(product_id: str):
    return WholesalerHasProductsController.get_wholesaler_product_by_product_id(product_id=product_id)


@wholesaler_has_products_router.put("/update-wholesaler-product-price", response_model=WholesalerHasProductsSchema)
def update_wholesaler_product_price(wholesaler_id: str, product_id: str, price: float):
    return WholesalerHasProductsController.update_wholesaler_product_price(
        wholesaler_id=wholesaler_id,
        product_id=product_id,
        price=price)


@wholesaler_has_products_router.put("/update-wholesaler-product-quantity-available",
                                    response_model=WholesalerHasProductsSchema)
def update_wholesaler_product_quantity_available(wholesaler_id: str, product_id: str, quantity_available: float):
    return WholesalerHasProductsController.update_wholesaler_product_quantity_available(
        wholesaler_id=wholesaler_id,
        product_id=product_id,
        quantity_available=quantity_available)


@wholesaler_has_products_router.put("/update-wholesaler-product", response_model=WholesalerHasProductsSchema)
def update_wholesaler_product(wholesaler_product: WholesalerHasProductsSchemaUpdate):
    return WholesalerHasProductsController.update_wholesaler_product(
        id=wholesaler_product.id, wholesaler_id=wholesaler_product.wholesaler_id,
        quantity_available=wholesaler_product.quantity_available, price=wholesaler_product.price,
        product_id=wholesaler_product.product_id)


@wholesaler_has_products_router.delete("/delete-wholesaler-product-by-wholesaler-id",
                                       dependencies=[Depends(JWTBearer("super_user"))])
def delete_wholesaler_product_by_wholesaler_id(wholesaler_id: str):
    return WholesalerHasProductsController.delete_wholesaler_product_by_wholesaler_id(wholesaler_id=wholesaler_id)


@wholesaler_has_products_router.delete("/delete-wholesaler-product-by-product-id",
                                       dependencies=[Depends(JWTBearer("super_user"))])
def delete_wholesaler_product_by_product_id(product_id: str):
    return WholesalerHasProductsController.delete_wholesaler_product_by_product_id(product_id=product_id)
