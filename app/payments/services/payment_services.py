from sqlalchemy.exc import IntegrityError
from app.order_product.exceptions import OrderProductNotFoundException
from app.orders.exceptions import OrderNotFoundException
from app.orders.services import OrderServices
from app.payments.repositories import PaymentRepository
from app.db.database import SessionLocal


class PaymentServices:

    @staticmethod
    def create_payment(order_id: str):
        with SessionLocal() as db:
            try:
                payment_repository = PaymentRepository(db)
                return payment_repository.create_payment(order_id)
            except OrderNotFoundException as e:
                raise e
            except IntegrityError as e:
                raise e
            except Exception as e:
                raise e

    @staticmethod
    def get_all_payments():
        with SessionLocal() as db:
            payment_repository = PaymentRepository(db)
            return payment_repository.get_all_payments()

    @staticmethod
    def get_payment_by_id(payment_id: str):
        with SessionLocal() as db:
            payment_repository = PaymentRepository(db)
            return payment_repository.get_payment_by_id(payment_id)

    @staticmethod
    def get_payment_by_order_id(order_id: str):
        with SessionLocal() as db:
            payment_repository = PaymentRepository(db)
            return payment_repository.get_payment_by_order_id(order_id)

    @staticmethod
    def get_payment_by_wholesaler_id(wholesaler_id: str):
        try:
            with SessionLocal() as db:
                orders = OrderServices.get_order_by_wholesaler_id(wholesaler_id)
                payment_repository = PaymentRepository(db)
                payments = []
                for order in orders:
                    payments.append(payment_repository.get_payment_by_order_id(order.id))
                return payments
        except Exception as e:
            raise e

    @staticmethod
    def delete_payment_by_id(payment_id: str):
        try:
            with SessionLocal() as db:
                payment_repository = PaymentRepository(db)
                return payment_repository.delete_payment_by_id(payment_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_payment_by_order_id(order_id: str):
        try:
            with SessionLocal() as db:
                payment_repository = PaymentRepository(db)
                return payment_repository.delete_payment_by_order_id(order_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_payment_amount(order_id: str):
        with SessionLocal() as db:
            try:
                payment_repository = PaymentRepository(db)
                return payment_repository.update_payment_amount(order_id)
            except OrderNotFoundException as e:
                raise e
            except IntegrityError as e:
                raise e
            except Exception as e:
                raise e
