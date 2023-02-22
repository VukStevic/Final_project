from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.retailers.exceptions.retailer_exceptions import RetailerNotFound
from app.retailers.models import Retailer


class RetailerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_retailer(self, name, hq_location, landline, business_email, business_type_id, user_id):
        """
        It creates a retailer
        """
        try:
            retailer = Retailer(name, hq_location, landline, business_email, business_type_id, user_id)
            self.db.add(retailer)
            self.db.commit()
            self.db.refresh(retailer)
            return retailer
        except IntegrityError as e:
            raise e

    def get_all_retailers(self):
        """
        It returns all the retailers in the database
        """
        retailers = self.db.query(Retailer).all()
        return retailers

    def get_retailer_by_id(self, retailer_id: str):
        """
        It returns a retailer object from the database, given a retailer id
        """
        retailer = self.db.query(Retailer).filter(Retailer.id == retailer_id).first()
        return retailer

    def delete_retailer_by_id(self, retailer_id: str):
        """
        It deletes a retailer from the database by its id
        """
        try:
            retailer = self.db.query(Retailer).filter(Retailer.id == retailer_id).first()
            self.db.delete(retailer)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_retailer(self, retailer_id: str, name: str, hq_location: str, landline: str, business_email: str):
        """
        It updates the retailer with the given id, with the given name, hq_location, landline and business_email
        """
        retailer = self.db.query(Retailer).filter(Retailer.id == retailer_id).first()
        if not retailer:
            raise RetailerNotFound(code=400, message=f"Retailer with provided id {retailer_id} not found.")
        if hq_location is not None:
            retailer.hq_location = hq_location
        if name is not None:
            retailer.name = name
        if landline is not None:
            retailer.landline = landline
        if business_email is not None:
            retailer.business_email = business_email
        self.db.add(retailer)
        self.db.commit()
        self.db.refresh(retailer)
        return retailer

