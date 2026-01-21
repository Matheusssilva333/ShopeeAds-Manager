from fastapi import APIRouter
from datetime import datetime, timedelta
import random

router = APIRouter()

@router.get("/metrics")
async def get_metrics():
    """Retorna métricas para o dashboard (Simuladas)"""
    return {
        "revenue_total": 12450.00,
        "revenue_delta": "+12%",
        "orders_total": 124,
        "orders_delta": "+5%",
        "commission_estimated": 1867.50,
        "commission_delta": "+8%",
        "conversion_rate": 3.2,
        "conversion_delta": "-0.5%"
    }

@router.get("/trends")
async def get_trends():
    """Retorna dados de tendência para os gráficos"""
    dates = [(datetime.now() - timedelta(days=x)).strftime("%Y-%m-%d") for x in range(7)]
    dates.reverse()
    
    return {
        "sales_trend": [
            {"date": d, "value": random.randint(1000, 3000)} for d in dates
        ],
        "orders_trend": [
            {"date": d, "value": random.randint(10, 30)} for d in dates
        ]
    }
