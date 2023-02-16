from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.wholesaler_has_products.models.wholesaler_has_products import WholesalerHasProducts


class WholesalerHasProductsRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_wholesaler_product(self, wholesaler_id: str, product_id: str):
        try:
            wholesaler_has_products = WholesalerHasProducts(wholesaler_id=wholesaler_id, product_id=product_id)
            self.db.add(wholesaler_has_products)
            self.db.commit()
            self.db.refresh(wholesaler_has_products)
            return wholesaler_has_products
        except IntegrityError as e:
            raise e

    def get_all_wholesaler_products(self):
        wholesaler_has_products = self.db.query(WholesalerHasProducts).all()
        return wholesaler_has_products

    def get_wholesaler_product_by_wholesaler_id(self, wholesaler_id: str):
        wholesaler_has_products = self.db.query(WholesalerHasProducts).filter(WholesalerHasProducts.wholesaler_id ==
                                                                              wholesaler_id).first()
        return wholesaler_has_products

    def get_wholesaler_product_by_product_id(self, product_id: str):
        wholesaler_has_products = self.db.query(WholesalerHasProducts).filter(WholesalerHasProducts.product_id ==
                                                                              product_id).first()
        return wholesaler_has_products

    def delete_wholesaler_product_by_wholesaler_id(self, wholesaler_id: str):
        try:
            wholesaler_has_products = self.db.query(WholesalerHasProducts).\
                filter(WholesalerHasProducts.wholesaler_id == wholesaler_id).first()
            self.db.delete(wholesaler_has_products)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def delete_wholesaler_product_by_product_id(self, product_id: str):
        try:
            wholesaler_has_products = self.db.query(WholesalerHasProducts).\
                filter(WholesalerHasProducts.product_id == product_id).first()
            self.db.delete(wholesaler_has_products)
            self.db.commit()
            return True
        except Exception as e:
            raise e
