from typing import Optional
from pydantic import BaseModel, UUID4


class BusinessTypeSchema(BaseModel):
    id: UUID4
    name: str
    description: str

    class Config:
        orm_mode = True


class BusinessTypeSchemaIn(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True


class BusinessTypeSchemaUpdate(BaseModel):
    id: str
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True
