from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from app.retailers.services import RetailerServices


class RetailerController:
    @staticmethod
    def create_retailer(name, hq_location, landline, business_email, business_type_id, user_id):
        try:
            retailer = RetailerServices.create_retailer(name, hq_location, landline, business_email, 
                                                        business_type_id, user_id)
            return retailer
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"Retailer with provided business email - {business_email} already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_retailers():
        retailers = RetailerServices.get_all_retailers()
        return retailers

    @staticmethod
    def get_retailer_by_id(retailer_id: str):
        retailer = RetailerServices.get_retailer_by_id(retailer_id)
        if retailer:
            return retailer
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Retailer with provided id {retailer_id} does not exist",
            )

    @staticmethod
    def delete_retailer_by_id(retailer_id: str):
        try:
            RetailerServices.delete_retailer_by_id(retailer_id)
            return {"message": f"Retailer with provided id, {retailer_id}, is deleted."}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_retailer_name(retailer_id: str, name: str):
        try:
            return RetailerServices.update_retailer_name(retailer_id, name)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_retailer_landline(retailer_id: str, landline: str):
        try:
            return RetailerServices.update_retailer_landline(retailer_id, landline)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_retailer_business_email(retailer_id: str, business_email: str):
        try:
            return RetailerServices.update_retailer_business_email(retailer_id, business_email)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
