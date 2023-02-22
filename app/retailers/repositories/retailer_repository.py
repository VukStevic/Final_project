from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.retailers.models import Retailer


class RetailerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_retailer(self, name, hq_location, landline, business_email, business_type_id, user_id):
        try:
            retailer = Retailer(name, hq_location, landline, business_email, business_type_id, user_id)
            self.db.add(retailer)
            self.db.commit()
            self.db.refresh(retailer)
            return retailer
        except IntegrityError as e:
            raise e

    def get_all_retailers(self):
        retailers = self.db.query(Retailer).all()
        return retailers

    def get_retailer_by_id(self, retailer_id: str):
        retailer = self.db.query(Retailer).filter(Retailer.id == retailer_id).first()
        return retailer

    def delete_retailer_by_id(self, retailer_id: str):
        try:
            retailer = self.db.query(Retailer).filter(Retailer.id == retailer_id).first()
            self.db.delete(retailer)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_retailer_name(self, retailer_id: str, name: str):
        try:
            retailer = self.db.query(Retailer).filter(Retailer.id == retailer_id).first()
            retailer.name = name
            self.db.add(retailer)
            self.db.commit()
            self.db.refresh(retailer)
            return retailer
        except Exception as e:
            raise e

    def update_retailer_landline(self, retailer_id: str, landline: str):
        try:
            retailer = self.db.query(Retailer).filter(Retailer.id == retailer_id).first()
            retailer.landline = landline
            self.db.add(retailer)
            self.db.commit()
            self.db.refresh(retailer)
            return retailer
        except Exception as e:
            raise e

    def update_retailer_business_email(self, retailer_id: str, business_email: str):
        try:
            retailer = self.db.query(Retailer).filter(Retailer.id == retailer_id).first()
            retailer.business_email = business_email
            self.db.add(retailer)
            self.db.commit()
            self.db.refresh(retailer)
            return retailer
        except Exception as e:
            raise e

    def update_retailer(self, retailer_id: str, name: str, hq_location: str, landline: str, business_email: str):
        try:
            retailer = self.db.query(Retailer).filter(Retailer.id == retailer_id).first()
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
        except Exception as e:
            raise e
