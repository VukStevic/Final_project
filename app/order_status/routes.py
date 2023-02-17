from fastapi import APIRouter
from app.order_status.schemas import OrderStatusSchema, OrderStatusSchemaIn
from app.order_status.controllers import OrderStatusController


order_status_router = APIRouter(prefix="/api/order-status", tags=["Order status"])


@order_status_router.post("/create-order-status", response_model=OrderStatusSchema)
def create_order_status(order_status: OrderStatusSchemaIn):
    return OrderStatusController.create_order_status(status_code=order_status.status_code,
                                                     description=order_status.description,
                                                     date_and_time=order_status.date_and_time,
                                                     order_id=order_status.order_id)


@order_status_router.get("/get-all-order_statuses", response_model=list[OrderStatusSchema])
def get_all_order_statuses():
    return OrderStatusController.get_all_order_statuses()


@order_status_router.get("/get-order_status-by-status-code", response_model=OrderStatusSchema)
def get_order_status_by_status_code(status_code: str):
    return OrderStatusController.get_order_status_by_status_code(status_code=status_code)


@order_status_router.get("/get-order_status-by-date-and-time", response_model=OrderStatusSchema)
def get_order_status_by_date_and_time(date_and_time: str):
    return OrderStatusController.get_order_status_by_date_and_time(date_and_time=date_and_time)


@order_status_router.put("/update-order_status", response_model=OrderStatusSchema)
def update_order_status(status_code: str, new_status_code: str):
    return OrderStatusController.update_order_status(status_code=status_code, new_status_code=new_status_code)


@order_status_router.put("/update-order_status-description", response_model=OrderStatusSchema)
def update_order_status_description(status_code: str, description: str):
    return OrderStatusController.update_order_status_description(status_code=status_code,
                                                                 description=description)
