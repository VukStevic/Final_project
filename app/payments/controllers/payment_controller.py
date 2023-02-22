from sqlalchemy.exc import IntegrityError
from app.orders.exceptions import OrderNotFoundException
from app.payments.services import PaymentServices
from fastapi import HTTPException, Response


class PaymentController:
    @staticmethod
    def create_payment(order_id: str):
        try:
            payment = PaymentServices.create_payment(order_id)
            return payment
        except OrderNotFoundException:
            raise HTTPException(status_code=400, detail=f"Order with provided order id: {order_id} not found.")
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Payment with order id: {order_id} already exists. "
                                                        f"If additional products are added to the order, use "
                                                        f"update request to update the payment amount.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_payments():
        payments = PaymentServices.get_all_payments()
        return payments

    @staticmethod
    def get_payment_by_id(payment_id: str):
        payment = PaymentServices.get_payment_by_id(payment_id)
        if payment:
            return payment
        else:
            raise HTTPException(status_code=400, detail=f"Payment with provided payment "
                                                        f"id: {payment_id} does not exist.")

    @staticmethod
    def get_payment_by_order_id(order_id: str):
        payment = PaymentServices.get_payment_by_order_id(order_id)
        if payment:
            return payment
        else:
            raise HTTPException(status_code=400, detail=f"Payment with provided order "
                                                        f"id: {order_id} does not exist.")

    @staticmethod
    def get_payment_by_wholesaler_id(wholesaler_id: str):
        try:
            payment = PaymentServices.get_payment_by_wholesaler_id(wholesaler_id)
            if payment:
                return payment
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_payment_by_id(payment_id: str):
        try:
            PaymentServices.delete_payment_by_id(payment_id)
            return Response(content=f'Payment with payment id: "{payment_id}" successfully deleted.')
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def delete_payment_by_order_id(order_id: str):
        try:
            PaymentServices.delete_payment_by_order_id(order_id)
            return Response(content=f'Payment with order id: "{order_id}" successfully deleted.')
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_payment_amount(order_id: str):
        try:
            return PaymentServices.update_payment_amount(order_id)
        except OrderNotFoundException:
            raise HTTPException(status_code=400, detail=f"Order with provided order id: {order_id} not found.")
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Payment with provided order id: {order_id} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
