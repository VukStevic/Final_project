from fastapi import APIRouter
from app.payment_status.schemas import PaymentStatusSchema, PaymentStatusSchemaIn
from app.payment_status.controllers import PaymentStatusController


payment_status_router = APIRouter(prefix="/api/payment-status", tags=["Payment status"])


@payment_status_router.post("/create-payment-status", response_model=PaymentStatusSchema)
def create_payment_status(payment_status: PaymentStatusSchemaIn):
    return PaymentStatusController.create_payment_status(status_code=payment_status.status_code,
                                                         status_description=payment_status.status_description,
                                                         payment_id=payment_status.payment_id)


@payment_status_router.get("/get-all-payment_statuses", response_model=list[PaymentStatusSchema])
def get_all_payment_statuses():
    return PaymentStatusController.get_all_payment_statuses()


@payment_status_router.get("/get-payment_status-by-id", response_model=PaymentStatusSchema)
def get_payment_status_by_id(id: str):
    return PaymentStatusController.get_payment_status_by_id(id=id)


@payment_status_router.get("/get-payment_status-by-date-and-time", response_model=PaymentStatusSchema)
def get_payment_status_by_date_and_time(date_and_time: str):
    return PaymentStatusController.get_payment_status_by_date_and_time(date_and_time=date_and_time)


@payment_status_router.put("/update-payment_status", response_model=PaymentStatusSchema)
def update_payment_status(id: str, status_code: str):
    return PaymentStatusController.update_payment_status(id=id, status_code=status_code)


@payment_status_router.put("/update-payment_status-description", response_model=PaymentStatusSchema)
def update_payment_status_description(id: str, status_description: str):
    return PaymentStatusController.update_payment_status_description(id=id,
                                                                     status_description=status_description)


@payment_status_router.delete("/delete-payment-status-by-id")
def delete_payment_status_by_id(id: str):
    return PaymentStatusController.delete_payment_status_by_id(id=id)


@payment_status_router.delete("/delete-payment-status-by-date-and-time")
def delete_payment_status_by_date_and_time(date_and_time: str):
    return PaymentStatusController.delete_payment_status_by_date_and_time(date_and_time=date_and_time)
