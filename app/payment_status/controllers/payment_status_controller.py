from sqlalchemy.exc import IntegrityError
from app.payment_status.services import PaymentStatusServices
from fastapi import HTTPException, Response


class PaymentStatusController:
    @staticmethod
    def create_payment_status(status_code: str, status_description: str, date_and_time: str, payment_id: str):
        try:
            payment_status = PaymentStatusServices.create_payment_status(status_code, status_description, date_and_time,
                                                                         payment_id)
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
    def get_payment_status_by_status_code(status_code: str):
        payment_status = PaymentStatusServices.get_payment_status_by_status_code(status_code)
        if payment_status:
            return payment_status
        else:
            raise HTTPException(status_code=400, detail=f"Payment status with provided "
                                                        f"status code: {status_code} does not exist.")

    @staticmethod
    def get_payment_status_by_date_and_time(date_and_time: str):
        payment_status = PaymentStatusServices.get_payment_status_by_date_and_time(date_and_time)
        if payment_status:
            return payment_status
        else:
            raise HTTPException(status_code=400, detail=f"Payment status with provided "
                                                        f"date and time: {date_and_time} does not exist.")

    @staticmethod
    def delete_payment_status_by_status_code(status_code: str):
        try:
            PaymentStatusServices.delete_payment_status_by_status_code(status_code)
            return Response(content=f'Payment status with status code: "{status_code}" successfully deleted.')
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
    def update_payment_status(status_code: str, new_status_code: str):
        try:
            return PaymentStatusServices.update_payment_status(status_code, new_status_code)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_payment_status_description(status_code: str, status_description: str):
        try:
            return PaymentStatusServices.update_payment_status_description(status_code, status_description)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
