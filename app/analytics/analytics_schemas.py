from typing import Optional, List
from pydantic import BaseModel
from app.payments.schemas import PaymentSchema


class WholesalerRevenueSchema(BaseModel):
    wholesaler_id: str
    total_wholesaler_revenue: float
    payments: Optional[List[PaymentSchema]] = None
