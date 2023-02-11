from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.business_types.models import BusinessType


class BusinessTypeRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_business_type(self, name: str, description: str):
        try:
            business_type = BusinessType(name=name, description=description)
            self.db.add(business_type)
            self.db.commit()
            self.db.refresh(business_type)
            return business_type
        except IntegrityError as e:
            raise e

    def get_all_business_types(self):
        business_types = self.db.query(BusinessType).all()
        return business_types

    def get_business_type_by_id(self, business_type_id: str):
        business_type = self.db.query(BusinessType).filter(BusinessType.id == business_type_id).first()
        return business_type

    def delete_business_type_by_id(self, business_type_id: str):
        try:
            business_type = self.db.query(BusinessType).filter(BusinessType.id == business_type_id).first()
            self.db.delete(business_type)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_business_type_name(self, business_type_id: str, name: str):
        try:
            business_type = self.db.query(BusinessType).filter(BusinessType.id == business_type_id).first()
            business_type.name = name
            self.db.add(business_type)
            self.db.commit()
            self.db.refresh(business_type)
            return business_type
        except Exception as e:
            raise e

    def update_business_type_description(self, business_type_id: str, description: str):
        try:
            business_type = self.db.query(BusinessType).filter(BusinessType.id == business_type_id).first()
            business_type.description = description
            self.db.add(business_type)
            self.db.commit()
            self.db.refresh(business_type)
            return business_type
        except Exception as e:
            raise e
