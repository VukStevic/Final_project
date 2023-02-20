from fastapi import APIRouter, Depends
from app.payments.schemas import PaymentSchema
from app.payments.controllers import PaymentController
from app.users.controllers import JWTBearer

payment_router = APIRouter(prefix="/api/payments", tags=["Payments"])


@payment_router.post("/create-payment", response_model=PaymentSchema)
def create_payment(order_id: str):
    return PaymentController.create_payment(order_id=order_id)


@payment_router.get("/get-all-payments", response_model=list[PaymentSchema])
def get_all_payments():
    return PaymentController.get_all_payments()


@payment_router.get("/get-payment-by-id", response_model=PaymentSchema)
def get_payment_by_id(payment_id: str):
    return PaymentController.get_payment_by_id(payment_id=payment_id)


@payment_router.get("/get-payment-by-order-id", response_model=PaymentSchema)
def get_payment_by_order_id(order_id: str):
    return PaymentController.get_payment_by_order_id(order_id=order_id)


@payment_router.delete("/delete-payment-by-id", dependencies=[Depends(JWTBearer("super_user"))])
def delete_payment_by_id(payment_id: str):
    return PaymentController.delete_payment_by_id(payment_id=payment_id)


@payment_router.delete("/delete-payment-by-order-id", dependencies=[Depends(JWTBearer("super_user"))])
def delete_payment_by_order_id(order_id: str):
    return PaymentController.delete_payment_by_order_id(order_id=order_id)


@payment_router.put("/update-payment-amount", response_model=PaymentSchema)
def update_payment_amount(order_id: str):
    return PaymentController.update_payment_amount(order_id=order_id)
