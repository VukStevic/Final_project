from fastapi import APIRouter
from app.orders.schemas import OrderSchema, OrderSchemaIn, OrderSchemaAnalytics
from app.orders.controllers import OrderController


order_router = APIRouter(prefix="/api/orders", tags=["Orders"])


@order_router.post("/create-order", response_model=OrderSchema)
def create_order(order: OrderSchemaIn):
    return OrderController.create_order(type=order.type, order_date=order.order_date,
                                        wholesaler_id=order.wholesaler_id, retailer_id=order.retailer_id)


@order_router.get("/get-all-orders", response_model=list[OrderSchema])
def get_all_orders():
    return OrderController.get_all_orders()


@order_router.get("/get-order-by-id", response_model=OrderSchema)
def get_order_by_id(order_id: str):
    return OrderController.get_order_by_id(order_id=order_id)


@order_router.get("/get-order-by-wholesaler-id", response_model=list[OrderSchemaAnalytics])
def get_order_by_wholesaler_id(wholesaler_id: str):
    return OrderController.get_order_by_wholesaler_id(wholesaler_id=wholesaler_id)


@order_router.get("/get-order-by-retailer-id", response_model=list[OrderSchemaAnalytics])
def get_order_by_retailer_id(retailer_id: str):
    return OrderController.get_order_by_retailer_id(retailer_id=retailer_id)


@order_router.put("/update-order-type", response_model=OrderSchema)
def update_order_type(order_id: str, type: str):
    return OrderController.update_order_type(order_id=order_id, type=type)


@order_router.put("/update-order-date", response_model=OrderSchema)
def update_order_date(order_id: str, order_date: str):
    return OrderController.update_order_date(order_id=order_id, order_date=order_date)


@order_router.delete("/delete-order-by-id")
def delete_order_by_id(order_id: str):
    return OrderController.delete_order_by_id(order_id=order_id)
