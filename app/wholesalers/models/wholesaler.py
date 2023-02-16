from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey
from uuid import uuid4


class Wholesaler(Base):
    __tablename__ = "wholesalers"
    id = Column(String(90), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(90), unique=True)
    hq_location = Column(String(90))
    landline = Column(String(90))
    business_email = Column(String(90))

    business_type_id = Column(String(90), ForeignKey("business_types.id"))
    business_type = relationship("BusinessType", lazy='subquery')

    user_id = Column(String(90), ForeignKey("users.id"))
    user = relationship("User", lazy='subquery')

    def __init__(self, name: str, hq_location: str, landline: str, business_email: str, business_type_id: str,
                 user_id: str):
        self.name = name
        self.hq_location = hq_location
        self.landline = landline
        self.business_email = business_email
        self.business_type_id = business_type_id
        self.user_id = user_id
