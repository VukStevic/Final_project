
from app.db.database import Base
from sqlalchemy import Column, String, Boolean
from uuid import uuid4


class User(Base):
    __tablename__ = "users"
    id = Column(String(90), primary_key=True, default=uuid4, autoincrement=False)
    username = Column(String(90), unique=True)
    email = Column(String(90))
    password = Column(String(90))
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    def __init__(self, username: str, email: str, password: str, is_active=True, is_superuser=False):
        self.username = username
        self.email = email
        self.password = password
        self.is_active = is_active
        self.is_superuser = is_superuser
        
