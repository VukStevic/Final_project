from fastapi import APIRouter
from app.order_product.schemas import OrderProductSchema, OrderProductSchemaIn, AveragePriceSchema
from app.order_product.controllers import OrderProductController


order_product_router = APIRouter(prefix="/api/order-product", tags=["Order products"])


@order_product_router.post("/create-order-product", response_model=OrderProductSchema)
def create_order_product(order_product: OrderProductSchemaIn):
    return OrderProductController.create_order_product(order_id=order_product.order_id,
                                                       wholesaler_product_id=order_product.wholesaler_product_id,
                                                       quantity=order_product.quantity)


@order_product_router.get("/get-all-order-products", response_model=list[OrderProductSchema])
def get_all_order_products():
    return OrderProductController.get_all_order_products()


@order_product_router.get("/get-order-product-by-order-id", response_model=list[OrderProductSchema])
def get_order_product_by_order_id(order_id: str):
    return OrderProductController.get_order_product_by_order_id(order_id=order_id)


@order_product_router.get("/get-order-product-by-wholesaler-product-id", response_model=list[OrderProductSchema])
def get_order_product_by_wholesaler_product_id(wholesaler_product_id: str):
    return OrderProductController.get_order_product_by_wholesaler_product_id(
        wholesaler_product_id=wholesaler_product_id)


@order_product_router.get("/get-order-product-by-id", response_model=OrderProductSchema)
def get_order_product_by_id(id: str):
    return OrderProductController.get_order_product_by_id(id=id)


@order_product_router.delete("/delete-order-product-by-order-id")
def delete_order_product_by_order_id(order_id: str):
    return OrderProductController.delete_order_product_by_order_id(order_id=order_id)


@order_product_router.delete("/delete-order-product-by-wholesaler-product-id")
def delete_order_product_by_wholesaler_product_id(wholesaler_product_id: str):
    return OrderProductController.get_order_product_by_wholesaler_product_id(
        wholesaler_product_id=wholesaler_product_id)
