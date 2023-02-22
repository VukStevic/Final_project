from pydantic import BaseModel, UUID4


class PaymentSchema(BaseModel):
    id: UUID4
    payment_amount: float
    order_id: str

    class Config:
        orm_mode = True


class PaymentSchemaIn(BaseModel):
    order_id: str

    class Config:
        orm_mode = True


class PaymentSchemaUpdate(BaseModel):
    order_id: str

    class Config:
        orm_mode = True


class PaymentBYWholesalerSchema(BaseModel):
    id: UUID4
    payment_amount: float
    order_id: str
    wholesaler_id: str
    # order: OrderSchema

    class Config:
        orm_mode = True
