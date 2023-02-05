
from pydantic import BaseModel, UUID4, EmailStr


class UserSchema(BaseModel):
    id: UUID4
    username: str
    email = str
    password = str
    is_active = bool
    is_superuser = bool

    class Config:
        orm_mode = True


class UserSchemaIn(BaseModel):
    email = EmailStr
    password = str

    class Config:
        orm_mode = True


class UserSchemaUpdate(BaseModel):
    current_password: str
    new_password: str

    class Config:
        orm_mode = True
