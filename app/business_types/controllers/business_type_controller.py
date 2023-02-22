from sqlalchemy.exc import IntegrityError
from app.business_types.exceptions.business_type_exceptions import BusinessTypeNotFound
from app.business_types.services import BusinessTypeServices
from fastapi import HTTPException, Response


class BusinessTypeController:
    @staticmethod
    def create_business_type(name, description: str):
        """
        It creates a business type
        """
        try:
            business_type = BusinessTypeServices.create_business_type(name, description)
            return business_type
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Business type with provided name: {name} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_business_types():
        """
        It returns a list of all business types
        """
        business_types = BusinessTypeServices.get_all_business_types()
        return business_types

    @staticmethod
    def get_business_type_by_id(business_type_id: str):
        """
        It returns the business type by id.
        """
        try:
            return BusinessTypeServices.get_business_type_by_id(business_type_id)
        except BusinessTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)

    @staticmethod
    def delete_business_type_by_id(business_type_id: str):
        """
        It deletes a business type by id.
        """
        try:
            BusinessTypeServices.delete_business_type_by_id(business_type_id)
            return Response(content=f'Business type with id: "{business_type_id}" successfully deleted.')
        except BusinessTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)

    @staticmethod
    def update_business_type(business_type_id: str, name: str, description: str):
        """
        It updates the business type.
        """
        try:
            return BusinessTypeServices.update_business_type(business_type_id, name, description)
        except BusinessTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
