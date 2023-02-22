from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.retailers.exceptions.retailer_exceptions import RetailerNotFound
from app.retailers.services import RetailerServices


class RetailerController:
    @staticmethod
    def create_retailer(name, hq_location, landline, business_email, business_type_id, user_id):
        """
        It creates a retailer
        """
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
        """
        This function returns a list of all retailers in the database
        """
        retailers = RetailerServices.get_all_retailers()
        return retailers

    @staticmethod
    def get_retailer_by_id(retailer_id: str):
        """
        It gets a retailer by id
        """
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
        """
        It takes a retailer_id as a string, and deletes the retailer with that id
        """
        try:
            RetailerServices.delete_retailer_by_id(retailer_id)
            return {"message": f"Retailer with provided id, {retailer_id}, is deleted."}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_retailer(retailer_id: str, name: str, hq_location: str, landline: str, business_email: str):
        """
        It updates a retailer's details
        """
        try:
            return RetailerServices.update_retailer(retailer_id, name, hq_location, landline, business_email)
        except RetailerNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
