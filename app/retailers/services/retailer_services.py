from app.db.database import SessionLocal
from app.retailers.exceptions.retailer_exceptions import RetailerNotFound
from app.retailers.repositories import RetailerRepository


class RetailerServices:
    @staticmethod
    def create_retailer(name, hq_location, landline, business_email, business_type_id, user_id):
        with SessionLocal() as db:
            try:
                retailer_repository = RetailerRepository(db)
                return retailer_repository.create_retailer(name, hq_location, landline, business_email, 
                                                           business_type_id, user_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_retailers():
        with SessionLocal() as db:
            retailer_repository = RetailerRepository(db)
            return retailer_repository.get_all_retailers()

    @staticmethod
    def get_retailer_by_id(retailer_id: str):
        with SessionLocal() as db:
            retailer_repository = RetailerRepository(db)
            return retailer_repository.get_retailer_by_id(retailer_id)

    @staticmethod
    def delete_retailer_by_id(retailer_id: str):
        try:
            with SessionLocal() as db:
                retailer_repository = RetailerRepository(db)
                return retailer_repository.delete_retailer_by_id(retailer_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_retailer_name(retailer_id: str, name: str):
        with SessionLocal() as db:
            try:
                retailer_repository = RetailerRepository(db)
                return retailer_repository.update_retailer_name(retailer_id, name)
            except Exception as e:
                raise e

    @staticmethod
    def update_retailer_landline(retailer_id: str, landline: str):
        with SessionLocal() as db:
            try:
                retailer_repository = RetailerRepository(db)
                return retailer_repository.update_retailer_landline(retailer_id, landline)
            except Exception as e:
                raise e

    @staticmethod
    def update_retailer_business_email(retailer_id: str, business_email: str):
        with SessionLocal() as db:
            try:
                retailer_repository = RetailerRepository(db)
                return retailer_repository.update_retailer_business_email(retailer_id, business_email)
            except Exception as e:
                raise e

    @staticmethod
    def update_retailer(retailer_id: str, name: str, hq_location: str, landline: str, business_email: str):
        with SessionLocal() as db:
            try:
                retailer_repository = RetailerRepository(db)
                return retailer_repository.update_retailer(retailer_id, name, hq_location, landline, business_email)
            except RetailerNotFound as e:
                raise e
            except Exception as e:
                raise e
