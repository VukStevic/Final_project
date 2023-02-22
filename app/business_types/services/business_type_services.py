from app.business_types.exceptions.business_type_exceptions import BusinessTypeNotFound
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
        try:
            with SessionLocal() as db:
                business_type_repository = BusinessTypeRepository(db)
                return business_type_repository.get_business_type_by_id(business_type_id)
        except BusinessTypeNotFound as e:
            raise e

    @staticmethod
    def delete_business_type_by_id(business_type_id: str):
        try:
            with SessionLocal() as db:
                business_type_repository = BusinessTypeRepository(db)
                return business_type_repository.delete_business_type_by_id(business_type_id)
        except Exception:
            raise BusinessTypeNotFound(code=400, message=f"Business type with provided id: {business_type_id} "
                                                         f"does not exist.")

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

    @staticmethod
    def update_business_type(business_type_id: str, name: str, description: str):
        with SessionLocal() as db:
            try:
                business_type_repository = BusinessTypeRepository(db)
                business_type = business_type_repository.update_business_type(business_type_id, name, description)
                return business_type
            except Exception:
                raise BusinessTypeNotFound(code=400, message=f"Business type with provided id: {business_type_id} "
                                                             f"does not exist.")
