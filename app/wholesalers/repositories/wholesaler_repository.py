from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.wholesalers.exceptions.wholesaler_exceptions import WholesalerNotFound
from app.wholesalers.models import Wholesaler


class WholesalerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_wholesaler(self, name, hq_location, landline, business_email, business_type_id, user_id):
        """
        It creates a wholesaler
        """
        try:
            wholesaler = Wholesaler(name, hq_location, landline, business_email, business_type_id, user_id)
            self.db.add(wholesaler)
            self.db.commit()
            self.db.refresh(wholesaler)
            return wholesaler
        except IntegrityError as e:
            raise e

    def get_all_wholesalers(self):
        """
        It returns all the wholesalers in the database
        """
        wholesalers = self.db.query(Wholesaler).all()
        return wholesalers

    def get_wholesaler_by_id(self, wholesaler_id: str):
        """
        It returns a wholesaler object from the database, given a wholesaler id
        """
        wholesaler = self.db.query(Wholesaler).filter(Wholesaler.id == wholesaler_id).first()
        return wholesaler

    def delete_wholesaler_by_id(self, wholesaler_id: str):
        """
        It deletes a wholesaler from the database by their id
        """
        try:
            wholesaler = self.db.query(Wholesaler).filter(Wholesaler.id == wholesaler_id).first()
            self.db.delete(wholesaler)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_wholesaler(self, wholesaler_id: str, name: str, hq_location: str, landline: str, business_email: str):
        """
        It updates the wholesaler with the given wholesaler_id with the given name, hq_location,
        landline and business_email
        """
        wholesaler = self.db.query(Wholesaler).filter(Wholesaler.id == wholesaler_id).first()
        if not wholesaler:
            raise WholesalerNotFound(code=400, message=f"Wholesaler with provided wholesaler id: {wholesaler_id} "
                                                       f"not found.")
        if hq_location is not None:
            wholesaler.hq_location = hq_location
        if name is not None:
            wholesaler.name = name
        if landline is not None:
            wholesaler.landline = landline
        if business_email is not None:
            wholesaler.business_email = business_email
        self.db.add(wholesaler)
        self.db.commit()
        self.db.refresh(wholesaler)
        return wholesaler
