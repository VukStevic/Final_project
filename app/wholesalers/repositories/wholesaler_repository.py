from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.wholesalers.models import Wholesaler


class WholesalerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_wholesaler(self, name, hq_location, landline, business_email, business_type_id, user_id):
        try:
            wholesaler = Wholesaler(name, hq_location, landline, business_email, business_type_id, user_id)
            self.db.add(wholesaler)
            self.db.commit()
            self.db.refresh(wholesaler)
            return wholesaler
        except IntegrityError as e:
            raise e

    def get_all_wholesalers(self):
        wholesalers = self.db.query(Wholesaler).all()
        return wholesalers

    def get_wholesaler_by_id(self, wholesaler_id: str):
        wholesaler = self.db.query(Wholesaler).filter(Wholesaler.id == wholesaler_id).first()
        return wholesaler

    def delete_wholesaler_by_id(self, wholesaler_id: str):
        try:
            wholesaler = self.db.query(Wholesaler).filter(Wholesaler.id == wholesaler_id).first()
            self.db.delete(wholesaler)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_wholesaler_name(self, wholesaler_id: str, name: str):
        try:
            wholesaler = self.db.query(Wholesaler).filter(Wholesaler.id == wholesaler_id).first()
            wholesaler.name = name
            self.db.add(wholesaler)
            self.db.commit()
            self.db.refresh(wholesaler)
            return wholesaler
        except Exception as e:
            raise e

    def update_wholesaler_landline(self, wholesaler_id: str, landline: str):
        try:
            wholesaler = self.db.query(Wholesaler).filter(Wholesaler.id == wholesaler_id).first()
            wholesaler.landline = landline
            self.db.add(wholesaler)
            self.db.commit()
            self.db.refresh(wholesaler)
            return wholesaler
        except Exception as e:
            raise e

    def update_wholesaler_business_email(self, wholesaler_id: str, business_email: str):
        try:
            wholesaler = self.db.query(Wholesaler).filter(Wholesaler.id == wholesaler_id).first()
            wholesaler.business_email = business_email
            self.db.add(wholesaler)
            self.db.commit()
            self.db.refresh(wholesaler)
            return wholesaler
        except Exception as e:
            raise e
