from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class CommissionRecord(BaseModel):
    order_id: str
    product_name: str
    order_time: datetime
    order_status: str
    checkout_amount: float
    estimated_commission: float
    commission_rate: float
    conversion_type: str  # ex: Direta ou Indireta

class CommissionSummary(BaseModel):
    total_orders: int
    total_sales_value: float
    total_estimated_commission: float
    average_commission_rate: float
    records: List[CommissionRecord]
