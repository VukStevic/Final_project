from app.db.database import SessionLocal
from app.wholesalers.exceptions.wholesaler_exceptions import WholesalerNotFound
from app.wholesalers.repositories import WholesalerRepository


class WholesalerServices:
    @staticmethod
    def create_wholesaler(name, hq_location, landline, business_email, business_type_id, user_id):
        """
        It creates a wholesaler
        """
        with SessionLocal() as db:
            try:
                wholesaler_repository = WholesalerRepository(db)
                return wholesaler_repository.create_wholesaler(name, hq_location, landline, business_email,
                                                               business_type_id, user_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_wholesalers():
        """
        It gets all the wholesalers from the database
        """
        with SessionLocal() as db:
            wholesaler_repository = WholesalerRepository(db)
            return wholesaler_repository.get_all_wholesalers()

    @staticmethod
    def get_wholesaler_by_id(wholesaler_id: str):
        """
        > This function gets a wholesaler by id
        """
        with SessionLocal() as db:
            wholesaler_repository = WholesalerRepository(db)
            return wholesaler_repository.get_wholesaler_by_id(wholesaler_id)

    @staticmethod
    def delete_wholesaler_by_id(wholesaler_id: str):
        """
        It deletes a wholesaler from the database by its id
        """
        try:
            with SessionLocal() as db:
                wholesaler_repository = WholesalerRepository(db)
                return wholesaler_repository.delete_wholesaler_by_id(wholesaler_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_wholesaler(wholesaler_id: str, name: str, hq_location: str, landline: str, business_email: str):
        """
        It updates a wholesaler's details
        """
        with SessionLocal() as db:
            try:
                wholesaler_repository = WholesalerRepository(db)
                return wholesaler_repository.update_wholesaler(wholesaler_id, name, hq_location, landline,
                                                               business_email)
            except WholesalerNotFound as e:
                raise e
            except Exception as e:
                raise e
