from app.db import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.orders.models import Order
from app.products.models import Product


class OrderProduct(Base):
    __tablename__ = "order_product"
    order_id = Column(String(90), ForeignKey("orders.id"), primary_key=True)
    product_id = Column(String(90), ForeignKey("products.id"), primary_key=True)

    order = relationship("Order", lazy="subquery")
    product = relationship("Product", lazy="subquery")

# class OrderProduct(Base):
#     __tablename__ = 'order_products'
#     order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
#     product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
#     order = relationship("Order", back_populates="order_products")
#     product = relationship("Product", back_populates="order_products")
#
#     Order.order_products = relationship("OrderProduct", back_populates="order")
#     Product.order_products = relationship("OrderProduct", back_populates="product")
#
    def __init__(self, order_id: str, product_id: str):
        self.order_id = order_id
        self.product_id = product_id
