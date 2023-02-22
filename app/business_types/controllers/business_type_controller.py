from sqlalchemy.exc import IntegrityError
from app.business_types.services import BusinessTypeServices
from fastapi import HTTPException, Response


class BusinessTypeController:
    @staticmethod
    def create_business_type(name, description: str):
        try:
            business_type = BusinessTypeServices.create_business_type(name, description)
            return business_type
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Business type with provided name: {name} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_business_types():
        business_types = BusinessTypeServices.get_all_business_types()
        return business_types

    @staticmethod
    def get_business_type_by_id(business_type_id: str):
        business_type = BusinessTypeServices.get_business_type_by_id(business_type_id)
        if business_type:
            return business_type
        else:
            raise HTTPException(status_code=400, detail=f"Business type with provided "
                                                        f"id: {business_type_id} does not exist.")

    @staticmethod
    def delete_business_type_by_id(business_type_id: str):
        try:
            BusinessTypeServices.delete_business_type_by_id(business_type_id)
            return Response(content=f'Business type with id: "{business_type_id}" successfully deleted.')
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_business_type_name(business_type_id: str, name: str):
        try:
            return BusinessTypeServices.update_business_type_name(business_type_id, name)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_business_type_description(business_type_id: str, description: str):
        try:
            return BusinessTypeServices.update_business_type_description(business_type_id, description)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_business_type(business_type_id: str, name: str, description: str):
        try:
            return BusinessTypeServices.update_business_type(business_type_id, name, description)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
