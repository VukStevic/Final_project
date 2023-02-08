from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey
from uuid import uuid4


class Administrator(Base):
    __tablename__ = "administrators"
    id = Column(String(90), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(90), unique=True)
    surname = Column(String(90))

    user_id = Column(String(90), ForeignKey("users.id"))
    user = relationship("User", lazy='subquery')

    def __init__(self, name: str, surname: str, user_id: str):
        self.name = name
        self.surname = surname
        self.user_id = user_id
