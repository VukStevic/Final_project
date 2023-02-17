from fastapi import APIRouter
from app.payment_status.schemas import PaymentStatusSchema, PaymentStatusSchemaIn
from app.payment_status.controllers import PaymentStatusController


payment_status_router = APIRouter(prefix="/api/payment-status", tags=["Payment status"])


@payment_status_router.post("/create-payment-status", response_model=PaymentStatusSchema)
def create_payment_status(payment_status: PaymentStatusSchemaIn):
    return PaymentStatusController.create_payment_status(status_code=payment_status.status_code,
                                                         status_description=payment_status.status_description,
                                                         date_and_time=payment_status.date_and_time,
                                                         payment_id=payment_status.payment_id)


@payment_status_router.get("/get-all-payment_statuses", response_model=list[PaymentStatusSchema])
def get_all_payment_statuses():
    return PaymentStatusController.get_all_payment_statuses()


@payment_status_router.get("/get-payment_status-by-status-code", response_model=PaymentStatusSchema)
def get_payment_status_by_status_code(status_code: str):
    return PaymentStatusController.get_payment_status_by_status_code(status_code=status_code)


@payment_status_router.get("/get-payment_status-by-date-and-time", response_model=PaymentStatusSchema)
def get_payment_status_by_date_and_time(date_and_time: str):
    return PaymentStatusController.get_payment_status_by_date_and_time(date_and_time=date_and_time)


@payment_status_router.put("/update-payment_status", response_model=PaymentStatusSchema)
def update_payment_status(status_code: str, new_status_code: str):
    return PaymentStatusController.update_payment_status(status_code=status_code, new_status_code=new_status_code)


@payment_status_router.put("/update-payment_status-description", response_model=PaymentStatusSchema)
def update_payment_status_description(status_code: str, status_description: str):
    return PaymentStatusController.update_payment_status_description(status_code=status_code,
                                                                     status_description=status_description)
