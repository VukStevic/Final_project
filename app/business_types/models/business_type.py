from app.db.database import Base
from sqlalchemy import Column, String
from uuid import uuid4


class BusinessType(Base):
    __tablename__ = "business_types"
    id = Column(String(90), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(90), unique=True)
    description = Column(String(90))

    def __init__(self, id: str, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description

