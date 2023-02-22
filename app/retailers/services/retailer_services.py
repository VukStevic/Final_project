from app.db.database import SessionLocal
from app.retailers.exceptions.retailer_exceptions import RetailerNotFound
from app.retailers.repositories import RetailerRepository


class RetailerServices:
    @staticmethod
    def create_retailer(name, hq_location, landline, business_email, business_type_id, user_id):
        """
        It creates a retailer
        """
        with SessionLocal() as db:
            try:
                retailer_repository = RetailerRepository(db)
                return retailer_repository.create_retailer(name, hq_location, landline, business_email, 
                                                           business_type_id, user_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_retailers():
        """
        It gets all the retailers from the database
        """
        with SessionLocal() as db:
            retailer_repository = RetailerRepository(db)
            return retailer_repository.get_all_retailers()

    @staticmethod
    def get_retailer_by_id(retailer_id: str):
        """
        > This function gets a retailer by id
        """
        with SessionLocal() as db:
            retailer_repository = RetailerRepository(db)
            return retailer_repository.get_retailer_by_id(retailer_id)

    @staticmethod
    def delete_retailer_by_id(retailer_id: str):
        """
        It deletes a retailer from the database by its id
        """
        try:
            with SessionLocal() as db:
                retailer_repository = RetailerRepository(db)
                return retailer_repository.delete_retailer_by_id(retailer_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_retailer(retailer_id: str, name: str, hq_location: str, landline: str, business_email: str):
        """
        It updates a retailer's details in the database
        """
        with SessionLocal() as db:
            try:
                retailer_repository = RetailerRepository(db)
                return retailer_repository.update_retailer(retailer_id, name, hq_location, landline, business_email)
            except RetailerNotFound as e:
                raise e
            except Exception as e:
                raise e
