from sqlalchemy.exc import IntegrityError
from app.payment_status.services import PaymentStatusServices
from fastapi import HTTPException, Response


class PaymentStatusController:
    @staticmethod
    def create_payment_status(status_code: str, status_description: str, payment_id: str):
        try:
            payment_status = PaymentStatusServices.create_payment_status(status_code, status_description, payment_id)
            return payment_status
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_payment_statuses():
        payment_statuses = PaymentStatusServices.get_all_payment_statuses()
        return payment_statuses

    @staticmethod
    def get_payment_status_by_id(id: str):
        payment_status = PaymentStatusServices.get_payment_status_by_id(id)
        if payment_status:
            return payment_status
        else:
            raise HTTPException(status_code=400, detail=f"Payment status with provided "
                                                        f"id: {id} does not exist.")

    @staticmethod
    def get_payment_status_by_payment_id(payment_id: str):
        payment_status = PaymentStatusServices.get_payment_status_by_payment_id(payment_id)
        if payment_status:
            return payment_status
        else:
            raise HTTPException(status_code=400, detail=f"Payment status with provided "
                                                        f"id: {payment_id} does not exist.")

    @staticmethod
    def get_payment_status_by_date_and_time(date_and_time: str):
        payment_status = PaymentStatusServices.get_payment_status_by_date_and_time(date_and_time)
        if payment_status:
            return payment_status
        else:
            raise HTTPException(status_code=400, detail=f"Payment status with provided "
                                                        f"date and time: {date_and_time} does not exist.")

    @staticmethod
    def delete_payment_status_by_id(id: str):
        try:
            PaymentStatusServices.delete_payment_status_by_id(id)
            return Response(content=f'Payment status with id: "{id}" successfully deleted.')
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def delete_payment_status_by_date_and_time(date_and_time: str):
        try:
            PaymentStatusServices.delete_payment_status_by_date_and_time(date_and_time)
            return Response(content=f'Payment status with date and time: "{date_and_time}" successfully deleted.')
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_payment_status(id: str, status_code: str):
        try:
            return PaymentStatusServices.update_payment_status(id, status_code)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_payment_status_description(id: str, status_description: str):
        try:
            return PaymentStatusServices.update_payment_status_description(id, status_description)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
