from fastapi import APIRouter
from app.order_product.schemas import OrderProductSchema, OrderProductSchemaIn
from app.order_product.controllers import OrderProductController


order_product_router = APIRouter(prefix="/api/order-product", tags=["Order products"])


@order_product_router.post("/create-order-product", response_model=OrderProductSchema)
def create_order_product(order_product: OrderProductSchemaIn):
    return OrderProductController.create_order_product(order_id=order_product.order_id,
                                                       product_id=order_product.product_id)


@order_product_router.get("/get-all-order-products", response_model=list[OrderProductSchema])
def get_all_order_products():
    return OrderProductController.get_all_order_products()


@order_product_router.get("/get-order-product-by-order-id", response_model=OrderProductSchema)
def get_order_product_by_order_id(order_id: str):
    return OrderProductController.get_order_product_by_order_id(order_id=order_id)


@order_product_router.get("/get-order-product-by-product-id", response_model=OrderProductSchema)
def get_order_product_by_product_id(product_id: str):
    return OrderProductController.get_order_product_by_product_id(product_id=product_id)


@order_product_router.delete("/delete-order-product-by-order-id")
def delete_order_product_by_order_id(order_id: str):
    return OrderProductController.delete_order_product_by_order_id(order_id=order_id)


@order_product_router.delete("/delete-order-product-by-product-id")
def delete_order_product_by_product_id(product_id: str):
    return OrderProductController.get_order_product_by_product_id(product_id=product_id)
