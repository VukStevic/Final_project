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
    name: str
    description: str

    class Config:
        orm_mode = True
