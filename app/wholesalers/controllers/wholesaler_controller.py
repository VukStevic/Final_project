from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.wholesalers.exceptions.wholesaler_exceptions import WholesalerNotFound
from app.wholesalers.services import WholesalerServices


class WholesalerController:
    @staticmethod
    def create_wholesaler(name, hq_location, landline, business_email, business_type_id, user_id):
        """
        It creates a wholesaler
        """
        try:
            wholesaler = WholesalerServices.create_wholesaler(name, hq_location, landline, business_email,
                                                              business_type_id, user_id)
            return wholesaler
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"Wholesaler with provided business email - {business_email} already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_wholesalers():
        """
        This function returns a list of all wholesalers in the database
        """
        wholesalers = WholesalerServices.get_all_wholesalers()
        return wholesalers

    @staticmethod
    def get_wholesaler_by_id(wholesaler_id: str):
        """
        It gets a wholesaler by id
        """
        wholesaler = WholesalerServices.get_wholesaler_by_id(wholesaler_id)
        if wholesaler:
            return wholesaler
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Wholesaler with provided id {wholesaler_id} does not exist",
            )

    @staticmethod
    def delete_wholesaler_by_id(wholesaler_id: str):
        """
        It deletes a wholesaler from the database by its id
        """
        try:
            WholesalerServices.delete_wholesaler_by_id(wholesaler_id)
            return {"message": f"Wholesaler with provided id, {wholesaler_id}, is deleted."}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_wholesaler(wholesaler_id: str, name: str, hq_location: str, landline: str, business_email: str):
        """
        It updates the wholesaler with the given wholesaler_id with the given name, hq_location, landline, and
        business_email
        """
        try:
            return WholesalerServices.update_wholesaler(wholesaler_id, name, hq_location, landline, business_email)
        except WholesalerNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
