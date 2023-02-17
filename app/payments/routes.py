from fastapi import APIRouter
from app.payments.schemas import PaymentSchema, PaymentSchemaIn
from app.payments.controllers import PaymentController


payment_router = APIRouter(prefix="/api/payments", tags=["Payments"])


@payment_router.post("/create-payment", response_model=PaymentSchema)
def create_payment(payment: PaymentSchemaIn):
    return PaymentController.create_payment(payment_amount=payment.payment_amount, order_id=payment.order_id)


@payment_router.get("/get-all-payments", response_model=list[PaymentSchema])
def get_all_payments():
    return PaymentController.get_all_payments()


@payment_router.get("/get-payment-by-id", response_model=PaymentSchema)
def get_payment_by_id(payment_id: str):
    return PaymentController.get_payment_by_id(payment_id=payment_id)


@payment_router.get("/get-payment-by-order-id", response_model=PaymentSchema)
def get_payment_by_order_id(order_id: str):
    return PaymentController.get_payment_by_order_id(order_id=order_id)


@payment_router.put("/update-payment-amount", response_model=PaymentSchema)
def update_payment_amount(payment_id: str, payment_amount: float):
    return PaymentController.update_payment_amount(payment_id=payment_id, payment_amount=payment_amount)


@payment_router.delete("/delete-payment-by-id")
def delete_payment_by_id(payment_id: str):
    return PaymentController.delete_payment_by_id(payment_id=payment_id)


@payment_router.delete("/delete-payment-by-order-id")
def delete_payment_by_order_id(order_id: str):
    return PaymentController.delete_payment_by_order_id(order_id=order_id)
