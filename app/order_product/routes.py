from fastapi import APIRouter, Depends
from app.order_product.schemas import OrderProductSchema, OrderProductSchemaIn, OrderProductSchemaUpdate
from app.order_product.controllers import OrderProductController
from app.users.controllers import JWTBearer

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


@order_product_router.put("/update-order-product", response_model=OrderProductSchema)
def update_order_product(order_product: OrderProductSchemaUpdate):
    return OrderProductController.update_order_product(id=order_product.id, quantity=order_product.quantity)


@order_product_router.delete("/delete-order-product-by-order-id", dependencies=[Depends(JWTBearer("super_user"))])
def delete_order_product_by_order_id(order_id: str):
    return OrderProductController.delete_order_product_by_order_id(order_id=order_id)


@order_product_router.delete("/delete-order-product-by-wholesaler-product-id",
                             dependencies=[Depends(JWTBearer("super_user"))])
def delete_order_product_by_wholesaler_product_id(wholesaler_product_id: str):
    return OrderProductController.get_order_product_by_wholesaler_product_id(
        wholesaler_product_id=wholesaler_product_id)
