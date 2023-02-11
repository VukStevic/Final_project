from app.business_types.repositories import BusinessTypeRepository
from app.db.database import SessionLocal


class BusinessTypeServices:

    @staticmethod
    def create_business_type(name, description: str):
        with SessionLocal() as db:
            try:
                business_type_repository = BusinessTypeRepository(db)
                return business_type_repository.create_business_type(name, description)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_business_types():
        with SessionLocal() as db:
            business_type_repository = BusinessTypeRepository(db)
            return business_type_repository.get_all_business_types()

    @staticmethod
    def get_business_type_by_id(business_type_id: str):
        with SessionLocal() as db:
            business_type_repository = BusinessTypeRepository(db)
            return business_type_repository.get_business_type_by_id(business_type_id)

    @staticmethod
    def delete_business_type_by_id(business_type_id: str):
        try:
            with SessionLocal() as db:
                business_type_repository = BusinessTypeRepository(db)
                return business_type_repository.delete_business_type_by_id(business_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_business_type_name(business_type_id: str, name: str):
        with SessionLocal() as db:
            try:
                business_type_repository = BusinessTypeRepository(db)
                return business_type_repository.update_business_type_name(business_type_id, name)
            except Exception as e:
                raise e

    @staticmethod
    def update_business_type_description(business_type_id: str, description: str):
        with SessionLocal() as db:
            try:
                business_type_repository = BusinessTypeRepository(db)
                business_type = business_type_repository.update_business_type_description(business_type_id, description)
                return business_type
            except Exception as e:
                raise e
