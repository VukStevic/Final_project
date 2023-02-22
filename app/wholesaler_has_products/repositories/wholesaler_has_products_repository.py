from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.wholesaler_has_products.exceptions import WholesalerProductNotFoundException
from app.wholesaler_has_products.models.wholesaler_has_products import WholesalerHasProducts


class WholesalerHasProductsRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_wholesaler_product(self, wholesaler_id: str, product_id: str, price: float, quantity_available: float):
        """
        It creates a new wholesaler_has_products entry in the database
        """
        try:
            wholesaler_has_products = WholesalerHasProducts(wholesaler_id=wholesaler_id, product_id=product_id,
                                                            price=price, quantity_available=quantity_available)
            self.db.add(wholesaler_has_products)
            self.db.commit()
            self.db.refresh(wholesaler_has_products)
            return wholesaler_has_products
        except IntegrityError as e:
            raise e

    def get_all_wholesaler_products(self):
        """
        It returns all the products that a wholesaler has
        """
        wholesaler_has_products = self.db.query(WholesalerHasProducts).all()
        return wholesaler_has_products

    def get_wholesaler_product_by_wholesaler_id(self, wholesaler_id: str):
        """
        It returns a list of products that a wholesaler has
        """
        wholesaler_has_products = self.db.query(WholesalerHasProducts).filter(WholesalerHasProducts.wholesaler_id ==
                                                                              wholesaler_id).first()
        return wholesaler_has_products

    def get_wholesaler_product_by_id(self, id: str):
        """
        It returns a wholesaler_has_products object from the database, given the id of the wholesaler_has_products object
        """
        wholesaler_has_products = self.db.query(WholesalerHasProducts).filter(WholesalerHasProducts.id ==
                                                                              id).first()
        return wholesaler_has_products

    def get_wholesaler_product_by_product_id(self, product_id: str):
        """
        It returns a wholesaler_has_products object from the database, given a product_id
        """
        wholesaler_has_products = self.db.query(WholesalerHasProducts).filter(WholesalerHasProducts.product_id ==
                                                                              product_id).first()
        return wholesaler_has_products

    def delete_wholesaler_product_by_wholesaler_id(self, wholesaler_id: str):
        """
        It deletes a wholesaler product by wholesaler id
        """
        try:
            wholesaler_has_products = self.db.query(WholesalerHasProducts).\
                filter(WholesalerHasProducts.wholesaler_id == wholesaler_id).first()
            self.db.delete(wholesaler_has_products)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def delete_wholesaler_product_by_product_id(self, product_id: str):
        """
        It deletes a product from a wholesaler's inventory
        """
        try:
            wholesaler_has_products = self.db.query(WholesalerHasProducts).\
                filter(WholesalerHasProducts.product_id == product_id).first()
            self.db.delete(wholesaler_has_products)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_wholesaler_product(self, wholesaler_id: str, product_id: str, price: float,
                                  quantity_available: float):
        """
        Updates a wholesaler product
        """
        wholesaler_product = self.db.query(WholesalerHasProducts)\
            .filter(WholesalerHasProducts.wholesaler_id == wholesaler_id,
                    WholesalerHasProducts.product_id == product_id).first()
        if not wholesaler_product:
            raise WholesalerProductNotFoundException(code=400, message=f"Wholesaler product with provided id: {id} "
                                                                       f"not found.")
        if price is not None:
            wholesaler_product.price = price
        if quantity_available is not None:
            wholesaler_product.quantity_available = quantity_available
        self.db.add(wholesaler_product)
        self.db.commit()
        self.db.refresh(wholesaler_product)
        return wholesaler_product
