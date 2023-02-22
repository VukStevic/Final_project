from app.db.database import SessionLocal
from app.wholesalers.exceptions.wholesaler_exceptions import WholesalerNotFound
from app.wholesalers.repositories import WholesalerRepository


class WholesalerServices:
    @staticmethod
    def create_wholesaler(name, hq_location, landline, business_email, business_type_id, user_id):
        with SessionLocal() as db:
            try:
                wholesaler_repository = WholesalerRepository(db)
                return wholesaler_repository.create_wholesaler(name, hq_location, landline, business_email,
                                                               business_type_id, user_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_wholesalers():
        with SessionLocal() as db:
            wholesaler_repository = WholesalerRepository(db)
            return wholesaler_repository.get_all_wholesalers()

    @staticmethod
    def get_wholesaler_by_id(wholesaler_id: str):
        with SessionLocal() as db:
            wholesaler_repository = WholesalerRepository(db)
            return wholesaler_repository.get_wholesaler_by_id(wholesaler_id)

    @staticmethod
    def delete_wholesaler_by_id(wholesaler_id: str):
        try:
            with SessionLocal() as db:
                wholesaler_repository = WholesalerRepository(db)
                return wholesaler_repository.delete_wholesaler_by_id(wholesaler_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_wholesaler_name(wholesaler_id: str, name: str):
        with SessionLocal() as db:
            try:
                wholesaler_repository = WholesalerRepository(db)
                return wholesaler_repository.update_wholesaler_name(wholesaler_id, name)
            except Exception as e:
                raise e

    @staticmethod
    def update_wholesaler_landline(wholesaler_id: str, landline: str):
        with SessionLocal() as db:
            try:
                wholesaler_repository = WholesalerRepository(db)
                return wholesaler_repository.update_wholesaler_landline(wholesaler_id, landline)
            except Exception as e:
                raise e

    @staticmethod
    def update_wholesaler_business_email(wholesaler_id: str, business_email: str):
        with SessionLocal() as db:
            try:
                wholesaler_repository = WholesalerRepository(db)
                return wholesaler_repository.update_wholesaler_business_email(wholesaler_id, business_email)
            except Exception as e:
                raise e

    @staticmethod
    def update_wholesaler(wholesaler_id: str, name: str, hq_location: str, landline: str, business_email: str):
        with SessionLocal() as db:
            try:
                wholesaler_repository = WholesalerRepository(db)
                return wholesaler_repository.update_wholesaler(wholesaler_id, name, hq_location, landline,
                                                               business_email)
            except WholesalerNotFound as e:
                raise e
            except Exception as e:
                raise e
