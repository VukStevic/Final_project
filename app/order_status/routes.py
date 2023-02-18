from fastapi import APIRouter
from app.order_status.schemas import OrderStatusSchema, OrderStatusSchemaIn
from app.order_status.controllers import OrderStatusController


order_status_router = APIRouter(prefix="/api/order-status", tags=["Order status"])


@order_status_router.post("/create-order-status", response_model=OrderStatusSchema)
def create_order_status(order_status: OrderStatusSchemaIn):
    return OrderStatusController.create_order_status(status_code=order_status.status_code,
                                                     description=order_status.description,
                                                     order_id=order_status.order_id)


@order_status_router.get("/get-all-order_statuses", response_model=list[OrderStatusSchema])
def get_all_order_statuses():
    return OrderStatusController.get_all_order_statuses()


@order_status_router.get("/get-order_status-by-id", response_model=OrderStatusSchema)
def get_order_status_by_id(id: str):
    return OrderStatusController.get_order_status_by_id(id=id)


@order_status_router.get("/get-order_status-by-date-and-time", response_model=OrderStatusSchema)
def get_order_status_by_date_and_time(date_and_time: str):
    return OrderStatusController.get_order_status_by_date_and_time(date_and_time=date_and_time)


@order_status_router.put("/update-order_status", response_model=OrderStatusSchema)
def update_order_status(id: str, status_code: str):
    return OrderStatusController.update_order_status(id=id, status_code=status_code)


@order_status_router.put("/update-order_status-description", response_model=OrderStatusSchema)
def update_order_status_description(id: str, description: str):
    return OrderStatusController.update_order_status_description(id=id, description=description)


@order_status_router.delete("/delete-order-status-by-id")
def delete_order_status_by_id(id: str):
    return OrderStatusController.delete_order_status_by_id(id=id)


@order_status_router.delete("/delete-order-status-by-date-and-time")
def delete_order_status_by_date_and_time(date_and_time: str):
    return OrderStatusController.delete_order_status_by_date_and_time(date_and_time=date_and_time)
