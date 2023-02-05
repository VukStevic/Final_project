
from app.db.database import Base
from sqlalchemy import Column, String, Boolean
from uuid import uuid4


class User(Base):
    __tablename__ = "users"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    username = Column(String(20), unique=True)
    email = Column(String(30))
    password = Column(String(50))
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    def __init__(self, username: str, email: str, password: str, is_active: bool, is_superuser: bool):
        self.is_superuser = is_superuser
        self.is_active = is_active
        self.password = password
        self.email = email
        self.username = username
